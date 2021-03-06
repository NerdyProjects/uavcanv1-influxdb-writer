# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/angular_acceleration/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.131750 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_acceleration.Scalar
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
                 timestamp:                    _ty_.Optional[uavcan.time.SynchronizedTimestamp_1_0] = None,
                 radian_per_second_per_second: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.sample.angular_acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second_per_second: saturated float32 radian_per_second_per_second
        """
        self._timestamp:                    uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second_per_second: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.radian_per_second_per_second = radian_per_second_per_second if radian_per_second_per_second is not None else 0.0

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
    def radian_per_second_per_second(self) -> float:
        """
        saturated float32 radian_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second_per_second

    @radian_per_second_per_second.setter
    def radian_per_second_per_second(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second_per_second = x
        else:
            raise ValueError(f'radian_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.radian_per_second_per_second):
            if self.radian_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.angular_acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second_per_second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            radian_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.angular_acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second_per_second=%s' % self.radian_per_second_per_second,
        ])
        return f'uavcan.si.sample.angular_acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7TW=h<6_#wvy7?N}j^j89ou-!5YG-v@d7U<GU8QaU#<F4AjnJZ<a%Q+o!gDLhk+cDdHV-W<V1NveDUhF#pOD9*'
        '$wPnwea=q^`U~>db7nZZE60AT0r@*a9-eb}uH3(#`bTtjqWYJ=kq!bKgpRAZk}Q-TF)!qf>nBl~XlZzvpWQVo^G&Asqe05cPs`<x'
        '%RiS(`IH;82=-Spw(qmp(bCZ@O5rq%`&r18%Y2`QTrne)*xB_Ntd;qUyU&$|l~PRP)4#FwrzM@F6Mrv1F7tVp8Kb0^8LrFUgQ6Fh'
        'IOHnxsk@Sg!N{~ZH(-Xj2JICm>P0b?->{Y%8F6QK5c@(UvHXY!k6=L?FuoMiVz#kFoB{3Pf<3<QB0EwgBWdJ5*s<_9*0LY-;QiR}'
        'K3B&bHt%}UxFL`GMwGM*R{BgEH%bDq@_K&dK_du{Ioq&z54X@Ye=8rB`6U-@j02{EaY09!2UnYqq^}aq{Ui>`{FECce!2JG6B84U'
        '1SfG8d0dgCN5;4`F@hN)*ghvI)0ziF%h=~cClM!1feOXcfJE>a8zN)iuQ-h}heGW-2u+mi!}gMNxU*7mp@WIXG+!oClYsXm_=Kcf'
        'wOE>l(yudupcp?>3grxspr%aoIS3T-I8pph8N>#T_f!&%r0Ze$Dq$o7!?;=@n)8auPe86t;i59`!>ZbsaJR}7S!thxTYz!<EX+7s'
        'X%Z6ieRLE2*9((_+P>j_XR8G+AqO%5JGsxm#<%C@2x*b^KXkT^dluN4mt=;luXj6Sz?sr3<UmMY;1-lfYz7XwL$)?6nPX?c?hJBA'
        'k%J@)15gAS2+87@`&?_LWH_izfJ7kD=%KaXHaG^>VnjNi)rch1$W^I_?H~gYgn>2?%nv2_D>jhF#8*;F?bMgq4j~t$-`c*jLzd#i'
        'kh||L6Uc-Ze5pX6&lDs@mZHCI5pMuRiW*Zk2oqMt7y<=-!Kn;?)P#yeXnr4<wP0b05yo`uhrCs>*D88^<fw?lLY<>#7zap-MT2R9'
        'K2W$DLtqFvQ9C6R!nu5AJBhJO%&_jnf_U9hH)vP9Dc+(JSWjZHE}iMeJ9Ov%hdZTM&TsyftK?bLRlY&o&>K(U<REs+{IpvcROYWW'
        'O@SY#kZ{<{j<tlDhgE*Eu(3yU@>#gDkE<H??^+u6^U2i`Ez@4+@qA&d54zr<?zVV~C2>t`h*ky-CE%bG%83W%QGU+t$wMBv7${c;'
        '<xYOl)k&s&4jUnNQwHrKH*Eox+lBzBb}vyJ`c=E`i~DOW8TZ2MFz{Lj3VOe4r<n)k>MD*69kh)4s<wyP=$-a+o2j$rtU5Ipv_@Aj'
        '4JKf*yS5z5BXIe@ck1#+$pj^1Za}ps3Thu+idhOJ%%D8YL86|ts{Geu8mkCZDj_e7I95*}APKX&;;Vum>46U+`vNKoe3(Sg&H}3#'
        'v(rmJ67-^`=T;TB4?Kx#>6H7jC&#iH#=#TrVCVHhi0aKID@KhPE^VIuF7q?Ll;(r#dzTMWHb3bmX_=E33DJYdOCT=b)q6ZjYzw@f'
        ';;2p3XyBZ7eF4Q@iU;}m2Q0u&_&p}^7<YHF5Qg*M*<I23q+FuiLVGZ_(^^7FXEG1&8Oa!j7!d3biD?{UkR>RTPU5+Vf}XH=67fVq'
        'PucG&#L0r5w(HY&ea7OfU7tfdUC?>Ue+F@;pl1<J74)3tKaV(H&<l3|BH~m*U$Sx*5ML_jCBzE_y^MISpjQyj6!c}pxq@D`=U=gU'
        'uUS2>S~=IPzSj_6E$Hir*9!Uu;wuFuh*t}G1M%g8zKM9Hpg%yoT+p`=FBSBMhzkY1Y3*7>yjajBYu_^B`GWq)+WBL|vjttT_O|SO'
        '9cy<RakikV*8Vlb>4L7?du&*LY})%&aXnekEqkw9*1uhQzuR@(>Dv~6V)3UI-?8{Ji$Ayc3yber+_NYw9$I{A@iU8`Tl~V}*A~CA'
        '_^rk7YP>fyX^E>1vD6UVhIp?b_8LMo#9>1`ZHUhr;`4_1q9ML+h;JI=+lKhg5*fVZp#Q_vz(#J@JZ$4IUuMndb-A2R;Fub|DdE{S'
        'dlv?$IrdV7IYnSjt&7E{AUI-uc(P>pNPH(>+}K=Q@2+obZf$LJJL}zU=XQ5(?bhn%T6bf!yV+UWy1m}n+^pwFrT)5Nfn>1@rR~-|'
        'af}3u#FsE^#2r-oFL6=)M|_ou?IZE-j`&snm;dvu(6U|sL})+nCqldai7-Ak#IKLgLh-)%pl(R_#lvCW`fx}+9P4G5;Q@dXF@A1S'
        '%xCMK2xAC;TRd0Vu5jrj`0kJJT43<!f!=@az{2mwnj(Rw$Tc$U0n^@y$;JNoy=BY==YJm8h@f~4000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
