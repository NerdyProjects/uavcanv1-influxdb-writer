# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/custom_data_types/housebus/heating/heatmeter.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:20.593588 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     housebus.heating.heatmeter
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class heatmeter_1_0(_dsdl_.CompositeObject):
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
                 power_w:             _ty_.Optional[_ty_.Union[int, _np_.int16]] = None,
                 flow_rate_lph:       _ty_.Optional[_ty_.Union[int, _np_.int16]] = None,
                 flow_temp_k:         _ty_.Optional[_ty_.Union[int, _np_.int8]] = None,
                 return_temp_k:       _ty_.Optional[_ty_.Union[int, _np_.int8]] = None,
                 delta_temp_mk:       _ty_.Optional[_ty_.Union[int, _np_.int32]] = None,
                 absolute_energy_kwh: _ty_.Optional[_ty_.Union[int, _np_.uint32]] = None,
                 error_code:          _ty_.Optional[_ty_.Union[int, _np_.uint8]] = None) -> None:
        """
        housebus.heating.heatmeter.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param power_w:             saturated int16 power_w
        :param flow_rate_lph:       saturated int16 flow_rate_lph
        :param flow_temp_k:         saturated int8 flow_temp_k
        :param return_temp_k:       saturated int8 return_temp_k
        :param delta_temp_mk:       saturated int24 delta_temp_mk
        :param absolute_energy_kwh: saturated uint32 absolute_energy_kwh
        :param error_code:          saturated uint8 error_code
        """
        self._power_w:             int
        self._flow_rate_lph:       int
        self._flow_temp_k:         int
        self._return_temp_k:       int
        self._delta_temp_mk:       int
        self._absolute_energy_kwh: int
        self._error_code:          int

        self.power_w = power_w if power_w is not None else 0

        self.flow_rate_lph = flow_rate_lph if flow_rate_lph is not None else 0

        self.flow_temp_k = flow_temp_k if flow_temp_k is not None else 0

        self.return_temp_k = return_temp_k if return_temp_k is not None else 0

        self.delta_temp_mk = delta_temp_mk if delta_temp_mk is not None else 0

        self.absolute_energy_kwh = absolute_energy_kwh if absolute_energy_kwh is not None else 0

        self.error_code = error_code if error_code is not None else 0

    @property
    def power_w(self) -> int:
        """
        saturated int16 power_w
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power_w

    @power_w.setter
    def power_w(self, x: _ty_.Union[int, _np_.int16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -32768 <= x <= 32767:
            self._power_w = x
        else:
            raise ValueError(f'power_w: value {x} is not in [-32768, 32767]')

    @property
    def flow_rate_lph(self) -> int:
        """
        saturated int16 flow_rate_lph
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._flow_rate_lph

    @flow_rate_lph.setter
    def flow_rate_lph(self, x: _ty_.Union[int, _np_.int16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -32768 <= x <= 32767:
            self._flow_rate_lph = x
        else:
            raise ValueError(f'flow_rate_lph: value {x} is not in [-32768, 32767]')

    @property
    def flow_temp_k(self) -> int:
        """
        saturated int8 flow_temp_k
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._flow_temp_k

    @flow_temp_k.setter
    def flow_temp_k(self, x: _ty_.Union[int, _np_.int8]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -128 <= x <= 127:
            self._flow_temp_k = x
        else:
            raise ValueError(f'flow_temp_k: value {x} is not in [-128, 127]')

    @property
    def return_temp_k(self) -> int:
        """
        saturated int8 return_temp_k
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._return_temp_k

    @return_temp_k.setter
    def return_temp_k(self, x: _ty_.Union[int, _np_.int8]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -128 <= x <= 127:
            self._return_temp_k = x
        else:
            raise ValueError(f'return_temp_k: value {x} is not in [-128, 127]')

    @property
    def delta_temp_mk(self) -> int:
        """
        saturated int24 delta_temp_mk
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._delta_temp_mk

    @delta_temp_mk.setter
    def delta_temp_mk(self, x: _ty_.Union[int, _np_.int32]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -8388608 <= x <= 8388607:
            self._delta_temp_mk = x
        else:
            raise ValueError(f'delta_temp_mk: value {x} is not in [-8388608, 8388607]')

    @property
    def absolute_energy_kwh(self) -> int:
        """
        saturated uint32 absolute_energy_kwh
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._absolute_energy_kwh

    @absolute_energy_kwh.setter
    def absolute_energy_kwh(self, x: _ty_.Union[int, _np_.uint32]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._absolute_energy_kwh = x
        else:
            raise ValueError(f'absolute_energy_kwh: value {x} is not in [0, 4294967295]')

    @property
    def error_code(self) -> int:
        """
        saturated uint8 error_code
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, x: _ty_.Union[int, _np_.uint8]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 255:
            self._error_code = x
        else:
            raise ValueError(f'error_code: value {x} is not in [0, 255]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: heatmeter_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i16(max(min(self.power_w, 32767), -32768))
        _ser_.add_aligned_i16(max(min(self.flow_rate_lph, 32767), -32768))
        _ser_.add_aligned_i8(max(min(self.flow_temp_k, 127), -128))
        _ser_.add_aligned_i8(max(min(self.return_temp_k, 127), -128))
        _ser_.add_aligned_signed(max(min(self.delta_temp_mk, 8388607), -8388608), 24)
        _ser_.add_aligned_u32(max(min(self.absolute_energy_kwh, 4294967295), 0))
        _ser_.add_aligned_u8(max(min(self.error_code, 255), 0))
        _ser_.pad_to_alignment(8)
        assert 112 <= (_ser_.current_bit_length - _base_offset_) <= 112, \
            'Bad serialization of housebus.heating.heatmeter.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: heatmeter_1_0._DeserializerTypeVar_) -> heatmeter_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "power_w"
        _f0_ = _des_.fetch_aligned_i16()
        # Temporary _f1_ holds the value of "flow_rate_lph"
        _f1_ = _des_.fetch_aligned_i16()
        # Temporary _f2_ holds the value of "flow_temp_k"
        _f2_ = _des_.fetch_aligned_i8()
        # Temporary _f3_ holds the value of "return_temp_k"
        _f3_ = _des_.fetch_aligned_i8()
        # Temporary _f4_ holds the value of "delta_temp_mk"
        _f4_ = _des_.fetch_aligned_signed(24)
        # Temporary _f5_ holds the value of "absolute_energy_kwh"
        _f5_ = _des_.fetch_aligned_u32()
        # Temporary _f6_ holds the value of "error_code"
        _f6_ = _des_.fetch_aligned_u8()
        self = heatmeter_1_0(
            power_w=_f0_,
            flow_rate_lph=_f1_,
            flow_temp_k=_f2_,
            return_temp_k=_f3_,
            delta_temp_mk=_f4_,
            absolute_energy_kwh=_f5_,
            error_code=_f6_)
        _des_.pad_to_alignment(8)
        assert 112 <= (_des_.consumed_bit_length - _base_offset_) <= 112, \
            'Bad deserialization of housebus.heating.heatmeter.1.0'
        assert isinstance(self, heatmeter_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'power_w=%s' % self.power_w,
            'flow_rate_lph=%s' % self.flow_rate_lph,
            'flow_temp_k=%s' % self.flow_temp_k,
            'return_temp_k=%s' % self.return_temp_k,
            'delta_temp_mk=%s' % self.delta_temp_mk,
            'absolute_energy_kwh=%s' % self.absolute_energy_kwh,
            'error_code=%s' % self.error_code,
        ])
        return f'housebus.heating.heatmeter.1.0({_o_0_})'

    _EXTENT_BYTES_ = 32

    _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8WTK5>0{_*O?`s@I7{@QzHfPdkLTpSG?1{CWVD1uM*cS>yBO1M4S`r%sDZ}jUbN39{-C1U4?{b1*Unm9!EOdM$h*tdT{40EB'
        'H@R%?2llN8$IZ?>pXcWJ_1zz?{Q6J5R($NOY!vAzZZQo?@K}7ugBV&Ylu0JFFyQRUXAp~omeJRv4BRvK{uB4TYual}q$wzeHM??X'
        'R34gK!DW-HEaeHgcmrjwA;@(Lfg6$bi{Atc;kM2OptO*w_q2F)wtnV13!U0e?uoO@j2ojwkQ>nMF}a;{=dqQuS3egJM;8}aVi7l-'
        '8GpNZc&2=mVn7yahoYZC^kr(G59)GE%PbIv#gO(5y3Q)O4!Jfgkr6n&X*V98yYX0Sm(IHWh~laJ=nkBHjcLQvh^wgT=;u7ZCA*l('
        'At*L<_6mz+=xoi={*CgVaTDJ>TfNm;#as9e-Y&6~UMz=9aRV&Q(BU0?Zw^+kV#@_)Aj#PA3qvaksLtsNV4Ed&T4E8zz5t#|W?(n%'
        '`lD3O%{sYjRBy4)11)1JH3MqF{)in9XT<&K>=2efDXFN%eZ>j}?0TigSTHL4*0b;827Z7|+`%pU2tUM+@h;xOPw)%e&8Zh6$P|Q>'
        '`N*BxS6EM+K*Tbs3=@&tw`)wxT!lafF|dqNrES<onLwKcLbZER0R`R8`5@%!U}sCDy*NLKf~}#ViBs(`*G486-K*Q@qtredrS^D~'
        'T05=nR_V!6K*%-yqk`1<Mjwa}+^G+jdMk*vvv<zN;Gzx5&`dr%d;Oj;_lxI4dORzMeTm7;*~UC4dXxk*7SzM*T}UJinW3?MkO8%+'
        'R8<uTQP8O3k$v?ck0Od_$_T&3Z^o-5dt+CoKIQ35m-gk-BL(ioqC!5N;Vmpy*!#a*Qug-qIOb|Jm5*y|z~da;FRs~HeX0Wz+^kGA'
        'No*caJ0v3YN=6HQ;univ&GMLgdWpeF#?wNR_i227D=+f<xi`=O{z=36oW6h2!QbBK5AS$-yUNzbY?F+d)9l3dY<8QBwx`*N?JB!D'
        'X7|WwZ<?LhuCk3Wi)4h;?8Nr$J7;8+RoQwzy{!W;Rk)1TaTV8m)i+3lwn%{PlKAWb?){fI;a8{F*~k0X#r<;b7pasqHO6&o3wDE~'
        't9-31MhX(qPw{rFh^ANEw>t~|tyN0r13V}rdNijqCzEw)Y+pa%X&(+C10&{X!ExDw4FV>US0t&1&*}0$OP#tus6Ew1y2f4DZOl0J'
        'aO+?D>sU<n2mk;'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
