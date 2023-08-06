"""Common index types."""

from __future__ import annotations

from typing import Any, Dict, Optional, List, Type, Union, Set
from dataclasses import dataclass

from pydantic import BaseModel, Field

TypePK = int
TypeLang = str
TypeDigest = str
TypeName = str
TypeTranslate = str
TypeI18Field = Dict[TypeLang, TypeTranslate]
TypeDoc = Type[Union[Any, BaseModel]]
Type18nDoc = Dict[TypeLang, TypeDoc]
TypeLookup = Dict[TypePK, Type18nDoc]
TypeSorting = Dict[str, int]
TypeSchemaRaw = Dict
TypeSchemaSrc = Dict


@dataclass
class IndexProperties:
    """Index properties."""

    read_method: str
    write_method: Union[str, None]

    schema_raw: Dict
    schema_source: Union[Dict, None]

    model_raw: Type[BaseModel]
    model_source: Union[Type[BaseModel], None]


@dataclass
class IndexOptions:

    name: str
    properties: IndexProperties
    model: Union[Any, BaseModel, None]
    read_only: bool = False


class PaginatedResponse(BaseModel):
    """Paginated response - overload your results."""

    page: int = Field(example=1)
    limit: int = Field(example=25)
    count: int = Field(example=25)
    last_page: int = Field(example=5)
    total: int = Field(example=125)

    results: List[Dict]


class Meta(BaseModel):
    """Meta schema."""

    pk: str
    lang: str

    checksum: TypeDigest

    commit: Optional[TypeDigest]
    branch: Optional[TypeDigest]

    unwanted: bool = False


class BaseSource(BaseModel):
    """Any removable type source."""

    delete: Optional[bool] = False
    hidden: Optional[bool] = False
    is_hidden: Optional[bool] = False
    is_delete: Optional[bool] = False


class TypeSource(BaseSource):
    """Type source."""

    @classmethod
    def example(cls, **kwargs) -> TypeSource:
        """Create example from values."""

        raise NotImplementedError()

    def exclude_fields(self) -> Set[str]:  # noqa
        """Not used fields."""

        return {
            'id',
            'delete',
            'is_delete',
            'is_deleted',
            'hidden',
            'is_hidden',
        }

    def clean(self) -> Dict:
        """Normalize source data.  Override in child model if needed.

        Accepts validated source.
        Returns a normalized dict for raw model constructor, except meta.
        """

        normalized = self.dict(exclude=self.exclude_fields())
        return normalized


class TypeRaw(BaseModel):
    """Base raw schema."""

    meta: Optional[Meta]

    @classmethod
    def create_unsigned(cls, raw_doc: Dict):
        """Create unsigned."""

        return cls(**raw_doc)

    @classmethod
    def create_with_meta(cls, normalized_doc: Dict, meta: Meta):
        """Raw doc normalizer.  Override in child model if needed.

        Accepts clean and normalized for raw model dict, except meta.
        Returns raw model instance from raw doc.
        """

        normalized_doc.update({'meta': meta})

        return cls(**normalized_doc)


class TypeView(BaseModel):
    """Base view schema."""

    commit: TypeDigest
