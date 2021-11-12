# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/electric_current/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.227649 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.electric_current.Scalar
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
                 ampere: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.electric_current.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param ampere: saturated float32 ampere
        """
        self._ampere: float

        self.ampere = ampere if ampere is not None else 0.0

    @property
    def ampere(self) -> float:
        """
        saturated float32 ampere
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ampere

    @ampere.setter
    def ampere(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._ampere = x
        else:
            raise ValueError(f'ampere: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.ampere):
            if self.ampere > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.ampere < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.ampere)
        else:
            _ser_.add_aligned_f32(self.ampere)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.electric_current.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "ampere"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            ampere=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.electric_current.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'ampere=%s' % self.ampere,
        ])
        return f'uavcan.si.unit.electric_current.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YWNl#Qk5FW!Kf=h_RtDIO4yf-U84qi0jGJ-^mH`D2D=5^9<NiXA!35gsul60a8<sbBySj`L$VtA+OS5;rv_tn>5'
        '7JvO-Xk2~ac|8$U=!95l6xHf8Wm+bLS4CY}<s^hhr_OlpypiuGwS-I9J%=;c2}`7;1?IOr9dTMFRwcevE|FStXA~#g8zW1XoN}tE'
        'fv`eG(pXiMkT=5p53~3Z`uF;cZ*UG_jZlZ3%sXk}BiuFH-y#T0he~QOpJ|l{>L_t>(7W1eqYCBJ2rC{O>WaF5X{`~a9MQ5Ix*YnO'
        '2+65+q^N|1d?P$Nxo(eb$!p9V#T3$Le1&%qHi&h!6x4{DK;IFkphMKhi+J(CQ0|bvMOhAKF=B-6PPf_4+MVwHekbd-v#fWJwOTKl'
        '-B#A=X5C(E|DfILcAF6I@+@Bp%e1JaLCi%WDh{E6ziD`SLrTIX(^Z{8zMZdIq$p%<B&SXaxCoEQK#ip!b!8k;0*=Evv6VMmVnRz&'
        'QzQ^3X<ijF^(baKsEky@GM#RI)Y?<!K>M*^d!Gz?#-z1p8XaKd(Cc{1d@Xj?lv<TWyQH`6l1}ZCw322rEd^wgQ;T!NeB9<paS0ds'
        'PQHt*nMM(}u6I4x91Gp;GlYk)lzVe^KE>l~>tTUZHH6K(K<uPo6%xWpj$~1xlj6SKqVCjHX6~J3!gGaw%(L+1gbJa`;eSQ>%a}d('
        '8c9xWXAxmUwU_V%cKVw?EyG7sPl2Gn;u+E{R2glF0UgKSezYd49J^PE9M`nGdRNDuS>{>t2i!Bss_g>+00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
