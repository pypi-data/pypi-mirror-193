from __future__ import annotations

import inspect
from typing import TYPE_CHECKING, Any

from attrs import define
from jinja2 import Environment, PackageLoader, select_autoescape

from qtgql.codegen.py.compiler.query import QueryHandlerDefinition

if TYPE_CHECKING:  # pragma: no cover
    from qtgql.codegen.py.compiler.config import QtGqlConfig
    from qtgql.codegen.py.objecttype import GqlEnumDefinition, GqlTypeDefinition

env = Environment(loader=PackageLoader("qtgql.codegen.py"), autoescape=select_autoescape())

SCHEMA_TEMPLATE = env.get_template("schema.jinja.py")
HANDLERS_TEMPLATE = env.get_template("handlers.jinja.py")


@define
class TemplateContext:
    enums: list[GqlEnumDefinition]
    types: list[GqlTypeDefinition]
    queries: list[QueryHandlerDefinition]
    config: QtGqlConfig

    @property
    def dependencies(self) -> list[str]:
        def build_import_statement(t: type[Any]) -> str:
            mod = inspect.getmodule(t)
            assert mod
            return f"from {mod.__name__} import {t.__name__}"

        ret = [build_import_statement(scalar) for scalar in self.config.custom_scalars.values()]
        ret.append(build_import_statement(self.config.base_object))
        return ret

    @property
    def custom_scalars(self) -> list[str]:
        return [scalar.__name__ for scalar in self.config.custom_scalars.values()]

    @property
    def base_object_name(self) -> str:
        return self.config.base_object.__name__


def schema_types_template(context: TemplateContext) -> str:
    return SCHEMA_TEMPLATE.render(context=context)


def handlers_template(context: TemplateContext) -> str:
    return HANDLERS_TEMPLATE.render(context=context)
