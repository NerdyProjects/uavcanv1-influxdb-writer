# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/mass/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.155554 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.mass.Scalar
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import uavcan.time


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
                 timestamp: _ty_.Optional[uavcan.time.SynchronizedTimestamp_1_0] = None,
                 kilogram:  _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.sample.mass.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param kilogram:  saturated float32 kilogram
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._kilogram:  float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.kilogram = kilogram if kilogram is not None else 0.0

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def kilogram(self) -> float:
        """
        saturated float32 kilogram
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kilogram

    @kilogram.setter
    def kilogram(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kilogram = x
        else:
            raise ValueError(f'kilogram: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.kilogram):
            if self.kilogram > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kilogram < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kilogram)
        else:
            _ser_.add_aligned_f32(self.kilogram)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.mass.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "kilogram"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            kilogram=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.mass.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'kilogram=%s' % self.kilogram,
        ])
        return f'uavcan.si.sample.mass.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7-EJJW6_#wv`txsOJC5TdbedXH>z$QWT6vu|ZC#~q0>-jo*^SVmopNTVCE=OjmgGp<00o+h78Wo-2gnr2Bjgcs'
        'S+u<fP@va&grHB5%bqjCS*;xVt^%a*40(9Y;rXThbn0(+&Q4T6`CEfwWTM#f4cC&z@)H)s-19?~43v?Um-*RktFzE%nm-;6c==hm'
        '{Au~eaw(tkQ<lK~^^EO>EcJ}^3`+)ZI$_3m+aZgYF7p|Gk82}UT8fE$`d5zrtfZ54;xFZ=Wj^mSYqbnA%T4)P5d0F8MqFh+bx-m*'
        'Ix=O>kC<h?Mf=2wdQnW}H=JcwCfwT|rlHU(m7nnFF)SDh#+G7Q%r=&YGoW2uaK{&3X2(FwL|VBAb}T$ejqIm9`Y^S;&-HN!&HI70'
        'e$3Op6(#L~l_4|MPgDd}UeB*QYy{ykZxi<J;}*K+&*h^szvP3BX~c9iF6b}|;A-=U47D;mRB2S^r~F8T<<5UkOiVl$oTOP2a81-M'
        '8RIg<3TBC5dz=g)Ks+KwrXeRrC7dt~Dm2qWlE7zbiA;gN;<Vlz3U%usRB73V?Ir1P?^eZy4kiIJe3?i?BEBoZCuG2Niwy>`44H+P'
        'dj!RVnbs(0bObeJhR;EuNWh8af5;#<aC}#*<Vd<1g|8AuAjd4%w}|1qVhR<=H3PV)O#85^_axk{GDTL}=inA#+#ZWFj#gSlQoe_7'
        'f<L>l+OO>!?RPg?;1aSgBe0W)3~YRNZjO)^>HMy{aon@O&H|NL(&_ZNWXPE|x5&Pbp};LDiPR1~a+hqZS2D-Wg54S9jwbsmiz843'
        '8VJeKl!x3Hre!>=O@Kro(wdRA;5Il0)?!4upw$YM8RV+e!*-N`2*N-c2<8V8{FPeBV-jj<r19#@Y{rlaGHh+$-6Bh=vgF?T%LFnZ'
        '1z&2=7cvb=kqyvaw@EOBB1Me@HjEXkVhn+TKHyb`KW;)r5;VUL%to*{#t37&^<&<u*lQKL{K!!WhlM&v?I;eA6pI$q0)3!yH-*3u'
        'aH8=_D1>wQ%%)1QOzf!c#DaL!Q8#E$ye;0L6If4Tu`ZqICtGyu!N*&rSk7<$nrrpE>MGwLZs?7tsoGDyGC%EC29^06O;g|p14uY*'
        'X2)8>%%dtlS=`toy7??zImA^1`}Z6T`}yQbiI$ll3wXXT)(8DySa(;v#ge!t)<i3Vh7xg53gyJ3@-RQ=@5%!n`4}i)M&(w1(Kjm7'
        'A%~5a`vV5;BDZY;mD`2@==QGC9Qswe?u&b?Et&4d*+CSv_BHf+-5z8Cl&i0KKZ{YzQC~IgP#e9|eql59R=pLk=7QGf3ueFsEOy_O'
        'V|fTJ|Mym1-YA)%WXuhycBP^A(WRKBP{It#)9x$%v{mK58Pixrs8R`eVa2g}0s$({>WZ%l{zwme2-z1<QQ$+BKs$?^V$9A!fh6cf'
        'P0y_=ZVz~rZkYiO<*ppdY8VGkxrd!Mh#{&so2)o$)NpD0{CAn3`MI<oRo~lul(P9rUk%EfyiAB0CV_&ufLHJHM7b9D0BVm}rH=;A'
        'X+IQD?4@{^pMS_A?1bN85>Ie<D~n+`51-!^-M^Mgv{#q_#`d6=P|}$!fO{q~#UTa+J3wL@2N`4u3Z;{HZla(k9G*lxQP5NFdkS%~'
        'pr_sXv|FEXIP2Eu5Kk9$-tnJ7oGIv8#8U-5=lIVf&KLB8+rNl7RnS+QoCU;J3VI3gLP0Mho-61T#4`nb6>+YhSKay7oZf3r&+AUk'
        'b*JwQ#McY@CgQb%zJ>T&K?&m3g5E%UwV-b!UMcAJ5HA<>9mGoo{XXJCL2o*{77;HNbjjJbjCj7FKX7*b5b<n5Z#jEg?!KP0yNx(o'
        '&=qI@D&llOJMJE9&L8XUK2=;#7Ieei>$dZ6&)x4%9e4V!!yh^PvBUQq{>0%=9sbPW2M%`}3Wo;{pE>;8;TI0SboiCSuN{8l@Y@>i'
        '&rCYvYC|kFM6V$}Xo#JL5DjtA5YHOo^M?4MA--&guNva(hWMr-zI8+fZ#n4yFg37|yR`t@ILwz>d-S?o&L?n8joy^-?3=v@gVP>+'
        'DZ-p0FsC|V@fiqCSRbA&89ox<%NN(yS314U+WN-ETCdyb^}2U@tE;zH)>nIL>%H~v>c*W;cYVE{BbEA@r!rQ3n6aQ;{1XO?xQi<O'
        'Aufvlh<{~b^H99MC4P~s|MOfhvRyy_+xYx%*U$g)ksy9~h!%+t#Yc6sc_1E*deX-u>d{!Ax(ve|r(OEOhL_LQ{SHP9{@?IIY1_i5'
        'li-)%!%Kj{ZvcA#z6A@v8Ebe18Xh;uv;#~#M@&BUzV9q!oW1`6j#wROL=6A{'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
