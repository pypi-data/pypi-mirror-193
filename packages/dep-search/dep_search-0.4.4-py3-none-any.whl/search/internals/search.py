"""Search types."""

from __future__ import annotations

from typing import Any, Dict, List, Union, Type

from dataclasses import dataclass
from logging import getLogger
from httpx import AsyncClient

from pydantic import BaseModel

from .types import Expression
from .fn import SafeEncoder  # noqa

from ..schemas import raws
from ..schemas import views
from ..shared import shared_definitions

TypeDomains = Union[None, List[raws.TypeDomain]]
TypeCategories = Union[None, List[raws.TypeCategory]]
TypeViewCategories = Union[None, List[views.TypeCategoryView]]
TypeCharts = Union[None, List[raws.TypeChart]]
TypeTags = Union[None, List[raws.TypeTag]]
TypePlaces = Union[None, List[raws.TypePlace]]
TypePersons = Union[None, List[raws.TypePerson]]
TypeMarketEvents = Union[None, List[raws.TypeMarketEvent]]

log = getLogger(__name__)


class Results(object):
    """Results."""

    items: List[Any]
    count: int
    total: int

    def is_empty(self) -> bool:
        """Is empty."""

        return not bool(self.items)


@dataclass(frozen=True)
class TypeProxyIndex:

    method: str
    serializer: Type[BaseModel]
    result_class: Union[Results, Any]


@dataclass(frozen=True)
class TagResults(Results):
    """Tag results."""

    items: TypeTags
    count: int
    total: int


@dataclass(frozen=True)
class MarketEventResults(Results):
    """Tag results."""

    items: TypeMarketEvents
    count: int
    total: int


@dataclass(frozen=True)
class DomainResults(Results):
    """Domain results."""

    items: TypeDomains
    count: int
    total: int


@dataclass(frozen=True)
class PlaceResults(Results):
    """Place results."""

    items: TypePlaces
    count: int
    total: int


@dataclass(frozen=True)
class PersonResults(Results):
    """Person results."""

    items: TypePersons
    count: int
    total: int


@dataclass(frozen=True)
class CategoryResults(Results):
    """Category results."""

    items: TypeCategories
    count: int
    total: int


@dataclass(frozen=True)
class ChartResults(Results):
    """Chart results."""

    items: TypeCharts
    count: int
    total: int


_search_config = {
    shared_definitions.IndexNameTag: TypeProxyIndex(
        method=shared_definitions.MethodRawTag,
        serializer=raws.TypeTag,
        result_class=TagResults,
    ),
    shared_definitions.IndexNameCategory: TypeProxyIndex(
        method=shared_definitions.MethodRawCategory,
        serializer=raws.TypeCategory,
        result_class=CategoryResults,
    ),
    shared_definitions.IndexNameChart: TypeProxyIndex(
        method=shared_definitions.MethodRawChart,
        serializer=raws.TypeChart,
        result_class=ChartResults,
    ),
    shared_definitions.IndexNamePerson: TypeProxyIndex(
        method=shared_definitions.MethodRawPerson,
        serializer=raws.TypePerson,
        result_class=PersonResults,
    ),
    shared_definitions.IndexNamePlace: TypeProxyIndex(
        method=shared_definitions.MethodRawPlace,
        serializer=raws.TypePlace,
        result_class=PlaceResults,
    ),
    shared_definitions.IndexNameDomain: TypeProxyIndex(
        method=shared_definitions.MethodRawDomain,
        serializer=raws.TypeDomain,
        result_class=DomainResults,
    ),
    shared_definitions.IndexNameMarketEvent: TypeProxyIndex(
        method=shared_definitions.MethodRawMarketEvent,
        serializer=raws.TypeMarketEvent,
        result_class=MarketEventResults,
    ),
    shared_definitions.IndexNameViewCategory: TypeProxyIndex(
        method=shared_definitions.MethodViewCategory,
        serializer=views.TypeCategoryView,
        result_class=None,
    ),

}


