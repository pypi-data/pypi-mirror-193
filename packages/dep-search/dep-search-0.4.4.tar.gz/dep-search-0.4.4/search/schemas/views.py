"""Views."""

from typing import List, Union
from pydantic import BaseModel


class TypeCategoryView(BaseModel):
    """Type category view."""

    pk: int
    slug: str

    parent_pk: Union[int, None]

    level: int

    lookup_category_pk: List[int]
    lookup_category_slugs: List[str]

    lookup_event_pk: List[int]
    lookup_event_slugs: List[str]

    lookup_tags: List[int]
