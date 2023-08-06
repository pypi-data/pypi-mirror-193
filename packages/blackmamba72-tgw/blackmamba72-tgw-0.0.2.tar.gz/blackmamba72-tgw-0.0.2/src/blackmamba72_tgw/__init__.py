'''
# replace this
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import constructs as _constructs_77d1e7e8


class LambdaConstruct(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="blackmamba72-tgw.LambdaConstruct",
):
    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a9fdb8fadae3042461e99aa3d93f6e2ce37a44d93ecf645312c9a6afb35350)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="sayHello")
    def say_hello(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "sayHello", []))


__all__ = [
    "LambdaConstruct",
]

publication.publish()

def _typecheckingstub__57a9fdb8fadae3042461e99aa3d93f6e2ce37a44d93ecf645312c9a6afb35350(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