@dataclass
class Search:
    """Async search."""

    url: str
    token: str
    client: AsyncClient

    # Internals ---------------------------------------------------------------

    def clean_params(  # noqa
        self,
        items: Union[List[Any], None],
        total: Union[int, None],
    ):
        """Clean params."""

        exists = bool(items)

        return {
            'items': list() if not exists else items,
            'count': 0 if not exists else len(items),
            'total': 0 if not exists else total,
        }

    def _read_items(self, response: Dict) -> List[Dict]:  # noqa
        """Read items from response."""
        try:
            return response['result']['data']['results']
        except Exception as _any:
            print(f'Error read response items: {_any}')
            return list()

    def _read_count(self, response: Dict) -> int:  # noqa
        """Read count from response."""
        try:
            return int(response['result']['data']['count'])
        except Exception as _any:
            print(f'Error read response count: {_any}')
            return 0

    def _read_total(self, response: Dict) -> int:  # noqa
        """Read total from response."""
        try:
            return int(response['result']['data']['total'])
        except Exception as _any:
            print(f'Error read response total: {_any}')
            return 0

    def _serialize(   # noqa
        self, name:
        str, items: List[Union[BaseModel, Any]],
    ):
        """Serialize items."""

        try:
            raw_class = _search_config[name].serializer
            return [raw_class(**item) for item in items]
        except Exception as _any_exc:
            log.error(f'Serialize error: {_any_exc}')
            return list()

    def _create_message(
        self,
        method: str,
        expression: Union[Any, None],
        sorting: Dict[str, int],
        lang: str,
        page: int,
        limit: int,
    ) -> Dict:
        """Create message payload."""

        raw_expression = expression.eval() if expression else None

        return {
            'jsonrpc': '2.0',
            'id': 0,
            'method': method,
            'params': {
                'query': {
                    'token': str(self.token),
                    'version': shared_definitions.branch_digest,
                    'lang': str(lang),
                    'sorting': sorting,
                    'expression': raw_expression,
                    'page': page,
                    'limit': limit,
                },
            },
        }

    def _get_proxy(self, name: str) -> TypeProxyIndex:  # noqa
        """Proxy by name."""

        return _search_config.get(name)

    async def _make_query(self, message: Dict) -> Union[Dict, None]:
        """Make post query and return response as dict or none."""

        response = await self.client.post(url=self.url, json=message)

        if response.status_code == 200:
            return response.json()

        log.error(f'Search service is not available: {response}')

    async def _lookup(
        self,
        name: str,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Results:

        proxy = self._get_proxy(name)

        message = self._create_message(
            method=proxy.method,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

        response = await self._make_query(message=message)

        if response:
            total = self._read_total(response)
            items = self._serialize(
                name=name,
                items=self._read_items(response),
            )
        else:
            total, items = 0, list()

        return proxy.result_class(
            **self.clean_params(items=items, total=total),
        )

    # Exports -----------------------------------------------------------------

    async def market_events(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[MarketEventResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNameMarketEvent,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def tags(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[TagResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNameTag,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def domains(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[DomainResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNameDomain,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def places(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[PlaceResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNamePlace,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def persons(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[PersonResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNamePerson,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def categories(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[CategoryResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNameCategory,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def charts(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = shared_definitions.lang_base,
        limit: int = 25,
        page: int = 1,
    ) -> Union[ChartResults, Any]:
        """Wrap query."""

        return await self._lookup(
            name=shared_definitions.IndexNameChart,
            expression=expression,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

    async def view_category(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
    ) -> TypeViewCategories:
        """Wrap query."""

        name = shared_definitions.IndexNameViewCategory
        proxy = self._get_proxy(name)

        message = self._create_message(
            method=proxy.method,
            expression=expression,
            sorting=sorting,
            lang=shared_definitions.lang_base,
            limit=100,
            page=1,
        )

        response = await self._make_query(message=message)
        items = response.get('result', list()) if response else list()
        try:
            return [proxy.serializer(**item) for item in items]  # noqa
        except Exception as _seralize_response:  # noqa
            log.error(f'On serialize response view: {_seralize_response}')
            return list()
