# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/time/510.GetSynchronizationMasterInfo.0.1.uavcan
#
# Generated at:  2021-11-11 23:08:23.003773 UTC
# Is deprecated: no
# Fixed port ID: 510
# Full name:     uavcan.time.GetSynchronizationMasterInfo
# Version:       0.1
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import uavcan.time


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class GetSynchronizationMasterInfo_0_1(_dsdl_.FixedPortServiceObject):
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request(_dsdl_.CompositeObject):
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
        def __init__(self) -> None:
            """
            uavcan.time.GetSynchronizationMasterInfo.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: GetSynchronizationMasterInfo_0_1.Request._SerializerTypeVar_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: GetSynchronizationMasterInfo_0_1.Request._DeserializerTypeVar_) -> GetSynchronizationMasterInfo_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = GetSynchronizationMasterInfo_0_1.Request(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
            'ABzY8XQGW^0{?wfU2hyU6x~2+!=?qQ(zJX?wLqXCrL&1d5idMIK`2_Xtr9@IRF-FacWvsi2Y+mKks{g$P%2rXQq4QRg5SsW%m#MT'
            'rmOuJ@AW<Bo^$Q{=)zzBT<o>4c&nLn$5lZcSjm+9m6Zw#TA8{rPI^f3%GaP|jgS2Mc?0QL`s8ssPFwLJm0E*Mq8G0mdK)SqEUa#M'
            'jcQgS#7<z-is{138j5ehAI^0ptkKBkrP2G$d9ZtWY>ET;C4loOuG1-4hrx`0>Bq(Mvo!1t*ZxS4Q{14;dn?P}!KDW&URzqza^5i?'
            '=Y1R+3l&2F=}CNpj^zwEZH)C)@-&K9sWZV=fB^-xVP2&8+d!Ba1_4bOjEx03(SuIIboaK@V-;q+ynSTR6+37`sbobhOoGZRlrzt$'
            'M<?7OX^@2v?(FWoT>MV4TXYFoj$jU}v7mkK%~V#9PT~d1O_hGS`AV<%4H`5j+HfFVFi%+J9bxz;nT@zr8dA4B+r(HR9jRE88%@kO'
            '=Se-unJ!dfyYGYvisPcm9w9bvUldUE_mIPsKLh4WAp?0s8f&H!t3Y3jtvfbWn&8Qikd-(s2kGmUI@l~q%?aAeF$*bxXz)kIJ}mnE'
            'd%A-EMf{f~j03$*q{rH|HlCD#e=<Em46I$5P6HaD0HqS6p)<#<5M(SHv_{FOMiYZEOEALScDrwx_jx8%q~I)`X}~hyB7UiftQ$NI'
            'oegMj>t8l1_ekb7Sk#9f3p{Afw0~K{x~k@cDMg&X?>@TL7U1xJuT;y_5u3Xr;UOuNOY!5=t6fS@73hf<c#{0tb&8k2lK#7PeTd7&'
            '?TxQe)1*kw199`ZG$<60>ORzFQT4sn3S*bYM1`L5BtDF9-e;VnP0wu-TRA!kN-;Y>8%2aEQvuSSX=~Vf>PnmqO$U^Q>!C!swbVEm'
            '@&lXYhfB0J94}+e?o*gGOt<4>6iQcyQuM`!xGdfhS05yC?Kp|+PsHX(+z>a#J162@@g4%e%;O<V`;XS*CQguU0$M77as0`bJDoQ>'
            '8=E)d{XlDeK;nr8zNbA*z^;zRjU`jlkYK45_B_`PNqiAE@1FwYwBjzt_Hzh_;M(u$AjP+-^9)ar<;y@PDDZu8tK|?Mh>w;mzJAx}'
            'JP7p*dlg^rT7|b02kMq6I*8ruJ3-%9pl%%G3vmDqczIsqA9nrN5vy41PunJZIudu#Uh&y6wsFy0@j12#+#>k*3xYYd_!sw;WS7AP'
            '000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response(_dsdl_.CompositeObject):
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
                     error_variance: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None,
                     time_system:    _ty_.Optional[uavcan.time.TimeSystem_0_1] = None,
                     tai_info:       _ty_.Optional[uavcan.time.TAIInfo_0_1] = None) -> None:
            """
            uavcan.time.GetSynchronizationMasterInfo.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error_variance: saturated float32 error_variance
            :param time_system:    uavcan.time.TimeSystem.0.1 time_system
            :param tai_info:       uavcan.time.TAIInfo.0.1 tai_info
            """
            self._error_variance: float
            self._time_system:    uavcan.time.TimeSystem_0_1
            self._tai_info:       uavcan.time.TAIInfo_0_1

            self.error_variance = error_variance if error_variance is not None else 0.0

            if time_system is None:
                self.time_system = uavcan.time.TimeSystem_0_1()
            elif isinstance(time_system, uavcan.time.TimeSystem_0_1):
                self.time_system = time_system
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 '
                                 f'got {type(time_system).__name__}')

            if tai_info is None:
                self.tai_info = uavcan.time.TAIInfo_0_1()
            elif isinstance(tai_info, uavcan.time.TAIInfo_0_1):
                self.tai_info = tai_info
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 '
                                 f'got {type(tai_info).__name__}')

        @property
        def error_variance(self) -> float:
            """
            saturated float32 error_variance
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error_variance

        @error_variance.setter
        def error_variance(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
            """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
            x = float(x)
            in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
            if in_range or not _np_.isfinite(x):
                self._error_variance = x
            else:
                raise ValueError(f'error_variance: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

        @property
        def time_system(self) -> uavcan.time.TimeSystem_0_1:
            """
            uavcan.time.TimeSystem.0.1 time_system
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._time_system

        @time_system.setter
        def time_system(self, x: uavcan.time.TimeSystem_0_1) -> None:
            if isinstance(x, uavcan.time.TimeSystem_0_1):
                self._time_system = x
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 got {type(x).__name__}')

        @property
        def tai_info(self) -> uavcan.time.TAIInfo_0_1:
            """
            uavcan.time.TAIInfo.0.1 tai_info
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._tai_info

        @tai_info.setter
        def tai_info(self, x: uavcan.time.TAIInfo_0_1) -> None:
            if isinstance(x, uavcan.time.TAIInfo_0_1):
                self._tai_info = x
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: GetSynchronizationMasterInfo_0_1.Response._SerializerTypeVar_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            if _np_.isfinite(self.error_variance):
                if self.error_variance > 340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
                elif self.error_variance < -340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
                else:
                    _ser_.add_aligned_f32(self.error_variance)
            else:
                _ser_.add_aligned_f32(self.error_variance)
            _ser_.pad_to_alignment(8)
            self.time_system._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.tai_info._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: GetSynchronizationMasterInfo_0_1.Response._DeserializerTypeVar_) -> GetSynchronizationMasterInfo_0_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "error_variance"
            _f0_ = _des_.fetch_aligned_f32()
            # Temporary _f1_ holds the value of "time_system"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.time.TimeSystem_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "tai_info"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.time.TAIInfo_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = GetSynchronizationMasterInfo_0_1.Response(
                error_variance=_f0_,
                time_system=_f1_,
                tai_info=_f2_)
            _des_.pad_to_alignment(8)
            assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error_variance=%s' % self.error_variance,
                'time_system=%s' % self.time_system,
                'tai_info=%s' % self.tai_info,
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 192

        _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
            'ABzY8XQGW^0{^vGTW=&s74{~Z#OX~!qD_{~1EdIuY?SeMW_%kj;^KJMtHJB>%JwD^Xld1S*SIR~>1wK~Jv&jj1c_u<G$B$N9uN<_'
            '@xVJ0F9=?ELE>-lGvJ)6o|zi2y-N@o`O<T$>eQ)o`Oa7U)APUn_vJbJDPGA&v5u2^sF@Np5%1An!s=lp2bt8uu(Eje8cW0g9^->i'
            '#>!92*FPwKR9-2b3`LqURr0yw*?pt($mEL6PI)3s=>SwTb9x-nv~I+J)o(DfKT0F6WD2_(A=4eI4O5-8FY9|uXEN2WW<ES-O2a5_'
            '@YGw?^QYzZ-1fN-%MZ%pLP(8KqL&+{%R8{!8AqASDvKw!1WV$neL)ygLqmf`pS3(wczAIPGoIc`BsH@~yb$(;2@{qc8eVP_P#M8#'
            '!hwug$zLum-5M{)W%W%M+rc3`$Ir{XvUoAnhNdx9v9IVJ=o!$%RG2)*jr)p5=qU|;*{YsFNAcRya--F5EiJFEF11%$?e@xgyV+c8'
            'EH~Rr%kAZr=IVNDWqG+#;$C@=2gP$tDXGF^3TI3s(0x9PWmLYi{Mg*w_ce=T8vmemC%BHY$aq$bh?I;6Yee>m;f!E3VM>xSqF5#s'
            'WC-bvU`S{(upzAn2l&O!fd`r-atO1GBoU|SAtQaoSTZ6*E)r&yx`jAd<!LI?!+Nj<maw~YkR@nH-<$TDCUTgPD3Q?-F42>`f=!0P'
            'a6-wA?*4wwu3<B0!ujlO#v<bk5^1Cu)hwW(M;xX!fm1~+LsyfS!EQn-3b|G%9cM!|3-lyXo0>cL<gC8#LnVg<45qP2M$Q;i1&$1G'
            '2<#lnJOS@9*ePRa%u+*OTb%gA9CFc&W}JS+SO%^k9MWb;6(jVRiUji&Oo_nDBXXrj<LUSa^Iivi=Ulhv>vgh=ewaOqVuw_uES@=z'
            'vo2OLBRvYPh9jkNAYe%yv+5;R3;Z&Fs(K2FOMb~8z@PmQ>^&&?GyJ)63G)}AY`xVl7Z-1*XbOuvsbPmq&D0wI^7eWD3jfOXIm~AM'
            'wfi=qpRgvDe4&^_TP_y!n@}fEQ)asGGQT>b;;ZAuFYfGicMo>Eoy~B+)7`utzPY=5fV$X@Or?QLik!!_Kv(soH1*)b5azXeQmoGu'
            'b3Ubp#FFXsH8W0i7jXrtdjw%(G}HAGK-8IEd})k6kT;5H1iKmRncuTeNt5xZc!ysp&bi9gJvhyqk2>t*2OAwY+dF?hH#dj=RcWP?'
            'Y#4}UL@-R>Al#TtUtL^eX?-Y;M8;x4>rx#q;<v?_g`ry*;zF!-m!9DKK~`lBK!$;Q(l*P|e9(jRgG`1+N;*J+N=d*MP$<sF&Gog$'
            'LZb;k2aU#6`|~{lmV^F{jsuY)9ih+r;x4QbE>k?^W4)9^!J**Bt$k})J#a~=U3_xQCPRdx#%TaGw<!;bpbHr{AF>`z0EnY;jOB-C'
            'az@0WU#+YM6O~{qBnr`aR)J$5qK_B@`H5zMaxK7~Gy;w24?WRii0!`MWZXwrRzsg4G|LhZS^q=+KoZ>avZ47Ivf;&zTeog@Ha8AB'
            'yWMdA*7eQKR%a7ae{EyB#exP96a7gQSVPeEJUvPgdNaTTaFAdR81q<jWnv90E_%&6?2Q~RK&!sZ*Z2*-$=~98obo$4G*o~<KwhYp'
            'xV&FH7g`U8=)zFMWw&@C)G}8QgMoyF8HILPh(#_3Y!M==7QxF5Fl5mI&~bA?r2Qnn8}}B53RsL<%<>+bF9f8^6WnD=0(7-#5l_1~'
            'MXh?H-mJT!5{|;DhJ7(i$Q6zSw9)(ExL+Q4K4OrMOj##RD`PyUIbbxRy~SQ|g-s2VxxS{c-`a{{W+>HBJ?H?8&=k`NRyjb4y{=i!'
            '^V=qN_Fe*n;p<~$neq!T+noGf7SFsX%uV}!pH0BCcs!I@S&*}o=+U4j!JXij9X5~^qub5!>{9t`F#>Djk`Ie7+;a8vz$E@Yj&}1T'
            'p=xw;ly`nrUfDkXiS7Y4%$$aDdp_^MIiVH7BR<f(`0y0+F9<H$A0VRA)UwBJ-m}FK6c;cYp{{z;LUG5BU6d;fE_6`{1EPdwHEcp^'
            'HvhXwNP7Ysi!++!#hE6#(LoCQ&<;7R<-o7y%TxRb0dCPBxejv^A>9A#{M;NSV09`FtKbA?$XIG&4Z-F1!KP(cwze(Lsp`B2plSi|'
            'J*H$m@M+zEj>a7hfFH_xqSYY;>K&uSLug(taLfns4w#QH0CzoMnGb9$d)P&YlD%9Tx3LE9D51{o+J2M}2MYR3<IE816fl0osH!2n'
            'YSEivo>lOtCOxVZ-h>_=x@H5NMU1(WlE&5m!sK<TfZTz~7^q}YrNa!hLJMUIhCnts%s*yza!uOSfw?DhqeaY|DmdMiZ6Z|!YlOoC'
            'ZeV*6R1Qg?rQp^8p;E<=n-JUu2&^A>=fE2N7tm77lv%<;L`ksnY7h|kTtn7^pZ8BwRNWZv;M9f5=lz9;eXQE=(iA&=3)D6nPLd}R'
            'Nz<RRgp!soSw_i{FIhp!vM*Uh$%-#oL&>TyX`^J#m#m|t?Md1Vl&pIewwoYn`8K!F=2p{}pv|q8FF^}izRhjiz2)1yj(fFyo7e4L'
            'tDc^9yVsg8v3s?B3HqnC?(0EsEcrICqc@g(Kd<B2m!^JhH5zu+k}t7ymM3~zjV9W&wBk$fq)V&bs;1p*EeJL&?P)byjarqj_{v~>'
            'vq4H+aW@MZww8b!+FBZ83g#aUB4Q~vu+%b#OjL*u7H3Z*KJyMN?>Vr%*4f&+zIPqzKBx(II^Em*A+R>=1Am@m^ua0Q&btRg^_)b{'
            '3C)D^Wsdt**u##oZT!E<r_es{e1LwfKb#ECG!SyCPr%vX?e2DW_w6qDhJWV-+nnA#80V<;xBNH!_xyMKkNgigfA>B=>hh%Me=gL_'
            '^-7<Y@f0}NJLzNC?9el?kl2NQy?waRYRk9rUg(H4fc*3Yh9;RyA?sObbMMS6QVp1zmgDxO-Q{GTvH$(%WRq>2>za#fl3Ny-xnkHT'
            '-Ua0MSfmET#l35oN40VPMj>93pgl@_+oCOwW9od<=Gz-k>f;oi4B)yq$W1%in2ZK*+vf7>&HY!$9cIiSrk5?RYW3C6(lCSD8*goH'
            'bZ0I!<IJ}WQQ?ar>B?)!S&BsjWpbFv9>l|^(|FNh40_${<x3kS(?d`a3mpMFpogE&9W3M8RmCwMO^ED|Cr>}~=xYG<m4Aq=m4CGT'
            'JiiCO_hIZ8Q(`)g{7qOMxKN}Uk;(DB418AuhlI2TjKDet?q0_te&D5>WpI;AXT1V4eE;Ka6@GCLd^sdDmy-yeRVCN>C0_7F{ulo7'
            'w32`Fc~tUBv+?jZ!ZRg)&%)3n96s`H6EAJb6t9x$sn?R?X?H7uXyY5?M`-(p+w`Aj&GZ9J{6G^3G?@gNzsEF6uYmN*R63q~Li{H;'
            'xee0xgOg{)E`|67xIsMcZVs0qh95s9ru=V}PvOdhOgc5?&fJs5CAfpTcm68GmniVhz9aYA2Z8qSE!R>{4TtZn2OQ%^=!<*UBKLs&'
            '8*$dv@yK25{(8d6^Pkugf7Ipoz-n~E_B_hxKGD`6)^#{YP8r0d_5T1`p>mZ982|t'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.time.GetSynchronizationMasterInfo.0.1()'


    _FIXED_PORT_ID_ = 510
    _MODEL_: _pydsdl_.ServiceType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^vHO>7&-6{Zs>R+xVzaf7yrw?R=W4MmaEk4Xmss>qhh$f68OPJ$NBV#yt9#$N7hc6KE*iID_F3LDs<X|g%=P@q5$'
        'z4g#rFGWv5jy)7T^wvYsYmYq@{oc&(a;YE3ZW}_PcIW5KdvD(R-Z!HUj(`5{a~1tbP6cCExnA8?EEJ9>-f{XKtJ?!P3ZxPdOOuDU'
        'Shy<&Y<nEA^t1HE57V3JZ1SibvbSTVB0HjXUP&H3$2>8@6nA>$gSPN}7V05eQ5X-RINT@f0o!**SgH{_y939sM`Fb47g)44_6Iza'
        'KD3I2^fw$8v9Rk8W&N^QJWXcoT^1^IlKc~|XV0Id>y`CmKTSV``nD5Aq3FjEQ|Z+-d8+ho_s3@Cn>5a4LC6LU3`lP$kJ&?UgSmDf'
        '!^jqH+Do3am5jpyLx;!gz=?R8yg$$7h|R}v-uzI8Ozimc#)jSIobZQUe8cU}?S=44I3L7)PYmF<o!FyQY}bh#?LL)FnkU2Omzs?`'
        '8{eom>t+I(!yN@}Lgq)bhqP1at>n1v%0c?(v-edh=i#8S<x7`Y5qBcX8AQr*@MF<xmYQD18tHXvmJBVStbr3yKv;4}^Mt=cGgUm`'
        'wW{JW_FTLK<Ri$&@JxYvwTm@m{~E)bT}FZ;X$7I&70?2Hk>SX!=JaJ8S$kXzc&-kXAL*szkc{%i7ToJ%7M5U^&!RmUUawcHoBn`J'
        'j3{PtshD50L<HS^Uq)7+q0#YoAOpI4(%1k;cnqdm(r3mwa%usR6~?{~lVOc-N%VyldR$f0<I3wETnQF=Y`;7iu+WLL#1-EXqX6Mx'
        '+yM7#|B<6;j|9E55cc6WWNz%cjvw7=!;DsA%kex*aeP<dHLZX`fKO@bcze!R)l&pX-&1Mwy&MAiBC<W^??fDt6zzXclSf_^(MA2f'
        'h1V>5llyHMq=|Ku5H%k4B@9KVZm^NewBFRNkYO1n2Jo4i^4a9^OOETpO$P??IqL1jp67(){k@Q|>v%Csf0oX!S3XgFU_)R8rRy_s'
        'ALfpP4`84N=LS8Tut(BGGScj-&29vaui>K?_f<dc^T+uU{7L={KY2Cf&)!V=H*fQA_4v2>bNu;R{1mq!fZd1?r0K>7$C8sk5QBiB'
        '&6(rkkH*HMFg6HjF!BSgxq^jveCBrji0!a&8Xg}mIW=9kpy~j7PPzklUrkP4$_3H1`YQT1s0$!??4$H@nmlc*$Uy{!ZduSR82BCj'
        'UA+cB&A(rA@iVK^Cm{3>-K*pwvsK7W0O~AXFd~-8?-u+%CF&cODIqSifJNe{jlXX8qk#!!Su>yLP3ZLaS-6+Kd=uN4?Ja)=Tf|h>'
        '`Kv=ZX(~WGWGaxpVp)|sk!e=tk7Q4eC(U~(I!0KU2gU4BTU(TvG<jf6FobnsZgm3tw0RG$dD4ld_M2Z=xA+hFYwH!-J-%@Zb4JdN'
        'FQOQ`nmjZN35uZzs^41njLFIAg~djz-C9^&US4P~wc72aPP^GW(^zb_7Z%%#OU>m@YiV(@k&;-7?&L8RhB8FjKzE>N%1^zyh>G!J'
        '#Rk%M-)dd0o~Hp;KA=V@oOjj?YGv4>Qx8x@wE+0n9~(e3;8d?}(~B8{2f&lu!zdI51DMt@WDH0@flV`U3We983A^C{Hc63TY1nCC'
        '>z;27JUP%nJAp`oVi9rFi3`20ErZ-_$|f3*%txg%3JHG@qA;*36*}ak<H4!{3pCcc466x=2xh8ob&U?$C_%+VMKxo1VQX3TPAK;*'
        'DD1ex8yjUv6dYNlF6g<ZYbpu}$O!XYKucbi-i{Go(Rj+~*BJ|_CUd0r9+e7b*AbpB*l-2BJho>0jyvfeQ!J|L&^Xtu`C{GDrF7a9'
        'uoOoCkfzKr+PR?&tiA(R!z5n<R2{EQ0TpKP8<(={WI4OG@wKIk5T(#lIY-l}RGNLR$b;j^gNuCQwvN^Z47~GGNrhGmk{Q4hAzL&_'
        'o&A&F%_l#-vDw?)-t2W(?X7Na^}PM+=H@oZVjB{*8?iFTiliWC^rejI)qP!}AWb0~qB<L|p<KI?DgSho2eaAJ5W#t!5z7crZ25BX'
        'T#gk83E&b{nyDf%b6Eq9<K^b?W&VD0%;c+v!mqUQ{_T}6W$_osDitavp`VGgRw8WFz@i;^+2T<YsI&9)%&+f>>mp#TaOyJLnWwk;'
        'sfo6kXwyVWV-tDs`Y6bP0%#B+RFq*m@u-i;LXcuoC=FI12|PFfIbfXI?3`)LHJbR@ZZyv7pC4J!9P(GX1|Nu_z}cFEBPDfFED6u$'
        'I#g$=;liaYtysNk;w$4(#DVfI!+9q=m+@B!0zr<<cmy=50Q54%LEB`MaK$j2S+5o%p(_!;j00m7n5{+dfxslSAY2LP;}0N_{Gkdt'
        'k);n<a5Al<GObajEhi|5p$;7W%ThEn?;#qVUb%GXVs~|AySv%5w=SJu?XGoKDdx|tOqQ5az$Y;*!ryR2=pOsmeL_{xcGT=humj56'
        '*IX*JVMLH-`Oo>s{1^Ol{u};l{yYBLIHydB_&QEX6Fe!OiTLxkVdKZ!C36@;M{{qaToJ^1r>4t<xdmIMU8J^*S|2!jbfdea{CV+8'
        '52sr5#Z#I1948XhCeF$`>ofc;e!*`FT7#W^nDn<*2BoKxt7T&+2Pf!F8K8?XD{ArTy`EN%!uF@8uzjUVB<U`Jy;_dbXD7L314@Xd'
        '$I6bQ0YTY6j#nzQW0_T@JcI?&9%H^vSxTHM+pC%w=(yG8Ig8;M07EDDJ1mqqI+obT$QkFb4NyZ_FQl62C%Jhh+<~3cs-|F5E~8)z'
        'I%4;QF4$OB_6Z@aQ1)Y-IQ7B`lt&^kZ)mK=nN8m<s3Vn&_Jls}j+ukQIiN#{{uE)F9Dy^Hz6$0qqA=M8NP(InrvRahiZkhXCj=*f'
        'NEZyq%fexb5s-$`ha!k3gJ-*}Zk>}F7Af{{yjOJS*P>wEng+;h2Wyr-<O)+ehB((*o}e@NkT@64+K5eT?i@C@yzj<=HTo-DI>{G='
        '2oniHpyk<W)xzf-m16q5cbK4z=w79vbH(SqxjTKd*w-ANs#ptRn+?+vdqqpLJZ6DfTIH5SYFQ|^EK$p1xn-GJmdY(>sAaj_(x#R('
        '<(3Y$v`a1R2DNlb8n&BgX_a+ulg_PXxrKCYwaP7|VXLfjn^td?b?(qwt+LJ?z1DI`PDihGrre^}YL{EcKdnw#4tZmttaFFFu~7DN'
        'hiqS%__@_+=vfQp7CmOMkke{3NuPzKatm3yuw0te)N7roR#$XMZ#7ztS{AQ#lbI88;&~Y_(V(Go3A{(=QjRGUf7D5c6|#}0O)(-d'
        'Bz({~dstDQF<^PifaSUF+S>Wc=ZV8YjJ?tAUD>k1NT?3{zKH1ULx@Z1_=fD+kDdjELi#epYclL%yHqy*-^5C&GN(E~Ejo85I#UJ2'
        'I@Bj{wtc0y-rIbm2jB2d_c5u)e(v&T{wMxd{ulmt{<jHl8GbFi#nj3Jq~%TjJ}P$P8BDbFL}2d_2Qj6&Bpr4PNd(AG&fUriObBVu'
        'N*#Mg(*GK$jgonJQ-*kNG4|h|3UsjLv97oXirCV?%yG6yp|}R*FVQXq#HF=s6i2nZep92+*V98umjp`VIEBtDI^JGFs^=kGbkMw)'
        'tc$w0QS?^d(8cA2i(4<`6(;8plY>MlYt`9%DVWtOE3dDv^rpyq9{IW;hIF4HO?vHd=2H?OO?Eul$A0X)we}f9t(!hrs3?^F4urTu'
        '4ZseZov-J7aSz0_S|+AXfS5k9pP0@Ne-oMqo=W_cK@`(<!hs8aa!U5^fc<wxn!yzZs(J=wbZud1csV)r^|%a7OcH!%nfw#3_!s;m'
        '{xAMzy#Lbn)2}jk(za!Wy-p<de;aw=iZpkk1t(gC6Zs$Xo#y&1T4yJ%`QUxc|1^W!Xl)-HJl&jKXZyv?B|P*I|MIT<^@EMdgM6ig'
        'y_UI^Ir0Lz?2S8I4!@N>IqQGC!_6<&KKka@dhqa@Uqs^U-CpZXZgWc~l^IAlk^P5L7mukU&^3zmu(%D@-Nu#I+Q%xDYs>WYGJSRM'
        'Wn8-P?_<WPx9L9zalif_L-?Pth8+L^'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
