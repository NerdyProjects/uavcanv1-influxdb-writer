# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/Empty.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.489842 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.Empty
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Empty_1_0(_dsdl_.CompositeObject):
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self) -> None:
        """
        uavcan.primitive.Empty.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Empty_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
            'Bad serialization of uavcan.primitive.Empty.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Empty_1_0._DeserializerTypeVar_) -> Empty_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        self = Empty_1_0(
                )
        _des_.pad_to_alignment(8)
        assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
            'Bad deserialization of uavcan.primitive.Empty.1.0'
        assert isinstance(self, Empty_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'uavcan.primitive.Empty.1.0({_o_0_})'

    _EXTENT_BYTES_ = 0

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{?YVO^XyU5N&mJ7e5ifqY8qohwXO%g5arj6jr=Rk#uUN1L-6rm3CTKa4(_|P}uVSnw}XySTUz6UVXgxDxda#e7Rh0'
        'UVi8&6_u$WV$j0qk3t%(p>u<GQ4?~$bwVL^lmfn;Jn}g|J>ye8%vZsRq2TwE7&~EWAM~I}k66DLJWZSrV8jr$v)osC|J^P==k`)t'
        'edaUHH$V^tEfZnn_nhzjm4lqN^H1kGg+5>>2o-<Lw_&N*sKC2GpcOCjU5GA)4hvuqyr7=5ZhALhlZvip=>qDNZMICu<0EaCCask`'
        '`Vfl7(D)>c?jYbQnRyE+K?11gjk~7ix4dQ}uRgAy)mvyL-iuiF2DCIAIqD7z(LGSE<6Loxq=}rL{4!f=0)uu%eJQ7lIp>?tHND*A'
        'Cneokp09xOoFDyfNSp@gij2bN6%MYPl8WK4JqAH8{5jk;=z47w_Yd-&H$o|GSN|0Ck7sm|j1ghFh?WVXFbVk^AGX!^D9fq+b`ZA*'
        'Nfx<-w%k^8Al7rR4}(+1+qwHX;Mxnj`3;LCqfD~?3FbVydXoYG00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
