"""Shared definitions."""

from ..internals import fn

from ..internals.builtins import ( # noqa
    TypeDigest,
    TypeGist,
    TypeIndexSchema,
    ImportQuerySecureSchema,
    StrictSecureQuerySchema,
    SecureQuery,
)
from ..schemas.views import TypeCategoryView  # noqa
from ..schemas.raws import (  # noqa
    TypeTag,
    TypeMarketEvent,
    TypeDomain,
    TypePlace,
    TypePerson,
    TypeCategory,
    TypeChart,
)

from ..schemas.sources import (  # noqa
    SourceTag,
    SourceMarketEvent,
    SourceDomain,
    SourcePlace,
    SourcePerson,
    SourceCategory,
    SourceChart,
)


lang_base = 'ru'
IndexLanguages = {
    lang_base: 'ru_RU',
    'en': 'en_US',
}

lang_foreign_only = list(IndexLanguages.keys())[1:]
all_languages = [lang_base, *lang_foreign_only]

fallback_digest = '000000'

IndexNameViewCategory = 'ViewCategory'
MethodViewCategory = 'view_category'

IndexNameCategory = 'RawCategory'
MethodRawCategory = 'raw_categories'

IndexNameChart = 'RawChart'
MethodRawChart = 'raw_charts'

IndexNameTag = 'RawTag'
MethodRawTag = 'raw_tags'

IndexNamePerson = 'RawPerson'
MethodRawPerson = 'raw_persons'

IndexNamePlace = 'RawPlace'
MethodRawPlace = 'raw_places'

IndexNameDomain = 'RawDomain'
MethodRawDomain = 'raw_domains'

IndexNameMarketEvent = 'RawMarketEvent'
MethodRawMarketEvent = 'raw_market_events'


_index_meta = {
    # Raws
    IndexNameTag: TypeGist(
        name=IndexNameTag,
        method=MethodRawTag,
        raw=TypeTag.schema(),
        parser=SourceTag,
        src=SourceTag.schema(),
        model=None,
    ),
    IndexNameDomain: TypeGist(
        name=IndexNameDomain,
        method=MethodRawDomain,
        raw=TypeDomain.schema(),
        parser=SourceDomain,
        src=SourceDomain.schema(),
        model=None,
    ),
    IndexNameMarketEvent: TypeGist(
        name=IndexNameMarketEvent,
        method=MethodRawMarketEvent,
        raw=TypeMarketEvent.schema(),
        parser=SourceMarketEvent,
        src=SourceMarketEvent.schema(),
        model=None,
    ),
    IndexNamePlace: TypeGist(
        name=IndexNamePlace,
        method=MethodRawPlace,
        raw=TypeMarketEvent.schema(),
        parser=SourcePlace,
        src=SourcePlace.schema(),
        model=None,
    ),
    IndexNamePerson: TypeGist(
        name=IndexNamePerson,
        method=MethodRawPerson,
        raw=TypePerson.schema(),
        parser=SourcePerson,
        src=SourcePerson.schema(),
        model=None,
    ),
    IndexNameCategory: TypeGist(
        name=IndexNameCategory,
        method=MethodRawCategory,
        raw=TypeCategory.schema(),
        parser=SourceCategory,
        src=SourceCategory.schema(),
        model=None,
    ),
    IndexNameChart: TypeGist(
        name=IndexNameChart,
        method=MethodRawChart,
        raw=TypeChart.schema(),
        parser=SourceChart,
        src=SourceChart.schema(),
        model=None,
    ),
    # Views
    IndexNameViewCategory: TypeGist(
        name=IndexNameViewCategory,
        method=MethodViewCategory,
        raw=TypeCategoryView.schema(),
        parser=None,
        src=None,
        model=None,
    ),
}


IndexMeta = _index_meta
branch_digest = fn.digest_branch(languages=all_languages, schema=IndexMeta)
