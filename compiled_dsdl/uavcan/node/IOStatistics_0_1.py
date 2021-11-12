# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/node/IOStatistics.0.1.uavcan
#
# Generated at:  2021-11-11 23:08:22.906523 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.IOStatistics
# Version:       0.1
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class IOStatistics_0_1(_dsdl_.CompositeObject):
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
                 num_emitted:  _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None,
                 num_received: _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None,
                 num_errored:  _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None) -> None:
        """
        uavcan.node.IOStatistics.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param num_emitted:  truncated uint40 num_emitted
        :param num_received: truncated uint40 num_received
        :param num_errored:  truncated uint40 num_errored
        """
        self._num_emitted:  int
        self._num_received: int
        self._num_errored:  int

        self.num_emitted = num_emitted if num_emitted is not None else 0

        self.num_received = num_received if num_received is not None else 0

        self.num_errored = num_errored if num_errored is not None else 0

    @property
    def num_emitted(self) -> int:
        """
        truncated uint40 num_emitted
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_emitted

    @num_emitted.setter
    def num_emitted(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_emitted = x
        else:
            raise ValueError(f'num_emitted: value {x} is not in [0, 1099511627775]')

    @property
    def num_received(self) -> int:
        """
        truncated uint40 num_received
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_received

    @num_received.setter
    def num_received(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_received = x
        else:
            raise ValueError(f'num_received: value {x} is not in [0, 1099511627775]')

    @property
    def num_errored(self) -> int:
        """
        truncated uint40 num_errored
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_errored

    @num_errored.setter
    def num_errored(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_errored = x
        else:
            raise ValueError(f'num_errored: value {x} is not in [0, 1099511627775]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: IOStatistics_0_1._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.num_emitted, 40)
        _ser_.add_aligned_unsigned(self.num_received, 40)
        _ser_.add_aligned_unsigned(self.num_errored, 40)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.node.IOStatistics.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: IOStatistics_0_1._DeserializerTypeVar_) -> IOStatistics_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "num_emitted"
        _f0_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f1_ holds the value of "num_received"
        _f1_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f2_ holds the value of "num_errored"
        _f2_ = _des_.fetch_aligned_unsigned(40)
        self = IOStatistics_0_1(
            num_emitted=_f0_,
            num_received=_f1_,
            num_errored=_f2_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.node.IOStatistics.0.1'
        assert isinstance(self, IOStatistics_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'num_emitted=%s' % self.num_emitted,
            'num_received=%s' % self.num_received,
            'num_errored=%s' % self.num_errored,
        ])
        return f'uavcan.node.IOStatistics.0.1({_o_0_})'

    _EXTENT_BYTES_ = 15

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{@j&-D_M$6i={e>ZX2_v_*Ze(+awU?A?~?Yf*z@Seph@r7t?nojJQRc<;<*KK7%a*awBcfI`O?|60%7yPK>g5nNby'
        '?w#NHov+_H`^%L-x3@RiPrTDCgcDUk9azOG^@5cZ6qK8~F;00%@r`3|1NXtgvqb~xRl5H&{gnD~i)vQm{X2n8In#wU0*ZsD$DVoR'
        'yy7m!Yjg_MDWj9zh}+*S&#%&GW3>5OdYR%5W!_s=1`jTMkEEA`bBaoF>q`ZdI18gk1@nyh9NT5)ja9YsYKn;6Z?#hs4dOt1n1KCf'
        'PCK+zo>rhIUZznd=gfIpV`@p>jJJ<gMA@v^$Ga!_3NzaLHGPxfP3k<;f?2UnbP`Ir6?b%~DWJIrk>V993{P?InFN9tC0Js{#0Ad5'
        'xpAnf1zBPVXpcU@6$yFX?jn`D^7iud?x-){lkdwrotx{~jRg)ErAYE_9Q=oi74Cof=u)xP*v`dYUzr)HnZ}s&OGhM|0x_Hii-@9^'
        'BY-*Mo(LE#jh>9ovD|Cn_Xw7ZNTl!*7KB+K+ytFd&u3LP71S6Y%VvX?0mNP}=nC^7t^uybinE;0@{$;2vNPo%=L2zfO=h%Qbi&Pf'
        '5qU#?BtMV?c|TzD1vFR@mK$^u-=t$T2SFQSJyjwd#v9a`U^(DL1+-z<+W6y8ni_@y1veaHJy2W2ZXl))2TG5tFc;-uW^t74unA?Q'
        'ICf_es_f-Vx^8JS%u_U6pQ7SH@v!JFQN2_$hn_8#BWrxBIHVJK_j!MFW8*Wj5+8BkbA2bEaSk|9x(R-0g2$f>>Zn<@tTQ&uOXfRx'
        'TSq5Ns07glX>f$cm6;X2gE3*`;|Bv&_R5ebhveM0{mC*y@PgE;s<8IlXt75SJj3Tx9>kNMAALd=z^v;?_1R^s8Ml{}K&Gq;&>7Dx'
        'Yg!QThP(i4ie4+K7UI^!EdfQH)1OIfQp=M|ngg{#Yo#Ye9=@`|_4MItTb#`*7S;dzImPRrEB|%-e2kCFZ4qCirb&@pM&cHAX|Ubc'
        'wI@&;+(lWxPa7<;H}-7jT%{aC#W{K$-#TJKV2I~Ha$kOWdU_mh?HiqCsxPFBuXl_nlDt#bEWfybZPcFR;blmS>JWDYvx{?nuF|&t'
        '>G#wh_5W}s?)#=o0QX@ivCOs7d5z+M&GTV9uTs>0w(e1wH%zyG35U2=e&_;WD>iVY6r&>v_#NYg%pjhL&%eIdc8;L=y6v@a{<SMZ'
        'S^N$1ri*tH2LJ#'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
