from typing import Callable

from mypy.plugin import MethodContext, Plugin
from mypy.types import Type as MypyType


class CustomPlugin(Plugin):
    def get_method_hook(
        self, fullname: str
    ) -> Callable[[MethodContext], MypyType] | None:
        if fullname.endswith("__pow__"):
            return self._check_pow
        if fullname.endswith("__add__"):
            return self._check_add
        return None

    def _check_add(self, ctx: MethodContext) -> MypyType:
        str_type = ctx.api.named_generic_type("builtins.str", [])

        if ctx.type == str_type:
            ctx.api.fail("Use another method for concatenate strings", ctx.context)
            return ctx.default_return_type

        return str_type

    def _check_pow(self, ctx: MethodContext) -> MypyType:
        int_type = ctx.api.named_generic_type("builtins.int", [])

        if ctx.type == int_type:
            ctx.api.fail("No power between ints in my code!", ctx.context)
            return ctx.default_return_type

        return ctx.api.named_generic_type("builtins.float", [])


def plugin(version: str):
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
