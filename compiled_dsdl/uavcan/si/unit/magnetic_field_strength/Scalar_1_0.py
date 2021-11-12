# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.222107 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.magnetic_field_strength.Scalar
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0(_dsdl_.CompositeObject):
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
                 tesla: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.magnetic_field_strength.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param tesla: saturated float32 tesla
        """
        self._tesla: float

        self.tesla = tesla if tesla is not None else 0.0

    @property
    def tesla(self) -> float:
        """
        saturated float32 tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._tesla = x
        else:
            raise ValueError(f'tesla: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.tesla):
            if self.tesla > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.tesla < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.tesla)
        else:
            _ser_.add_aligned_f32(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.magnetic_field_strength.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "tesla"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            tesla=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.magnetic_field_strength.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'tesla=%s' % self.tesla,
        ])
        return f'uavcan.si.unit.magnetic_field_strength.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YW%TE(Q7_Wf}f{zf1S2+nB*zMcp;6)QI6(nN3naS+Vv^&Y{&SoC9H6ek6Mv_T1;q&kGU+|l@Sj2QsGy6S%kGWX='
        '^?Ri@{rvN4!VHrUF<c8O#TS}N9+6BHl`_I|@Q=={cA0gWf0$Gpu3`TY&SB5jNl6QgA2>S7Xc-w1xl-7upu>_|k&%Jmk`ZGyFNZdd'
        '&N3>g2ER^5TpOWE$ZLM><NSOL{d@h|H@F19NvO42q|R~!pJ3UFf0Mx1kHV<MY8!-6ONkBpE-SCJD1;Rw%y@7l6}A7O+a#&5L{3+S'
        '{tmXxsIjC_j6=TdpPk;6hqCAm#*RY>Vbs3Dd+^%`oR*AgcDvDc>=XDA*0C^nplN0izCl`!=4b5TciWvtD`~Ymy<R)%wvwcKm^7O&'
        '8=Yp-?j)UVvv=6)b~+6Rvs{|jeI3b?6#Ob-Dg$4`ztlgy#Ux25Gr`Uw-_5rSB4oVMJfoH~xblxtuQ6w&QrZ&1;KXkcqnyq-1|%mH'
        '#r^$7oU4Mz4!Mj6N^>zR<C*@W=7A^&(v4Yq@L8jCbX>Vqq7O75IvJ)cR5A0S*oZioCSGEicxIZY88xC=1t6%L8e9i6Y|wNhG7eYy'
        'UcQguQ;Af*xKVt;JSN(^ckmBi3;T9@Kf~)>d%r?d1%78)6Ei7Ng}88&V_qoqQ&8<)#Wl4`FC28AWVt|B=81oDN*NR7@V}(|RfwKA'
        'i6AF;qu60YrQ`4e_WC<NO^Q#anl*y{x=RsmA<AG*JkW7CtObK2*`a!a@Nq@U>FYXisYzWL{Q<4!_Eh=<000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
