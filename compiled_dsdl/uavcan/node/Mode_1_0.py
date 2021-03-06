# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/node/Mode.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.909274 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Mode
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Mode_1_0(_dsdl_.CompositeObject):
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
    OPERATIONAL:     int = 0
    INITIALIZATION:  int = 1
    MAINTENANCE:     int = 2
    SOFTWARE_UPDATE: int = 3

    def __init__(self,
                 value: _ty_.Optional[_ty_.Union[int, _np_.uint8]] = None) -> None:
        """
        uavcan.node.Mode.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint3 value
        """
        self._value: int

        self.value = value if value is not None else 0

    @property
    def value(self) -> int:
        """
        saturated uint3 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, _np_.uint8]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 7:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 7]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Mode_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 7), 0), 3)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.node.Mode.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Mode_1_0._DeserializerTypeVar_) -> Mode_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        self = Mode_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Mode.1.0'
        assert isinstance(self, Mode_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Mode.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{@j%-)kH<5I*DBaqZS=a4@vcMlEegh`kplfj;Ev;@WVWy>`!+779gZSF<O<uCz$nv#(HS9$GL6T8R4pcC>f4;}}zN'
        '56A5M{AM)Y{Bh^s7t5XY=O5NnZh4td3r4b1{>HKr5}NC()>b+Q{*x1Dn%p%8M$;O?+wk~J_&q%GOH{E6?VmPmk~5Vk%^^9&zu;Hs'
        '1dNqh1<~<$f11m0!(d_1`768$evLBcjLaGbHvEdoZh>*>75vh^gpyyCU!|NmMqR{oTX=0`C7qn0$Hr@A<yZmlD+gmR*Lzu`nRK)S'
        'HFhEl7BP9wtfN)zMm+GF#}|oWSh9<@wo&Y;^Jf?a|A1P@6laFNo9MjB#FAf{u(Ck}cPQ6+@ST9#b-%K!Rg7_$AjF2)oJ*e#7RBe{'
        'OYv})VeRO6Z`d34kJ8>j5MTMtRGW&GMAu-LlWI&N&?NX}I<NJ`#XR7wHeloUuT5iRh;dr6@}jzU;y)@3%cIt!eSa>a-7h>1u}PaD'
        'm~Z|M>v})!kNUlX{x2=y2siC3EZe?HOi83AQjyx|afJ4gIDwkjL9_rqj{#0(RRNdGK{+L?Kpnwp8Q0VaVin08w0Q0pc0K^z+F`Gs'
        'j`q@Cy1N&leZ7~AlP!`XxXiTZwuptY*v7qdTLfHwqujF(D0lDVXn*u`Z@5QaAOFxBwIz2`I3-pW?vxqm7SdEvh^=Q3pR&}9WB=OV'
        'T!3U+yH;bOhiQ~TpBtE-Ut$8k@eZ|UHl2|)Vk6?dcr3mZFU9v_U%V1Oio*sMp95}4j)Ugm+^^F@o&l$|HjYXjQh%RX-IyHEPy($P'
        'uC>p*LRZjjkZj#T8$e!lXGdVNvn^FoHfKEBJ~engOt)^bQs&gaxG7_mE85z5P&ZzVZX{H)lRQmkN@Oe*%wk1@D-n4;kvW8OoM1k}'
        '!Cc>cq6@-Edx2Jm5S?*^Ef*|4uENn0M9bse6-_*4#K1&GTG$vGCv9uUWg+u+3zA6JtVAY!cfq79ULzRy{&(;nzmo2t{XT(9Qu{@!'
        '>)^?4N$j-BG>!+mJ%mcn8FJM2rp?uTTBf;>c>ToK-#ccUW8XKNL>aAVQ<lt3-?xe<e}_kd#eZyu$GM(m2!oX-!#*piP>cdQi^AP_'
        '_wcbI{?&Lvm}>8L+GKIXlK%jO`<Ssm1^@s'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
