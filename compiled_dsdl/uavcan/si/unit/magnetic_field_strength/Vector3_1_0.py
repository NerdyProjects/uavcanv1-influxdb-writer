# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.223438 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.magnetic_field_strength.Vector3
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Vector3_1_0(_dsdl_.CompositeObject):
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
    def __init__(self,
                 tesla: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.si.unit.magnetic_field_strength.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param tesla: saturated float32[3] tesla
        """
        self._tesla: _np_.ndarray

        if tesla is None:
            self.tesla = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(tesla, _np_.ndarray) and tesla.dtype == _np_.float32 and tesla.ndim == 1 and tesla.size == 3:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._tesla = tesla
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                tesla = _np_.array(tesla, _np_.float32).flatten()
                if not tesla.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'tesla: invalid array length: not {tesla.size} == 3')
                self._tesla = tesla
            assert isinstance(self._tesla, _np_.ndarray)
            assert self._tesla.dtype == _np_.float32
            assert self._tesla.ndim == 1
            assert len(self._tesla) == 3

    @property
    def tesla(self) -> _np_.ndarray:
        """
        saturated float32[3] tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._tesla = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'tesla: invalid array length: not {x.size} == 3')
            self._tesla = x
        assert isinstance(self._tesla, _np_.ndarray)
        assert self._tesla.dtype == _np_.float32
        assert self._tesla.ndim == 1
        assert len(self._tesla) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Vector3_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.tesla) == 3, 'self.tesla: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.magnetic_field_strength.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Vector3_1_0._DeserializerTypeVar_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "tesla"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            tesla=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.magnetic_field_strength.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'tesla=%s' % _np_.array2string(self.tesla, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.si.unit.magnetic_field_strength.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YXTTc@~6fV*Vh-eVwgFeWU;sd+AY+><DO{&R4C17|n!|cwqGjVU3nXRn}i9Bc|nM4xCU*VthOuJY>yU8Xqdv4$P'
        '&iVFh_1EueW&G%;`G`moJ4jN&am>HqFs2TQvLw$WSJdd0LnVqx6@q>k<<wl57pLaLZ0H(FaRPRyz=H^<j^s{}a^)nrpHjsm)Z;WJ'
        'NGd_ozGBW1jZ`LDMlYfP6_RJEVHLe_RGu$PFc(z5n^U8g5mrj@uuxQ*k7gFezfMNiI=0pn+Z{x(!bn-b`pJxNA@IoPhaEnoWOt15'
        'mHl+R%N0apn$T30$!1{51y8u*1Mpbt#2HrCvn->KD-@55m|z|7MOZ47WP}>_SU=jo47Xv<8?fzJ6L3=bW)1)((1=rl1-Y8&2jsDA'
        'b5#&qxF>L=fJ+G+cgi#5(9c_5z3Dew-qu#jZ#R9vz2i3;+jXzuw>;l#H@0?~ZO^M4TdN555}?a*#MQ_I^SX+{7&1P)Y<vm;I8Zn5'
        'M&EtS)r8JNxRw;?d6eZwug^*%M@g8)JTiK1k0u$=YQewHslc!_QzCDph;f)SYwHIGG>1L=zuztN39z%5;CH`U#4#45n@*5xfa8Li'
        'pJpRiKbIkNUPTE{O>k@vcxVp`c1T5xAt0Euo|SV6w9{dZ)A8PRi_nI$ny$gRf+NI|3>v8bl~}J`*<}=tCYm`hY?rM{SPMdPK_jdv'
        'F=zT7NCtKh<(W{36VuhJNM?nIC>UajatuS)r!LD9>K3qoZZ8v*_fvNw!9in_r@gosl5q300PzYpFG64y3EGDqpvqJivJ7%1cdc&S'
        '8M<{#-8v1YUP>K?gcz29M_6G1kO7aVIb(aQ%N*7i)5|=zJsHMi3j3H4p7#G46<B@vCFB#c2^N9NPH@cL!ut-=1SP@FA1aMil(qx_'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)