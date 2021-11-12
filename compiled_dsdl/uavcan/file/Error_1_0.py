# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/file/Error.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.018899 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.file.Error
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Error_1_0(_dsdl_.CompositeObject):
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
    OK:             int = 0
    UNKNOWN_ERROR:  int = 65535
    NOT_FOUND:      int = 2
    IO_ERROR:       int = 5
    ACCESS_DENIED:  int = 13
    IS_DIRECTORY:   int = 21
    INVALID_VALUE:  int = 22
    FILE_TOO_LARGE: int = 27
    OUT_OF_SPACE:   int = 28
    NOT_SUPPORTED:  int = 38

    def __init__(self,
                 value: _ty_.Optional[_ty_.Union[int, _np_.uint16]] = None) -> None:
        """
        uavcan.file.Error.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, _np_.uint16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Error_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.file.Error.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Error_1_0._DeserializerTypeVar_) -> Error_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = Error_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.file.Error.1.0'
        assert isinstance(self, Error_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.file.Error.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{@j&U2hvj6irIqq-hfprK$uHbU}dHh^(7LX%R0FoDDKgcP)Puc!1ID?$~#v_0DQ$*4RiOiUew<k&4ve2k^r0<c{rp'
        'G);u;2Wxij%(>^zoH_Tm>wmvoTA2LIy<(iIH1mmKlGBX;Oyi9CBoTu`D6W|`t8FdIM3<6v#s#yl?1N|a7kl4SNKOYB-ze!Yp}F7V'
        'xG|7YNNbkKkV(ZwZehVJJ)MnT*~VgH;ZOU_np=cwEqPpOrtA-hb_I{qRn}CFILp$r{3|4-niB0uUA4WCe84py;)=~~u6RFZX+77h'
        '&*baH+#)g8Bx8ABgKexMctVvX1CcTdcg)@936R_7*D&_Pg|MQ9KWxjIJ49)kr&Olrfu5H!R7_<^vl1CxC#guRS+F>}W|nIrcYE|H'
        '3D|_Yv(Y<^b$A!vhkH|mYf;0(2k@b}L1tL*oz%-lg=ESd?`zdAx2VQBnw_A-mbuxJG;y;E<43bG#?9hG>xxh@Cj03BxU6==Mi_k?'
        'lAzU!S`%8Z1>3VEuxl!h_V@Sp=Rmv}Mjdh#b;H9;&=z;+Kw7RxSJGOXhtldntroP~<S+>9!DY0r?d;6~ce{>I^;S^pM6K@;&3sY!'
        'ng6MW>SlvNv(%G}rq!P$J~&V09`y>U!P7vsR|uYK<!OPlDVHqKLXPbPHoH6X6ju+Q9vs&X3I2BjN9S?i_mPf!!Jd269#>v2w1;Bj'
        'sn-({sW4Ad*=KsXN{tm#e}l$6m$i0OKMqJIipcRn>+9gML*9Kn&ml+M4vCIPyLnK%9PP7t4#|nK-EB6bR_AgB?47|evw6<XNIafe'
        'ql5Ke10KM~@Hsq!L--Ox_y)d%4#e;y41mK3H2e;~f`R8Hx=_mSIVTh)VPBXv(&HnRl0ryLcxpqlL6j(E!ic*B;zVLiS_Ls+)e@br'
        'idV(Z<f>Ck9`0=OyqA@uG~S+QOIC|A&Uiv3>zA3!a^|6GwyEl%s}mphcl?L`bQb-S09BY$vRpft9rA?P7bu=;$dr??1Myc{OqH4T'
        'L=WY9PAQ%!n4DOW?~E|c(1SiX@vt+;L|}dK+nU>7aeX}bZnIOnG;a}6SmRv<qQ-+*V6Djf2^$FP2rhdxp@A*x)cJ3a1UU8;_{Y56'
        'q-o0Y{u_(nUl$F_ETeLKF$!BR?fu63Un<77S4<IXW4Vm6&H>L|H^BiNxxtd_D0uRY|BCZ&nol}oSjJ9A{(qb@e)gIN000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)