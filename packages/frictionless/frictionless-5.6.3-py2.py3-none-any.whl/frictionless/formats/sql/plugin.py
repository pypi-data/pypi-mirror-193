from __future__ import annotations
from urllib.parse import urlparse
from ...platform import platform
from ...system import Plugin
from .control import SqlControl
from .parser import SqlParser
from .adapter import SqlAdapter
from . import settings


class SqlPlugin(Plugin):
    """Plugin for SQL"""

    # Hooks

    def create_adapter(self, source, *, control=None):
        if isinstance(source, str):
            parsed = urlparse(source)
            for prefix in settings.SCHEME_PREFIXES:
                if parsed.scheme.startswith(prefix):
                    engine = platform.sqlalchemy.create_engine(source)
                    return SqlAdapter(engine, control=control)  # type: ignore

    def create_parser(self, resource):
        if resource.format == "sql":
            return SqlParser(resource)

    def detect_resource(self, resource):
        if resource.scheme:
            for prefix in settings.SCHEME_PREFIXES:
                if resource.scheme.startswith(prefix):
                    resource.type = "table"
                    resource.scheme = ""
                    resource.format = "sql"
                    resource.mediatype = "application/sql"

    def select_Control(self, type):
        if type == "sql":
            return SqlControl
