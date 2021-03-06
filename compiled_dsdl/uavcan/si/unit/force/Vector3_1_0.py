# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/force/Vector3.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.249883 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.force.Vector3
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
                 newton: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.si.unit.force.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton: saturated float32[3] newton
        """
        self._newton: _np_.ndarray

        if newton is None:
            self.newton = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(newton, _np_.ndarray) and newton.dtype == _np_.float32 and newton.ndim == 1 and newton.size == 3:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._newton = newton
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                newton = _np_.array(newton, _np_.float32).flatten()
                if not newton.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'newton: invalid array length: not {newton.size} == 3')
                self._newton = newton
            assert isinstance(self._newton, _np_.ndarray)
            assert self._newton.dtype == _np_.float32
            assert self._newton.ndim == 1
            assert len(self._newton) == 3

    @property
    def newton(self) -> _np_.ndarray:
        """
        saturated float32[3] newton
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton

    @newton.setter
    def newton(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._newton = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'newton: invalid array length: not {x.size} == 3')
            self._newton = x
        assert isinstance(self._newton, _np_.ndarray)
        assert self._newton.dtype == _np_.float32
        assert self._newton.ndim == 1
        assert len(self._newton) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Vector3_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.newton) == 3, 'self.newton: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.newton)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.force.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Vector3_1_0._DeserializerTypeVar_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            newton=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.force.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton=%s' % _np_.array2string(self.newton, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.si.unit.force.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YXTTc@~6fRP3A{xZ_peFL9_~34@u=u7X)nuU(Fua*zcIUJ+ac`NKEv*TOJZK=9L=wjT>)EzgK)cB%Gkb2|`Of+F'
        'd-?ZSxioyt^K8HriyWdr3L1%TG>E_<VH#(t5*n;oInXi>buQuaAOm}8U!B?$yJ6-?LSwW)%V{s9iKB#*Cqg@&REFRjLa0+&w`P&_'
        'Kq`?YmY2-J;rM)M{TaXX)1F$hOsLjU1i1!fzu0Mr{yJGR*Afu136i^nQB8?1;F+gW!lk4GYaX>kAJ`5gUCrMXpKkWFLLh<|5<N~f'
        '1xqGHEVSsM$5JawslJ(InFK<UXjsJh>xeI;N|QKcVEGgCc<(B_2y@<}ZMQHXC#4^DA3+kOX~L*v*Aty#o|tx#;+z$QJCcSPxm3t;'
        'YkbBW=4HK6sd=?}V{^0aHEW*N-1e%~txBWn)f--;S>4>OH5-kJEo$X~SweIf4TT<9f7X;q5Mjm_SB*~qAP4&P-I{yvgdWj(fY&hv'
        'W|pLxHS5!os6ia0kqE6>+l4qqS_|->GLRIPW<umV3Aw;Y^QL*Y4;g6jf4@8AD`Mww(C<Mzk0L4ux1BIok48DzUv|S^zfb{oUM8_f'
        'tbbG-Xumit6hq1*iUIyi;aR#+NIUd1nhf{0od-oIpEL6b9Bcf7!7Rm2O2{QOYuA>U1cQ-8PAuQys|xpmK_(%j8kjvd_erN%Mv|pc'
        '6TxiTtP+*xs2(&#Kr)I`H>u0h7~C8;&_!v1=qBz+alPtmk#wTG&w|&-616JbEDw-YBB6^-V3mn5)Hujh!YyR#4rS_&W$IL&iZgP+'
        'nGjADR+ohiuxw9+V9)t3Z*zxNhivi&-x_g0B7KiCCX((ylR>M8e}HUcw*Deg*Yc0}2Yf$b8h^~E^9R4wFLjdy000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
