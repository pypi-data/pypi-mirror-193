from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from ...platform import platform

if TYPE_CHECKING:
    from ..resource import Resource
    from ...formats.sql import IOnRow, IOnProgress


def index(
    self: Resource,
    database_url: str,
    *,
    table_name: Optional[str] = None,
    fast: bool = False,
    qsv_path: Optional[str] = None,
    on_row: Optional[IOnRow] = None,
    on_progress: Optional[IOnProgress] = None,
    use_fallback: bool = False,
) -> None:
    """Index resource into a database"""
    assert table_name, "Table name is required in normal mode"
    indexer = platform.frictionless_formats.sql.SqlIndexer(
        resource=self,
        database_url=database_url,
        table_name=table_name,
        fast=fast,
        qsv_path=qsv_path,
        on_row=on_row,
        on_progress=on_progress,
        use_fallback=use_fallback,
    )
    indexer.index()
