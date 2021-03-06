# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/metatransport/can/Manifestation.0.1.uavcan
#
# Generated at:  2021-11-11 23:08:22.783027 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.Manifestation
# Version:       0.1
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import warnings as _warnings_
import uavcan.metatransport.can


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Manifestation_0_1(_dsdl_.CompositeObject):
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
    def __init__(self, *,
                 error:                       _ty_.Optional[uavcan.metatransport.can.Error_0_1] = None,
                 data_fd:                     _ty_.Optional[uavcan.metatransport.can.DataFD_0_1] = None,
                 data_classic:                _ty_.Optional[uavcan.metatransport.can.DataClassic_0_1] = None,
                 remote_transmission_request: _ty_.Optional[uavcan.metatransport.can.RTR_0_1] = None) -> None:
        """
        uavcan.metatransport.can.Manifestation.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param error:                       uavcan.metatransport.can.Error.0.1 error
        :param data_fd:                     uavcan.metatransport.can.DataFD.0.1 data_fd
        :param data_classic:                uavcan.metatransport.can.DataClassic.0.1 data_classic
        :param remote_transmission_request: uavcan.metatransport.can.RTR.0.1 remote_transmission_request
        """
        _warnings_.warn('Data type uavcan.metatransport.can.Manifestation.0.1 is deprecated', DeprecationWarning)

        self._error:                       _ty_.Optional[uavcan.metatransport.can.Error_0_1] = None
        self._data_fd:                     _ty_.Optional[uavcan.metatransport.can.DataFD_0_1] = None
        self._data_classic:                _ty_.Optional[uavcan.metatransport.can.DataClassic_0_1] = None
        self._remote_transmission_request: _ty_.Optional[uavcan.metatransport.can.RTR_0_1] = None
        _init_cnt_: int = 0

        if error is not None:
            _init_cnt_ += 1
            self.error = error

        if data_fd is not None:
            _init_cnt_ += 1
            self.data_fd = data_fd

        if data_classic is not None:
            _init_cnt_ += 1
            self.data_classic = data_classic

        if remote_transmission_request is not None:
            _init_cnt_ += 1
            self.remote_transmission_request = remote_transmission_request

        if _init_cnt_ == 0:
            self.error = uavcan.metatransport.can.Error_0_1()  # Default initialization
        elif _init_cnt_ == 1:
            pass  # A value is already assigned, nothing to do
        else:
            raise ValueError(f'Union cannot hold values of more than one field')

    @property
    def error(self) -> _ty_.Optional[uavcan.metatransport.can.Error_0_1]:
        """
        uavcan.metatransport.can.Error.0.1 error
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error

    @error.setter
    def error(self, x: uavcan.metatransport.can.Error_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.Error_0_1):
            self._error = x
        else:
            raise ValueError(f'error: expected uavcan.metatransport.can.Error_0_1 got {type(x).__name__}')
        self._data_fd = None
        self._data_classic = None
        self._remote_transmission_request = None

    @property
    def data_fd(self) -> _ty_.Optional[uavcan.metatransport.can.DataFD_0_1]:
        """
        uavcan.metatransport.can.DataFD.0.1 data_fd
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data_fd

    @data_fd.setter
    def data_fd(self, x: uavcan.metatransport.can.DataFD_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.DataFD_0_1):
            self._data_fd = x
        else:
            raise ValueError(f'data_fd: expected uavcan.metatransport.can.DataFD_0_1 got {type(x).__name__}')
        self._error = None
        self._data_classic = None
        self._remote_transmission_request = None

    @property
    def data_classic(self) -> _ty_.Optional[uavcan.metatransport.can.DataClassic_0_1]:
        """
        uavcan.metatransport.can.DataClassic.0.1 data_classic
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data_classic

    @data_classic.setter
    def data_classic(self, x: uavcan.metatransport.can.DataClassic_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.DataClassic_0_1):
            self._data_classic = x
        else:
            raise ValueError(f'data_classic: expected uavcan.metatransport.can.DataClassic_0_1 got {type(x).__name__}')
        self._error = None
        self._data_fd = None
        self._remote_transmission_request = None

    @property
    def remote_transmission_request(self) -> _ty_.Optional[uavcan.metatransport.can.RTR_0_1]:
        """
        uavcan.metatransport.can.RTR.0.1 remote_transmission_request
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._remote_transmission_request

    @remote_transmission_request.setter
    def remote_transmission_request(self, x: uavcan.metatransport.can.RTR_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.RTR_0_1):
            self._remote_transmission_request = x
        else:
            raise ValueError(f'remote_transmission_request: expected uavcan.metatransport.can.RTR_0_1 got {type(x).__name__}')
        self._error = None
        self._data_fd = None
        self._data_classic = None

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Manifestation_0_1._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if self.error is not None:  # Union tag 0
            _ser_.add_aligned_u8(0)
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.data_fd is not None:  # Union tag 1
            _ser_.add_aligned_u8(1)
            _ser_.pad_to_alignment(8)
            self.data_fd._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.data_classic is not None:  # Union tag 2
            _ser_.add_aligned_u8(2)
            _ser_.pad_to_alignment(8)
            self.data_classic._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.remote_transmission_request is not None:  # Union tag 3
            _ser_.add_aligned_u8(3)
            _ser_.pad_to_alignment(8)
            self.remote_transmission_request._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        else:
            raise RuntimeError('Malformed union uavcan.metatransport.can.Manifestation.0.1')
        _ser_.pad_to_alignment(8)
        assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 568, \
            'Bad serialization of uavcan.metatransport.can.Manifestation.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Manifestation_0_1._DeserializerTypeVar_) -> Manifestation_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _des_.pad_to_alignment(8)
            _uni0_ = uavcan.metatransport.can.Error_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Manifestation_0_1(error=_uni0_)
        elif _tag0_ == 1:
            _des_.pad_to_alignment(8)
            _uni1_ = uavcan.metatransport.can.DataFD_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Manifestation_0_1(data_fd=_uni1_)
        elif _tag0_ == 2:
            _des_.pad_to_alignment(8)
            _uni2_ = uavcan.metatransport.can.DataClassic_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Manifestation_0_1(data_classic=_uni2_)
        elif _tag0_ == 3:
            _des_.pad_to_alignment(8)
            _uni3_ = uavcan.metatransport.can.RTR_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Manifestation_0_1(remote_transmission_request=_uni3_)
        else:
            raise _des_.FormatError(f'uavcan.metatransport.can.Manifestation.0.1: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 568, \
            'Bad deserialization of uavcan.metatransport.can.Manifestation.0.1'
        assert isinstance(self, Manifestation_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.error is not None:
            _o_0_ = 'error=%s' % self.error
        if self.data_fd is not None:
            _o_0_ = 'data_fd=%s' % self.data_fd
        if self.data_classic is not None:
            _o_0_ = 'data_classic=%s' % self.data_classic
        if self.remote_transmission_request is not None:
            _o_0_ = 'remote_transmission_request=%s' % self.remote_transmission_request
        return f'uavcan.metatransport.can.Manifestation.0.1({_o_0_})'

    _EXTENT_BYTES_ = 71

    _MODEL_: _pydsdl_.UnionType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{`t@S!^6fdY<7qROz5Di?-ZSTh`IKD9V;C%BOs+L!~la!x#9n7!Ns3_DskjcMh3Muz>xr3p$u!nRpi9OAsRo0%EZU'
        '{ICi5kOw~m0f8Wh^F|;qMt}f(+($m9{_d}Ox_i3j;tVa>ZNRE#{dIg@-TzTvRo8qr@S6|+IcEP?IlsJ`DP|VNQ$@3oO)q5sEIqSe'
        'j;Cgq7MGWb*^*hUjC_>OF6BR5T{f#<R<C|u{YBNN45sqwMIpOfPCuMY=f@Y#Qo2+~=Znirh0-|XB-8oqoLLmvqH?v8NIf(QMY^<N'
        'mEn(Z{biNMc>Gt@&#M)dN|#E7>`b|27OOuKT_}LLrK**|ce3U}rUvRzDw8gyQzb$wdO7kzsZgFRl?$d1yERxjr$qgeLSd;;wT7(`'
        '3CueDv#NEpa`?S;CX>z2`@6JGR-Oun`EV(l5qJHuNW8s^+nmXkQVV8&zGPLoUYrqdV%5q(Dzh|OwJw)u(v_2*kx0#~IwNgY&6vvt'
        'b2eQvGu1CDM^kgz6*H3}>?zUNyOraq;!?RVYYM@FnOaVZ9x6Y-Wi2h5x5@(Dt+}OwnVrwya_;`&?VH*B+(LOJGjsFPf_Tz}Tg&B{'
        'h3ssqV9u8psF&J!7E$SzZ^&*@jy+`K6XUnXog!6n16H~y`Y)LI5)I44?5tV+!n#uV=&d*2)o02@-K08t!K6lB(#>qiG7EY-uV?cm'
        'QAfNP>4k+=ecsHQ1;T;ya|JOHy0}Q|nQT!!*qL;G)*PqNn^`D|mr*{7+7OHGOToXZmBVjlOMhbj{ek#XKAQg2(sH$;s~Rb;F3v28'
        ';Su+jG#8h|gC?LqT_%X)opIm7q13FE74L|3w{i?GO<f`D6_UPNURX#MR)bQ}!o&1J*{uG$YH)qMI3tv2*=eZC6Xh9kyNlVpczNg|'
        'y+Rkmsl}y?cxKc#k5j$aI`2c;PifyeAHd&(_<IQHFr@?QJOTL#rGxAI5af)~L+ku7rHOTZgwmmPeiZeNq1-6yAE)%#IzK__(RF^3'
        '(j)8q6s3pP`DseoI)4J~o}qMPosXgYCn+6X=TD)Zv%vE-`qL=wU+3r0?|Dk&>s&|w&p6}8FCcvu=|!ZMkX}Z51*w7bD$;96uOq#I'
        '^d{1Aq_>bxAia(BIi$}cy@T`xq%R`9i*yp{J)|!oeHrO1NMA+z8q(L1-bXrxbQ-CJbOq@e(ha1WNVkw~Bi%u|i*(OPlZiMk#^i+|'
        'FDB*1l)RXh7nZzOkr!+7VnbeR%8M;|u`Mrl<i)PM*uzCx*nM+lS(qg9D9D>B&Xmct4w{ZZzf!qOw#Ts}hR4j1Iq?{it5s2LR2p~d'
        'wCgg?D_zFh!bZOHcAd{KJk9jE&8Yq58wFu-3bsvo(73f4sB6mB-b@$GmRnT0+T}uaF<Z($6t4E<M`C#A^JeCO7`l10;P<GPI1>+H'
        'HeD={9TLv>-z!hNCo5CY@wbF5Nh0C#<G-xFU#*-<iP#{YNf$C+kNAc2)ExU~T_J~PY3`k0u&+dSr^#<xmz@HpWr)oGw*IYXUHihi'
        '{;qYS@{68(y}AMRdO&NOyxoc0w{MC9dNxBZ+g#Qxj90A*>v`uUUbODHzTh?Y>Ym3xoPKL5PtHCc>S!t>j-L@umcpgb*4}iw`iWz3'
        '#hCpOkBb4F;>>y={{Q1TZxIi8i+*^EIK0JRz+3dgTlB$O#NjPs@D>c-g27ubcnbz^!Qd?zyaj`|VDJ_!;4K)u1%tO>@D>c-g27ub'
        'cnbz^!Qd?zyaj`|VDJ_U-h#nfFn9|FZ^7U#7`z38w_xxV4BmplTQGPF25-UOEf~B7gSTMt77X5k!CNqR3kGk&;4K)u1%tO>@D>c-'
        'g27ubcnbz^!Qd?zyaj`|VDJ_U-h#nfFn9|FZ^7U#7`z38w_xxV4BmplTQGPFCcOod-hxSQ!KAlf(pxa;EtvEcOnM6@y#<rrf=O?|'
        'q_<$wTQKP@nDiD*dJDE*wr~SN54`GeTBwIvB;C-3Zs;Mp5k*o_B=rN2q^wODJ_%2eC`Z~5X+xw9waLW5j0pN<R2mkKkE?m56%of}'
        '%uMT1{<a%iYu0~Q|7CsKVrbl77aHfr`eL!%De+G&K>ob<v{2X`hXl#b-P=cy{J&1I|7#@x*1Q3*Cd``FLI50xSsMrhz;T$h!9V~!'
        '0<$&@vo;8`)(^85hgmxcvvve#?QkFfJ_NHi0<)HYSsR8~8-iIIgjpMaS?h;c>w{T~!>q+%)-;$k4Q5S)S<_(FG?+CFW=(@x(_q##'
        'm^BS%O@mp}VAeF4H4SD>gIUvH)-;$k4Q5S)S<_(FG?+CFW=(@x(_q##m^BS%O@mp}VAeF4H4SD>gIUvH)-;$k4Q5S)S<_(FG?+CF'
        'W=(@x(_q##m^BS%O@mp}VAeF4H4SD>lV(kmW=)f3O_OF#lV(kmW=)f3O_OF#lV(kmW=)f3O_OF#lV(kmW=)f3O_OF#lV(i|2EhGM'
        '035me$mK@?aHI{9HYft%go&W8>IpB69223X^{=^~_KPs{u(&R}VdiSj!^|e(<<rFaJL`t&T1kD5R&mFxm1C(=dOl_Ug=OPf*qv~~'
        '?lp1e9mS(w=bE6{)64B1vDegtoUT*xe{vVZAV$78vObaZv8|7z3WiVxqk$^K1F8^%Dhxms1_P=v09A+urfdUHg*a5<FjV0XR3QOX'
        '7=kJcKo$C+3Nfg{NvOgJsKRlm!YEYX7*ydXRN)9z;c#Hh;t*6}1gemLDhxvvhM)?AP=x`gLO)cY52_G{D#V})22{a-Di}}&1FB#^'
        '6%43?0aY-d3I<fcfGQYJ1p}&JKotzAf&o=9pb7?5!GJ0lPz3|3U_ccNsDc4iFrW$sRKb8M7*GWRs$f7B45)$uRWP6m22{a-Di}}&'
        'L#l!yRl$&|U`SOkq$(Iv6%45ghExSZs)8X^!H}w8NL4VTDi~4~45<o+R0Tt-g5eEIBW;MZ;YY6x2uqK8LOa?C7i4HFXBArs3x)J*'
        'wQ}a;w8#}X&X%w@DA&K+@kq*CFc)bzTUe0zpFBo88thP!R^`*n>Dg>)waV{TPRJc(orRb!hm&XCPv_^&_swOqlvV9Y`%`DL*!=)4'
        'N^RK|C1yQH#`+qVlo*fK#hZ2>?|1ppnD|SY7+1yzNiBWm#wX*$q{fHb`XVPGHxdNP@ewy>jfuacc?vDZ8JUlxzIH{fG-1j*{D{lX'
        '##{r}urxnLhU`RLPeL*ZgV?k_KTgKcF`A-OLP$noJX@;EPx4bRvUM1Q^b`zl%Wd(~{0SIo8fj^$+p5pc@G%(nP)wr47z}>f?eZu2'
        'Q*aXQcnRs4WV}0RkDujF!_g@5ic(L*33c2D*Z4U(v!Ssi)X(g@MSk9$AH}%d2tW1yY*+f@&+rRywbZBQInXFw>RKQCS$+{NJl6Qm'
        'MEMI;_DWa#=9l<o88V1mJhQ7^?}J})Ly?y5Q`C?lOV@GmtNa?mAm`a$6m1&b=X<kf{qpPl212fu$3fJ(f$*$nnD|XTj?m9}4-Dr`'
        'xZU$!`7J(yAhWFz5j7_el=d7Szs;XR;Ol>5Ziu!g<XiK?fnnj#^E(K<+a5Df`woKj1H;N+;4flgP<y*3=>58P;5hhQK8Z<5M`I^i'
        'n8ak}z;W|?{3T4F!r#L?qK`>>7hnC}@bQ=VE11-EJielpS1=*`-tK|F%3s4|)c4NP)1Q*L_x<_P{`@Ih@}48JYO+s)Qa+7otzT}T'
        '#Ih{2<}LGCcqzVuDRIm$u_mM<+!b{UQEF1uoDyZHMSV-uSi!W}Uv@*3{z_GTOI?0b)c88A&UW)UTcXxC!FoHb*V`5~zxCGLZNKi0'
        'sQsO+zt?&FUD3iHL>r(OL?g*qyzO@Oye*9dS`tlDW69BYXYCmc+Y{YUlSw_^UaOOBv??G_!^w$wYi&<;+_r#4%_r~28}~5Xr5*%S'
        '>LmGIJiH&PC;bTcPFKlK;@;j?4x~46Q`BK{IZl19dHPI#)}wC4oz?fe5!$l=gwB)ez3qRq<^Ba!KuCVoZ4_JkLLqJfK$2hYAIo;v'
        'v54CPoa8s1Alf+)MB>H)D*0_|xOTrcTw+MP(30PUpxb-&(1{TPz~mnYBPetiV=~tFh`<!1=SPag--PubnRuMY=>(CIJtn6U?zW5{'
        'GdWFETr47|dqPgzW7~CdT5mSt?EyKh`=7%PmYmjW3kp9Pa+>b>qWyFua$1tp&U+A%)8XW_|BZ>r>2}F!`F2e>?^i@lcSue<UMV7{'
        '4}zSgv34RFFF8#VaV&(KuI1O0(+;g1Q<Bquc{n*Osp(h~a@r}e#@9*Hnvm1}vdziq@bZnx>Be=`<aBHG!pZ6O>eiFfoz?e~(?klk'
        '+s=xwr9F_-o|cH~6OFY>PS>?(DBC064ox;Ar|VjsY@^jC<aAxzQysUhAgAkknC?;!0dl&oAFC(*5cg$w<t3;0Ku-6(HxH4u2Xfl('
        'lV~i_Ep@sk>7g!lTTk%qft(KXOw80;jhpIe|C=rJzY&1Y5jouu#n!%1v`tPo#IoIWEG>}J4H4}e2%=DOx*@LJ?+q96sxGwe!qM$L'
        'dg%P*^d89R8ZrG@4P-LW=d%FBO!oq(i<0m8aMrWa@?;SDRMG!Y<Sz$eG3)oaxxrX0_p1T#N0Eh|e-!B)Nm&0i<WuxD<U4Qc)CRta'
        'Tu!epETuDDJai*B-7oH39<&jCrxJaq@}vJwCATpkKj@vX9waBCg{<f+i?FXOM&0kEqlK*QE@aV!J?0wWXdx?F$a+*4vWN~g{LlAC'
        'zmR3fHz8WcQha6MyfM*2R;LSD(N`AHLe}H<l?5%nPSRUzPps~{meO97br-VkyX9%A>OHy0WjV4>Y$?eS_VUxHZy`&{8!cqXWh`Bk'
        'FhrRI%8Z6AWUUEls|#7O?1m`)mAd?vs{E#1qwzwPx=!PTtmgI93t6=>a29;jbz57=YF<C^m4&^(J#2j2UC44<qIH3Uvt_-*_6%iv'
        'L`B+763ef5u#nY4tHjx(;r14?+HRXTc%mck$D8*s-K8E{TF6rN<DpmU`q|=>%6=LyWO?4f+UE}4>@8#=%iWLN+F;U)@O87nY;7Sc'
        '&@(aF33rQiZ~NbDsehu;9SC2=dx2tWUnp!cA5{MSv21r03oR-ToNwZtBicC-L>(?<wS-G*t&OY;xLRJw@}hHBiBt<jJx3S5kmdcx'
        '0z*j4SQ6uCpZvxmIo9VaVkPxH0oM>%`v~Wz2kAtg2duM_)f{Z=t6A>pVvik59i0UfvD6Vu{pg$p6tUDl?6ZKP&n+UBx^tF#qW0EA'
        'EOm=4wYzmaVyUCEfF5I(+TokSS!&7;W2s5@NduPJkvC?koid+AEcJn~)a}>bKTEAR3#en3T5%RoBc`+kmRfNZQ1ez>V5t>n0kzw9'
        '1D0BG7SR5CXzeVZUa-_)jrZ!$0_p`z?d>h>ET9G~b;w}0%+Jbh8=M8yl%?)j|E;jpwN2^!V5u9T*xDD0wpr?iShl;0rA3yyA)=iF'
        'L8LkhNR4Z^EnMB^fqg9Sp6V>1#w_&#qf?v()QqKeIcmPq8<tu{sry;#z1lYy!}gaDb9CH)<?Nf;l3qxcOuhJNwlr($a|`KtJw02>'
        'J~XR}A8Wm+{IOR0eB!Nzbg`J7ZTJ(d|I)&559I!0AQp4}$o(aK65>1kKlfLZMLz(L`)hH<6S*(z%5>ou0&;&}1M!b`KMj5afZu;4'
        'd4DR^nDg()ylJFmt{?NF5Po0In_A`b`+)9{s4?1*yYIK_Gka!t(#O#|t=9AN4oa*Egq+9kAa&+-UXI;C>dYa%+&W>ENKaFK1KwPs'
        '6<CFdI_u-Z6E><7G&A*a;DndZidm)NjC<Wi47~ijho>I0@5ILI;iYvOG4Q&-O{+d{UKhB1s4v%ea3AU`GC%G|tvKi1!EMw=`kEKF'
        'Q5)&&Uff1)q;Gg}8@18C>BVhG<Sysw;5H<3m)CS~8xnbgbIHBPZ4T+VdgONg^YzH>{5$o??fe(&k=yw%)+4v`@75!?^BbIbEwQ@?'
        'G`!@;?&iPj$L{98;>Yghzv{>C=D+60?&iPl$L{9u>+IuEAJ-9*zoN)rQ{-<b@;4RvTZ;T`MgEQ=e^-&e7oP8)`CBI#Qwa=}U{WQR'
        'QVFJ20!t-WQ3=*mf(?~mQzh6^3AR;&9hG2LCD>C4+%qBT1hpd=`P3s88pyz)(MM}CFc@wjGzbI+lpi>0aiGo6z#AAGYY-a9z+fa0'
        '8hBgvh6WDO`q0388lpEa@Gif50|W1}yEia6(IhnRg)yGcz#queLIZywQwt6JCk*Pq91IO~U=D@`Ixq)A1J&}g&Yukp4Tw|^3k`?}'
        '4+{-~%f5lYfN)=v_u~l+2)FaIqyE5vaNm&k8Mdq%2n-1KxV(Q)U_iK?pDpzV283I2Dx5zsIOB!}{=nb~H#G1E2B+Q7z#kZ#azg`u'
        'U~tk64g7(@2{$yTA)k;zjq=2?Kv3g`27#c)4GjW8jT;&Sf*Ln82n025Xb=c$+|Yoq8}{4cE^c&q@>K0)DgUWcf&3Lk{+c3xLy^C!'
        '$lp@rZ!7Y56#2V~{Jrpe`BSv@f-#lAPzfegf+>|?S|zYlf)$luO(ob+2{u)NEtOzfCD>63c2$Bsg+TrkZ@r+w`4@jX6pQ8lhW;rJ'
        'i+{cv@*aWl>46-90S>4B9E`J&L<eC+2Vq19VI1T^7{49z9E8D_AL$*&33_Kk&cN_-kqxI4wH{SFiDhq|y~Yiv6LFC{?DQ+bp5qOs'
        '6V8-p#IAijWH&Ive`vRZ!$E=F!*#oToqKWikl6c1e7kuar1oAFcRE2>4+)$!nK;vMhi+W7JYpj~DO!HgolXqcJs!m#nA&bz!b@nK'
        'eJu9w-;f=&gx8s-(e&q>JDupW@0Hr6R%<(8X%aAOPk;#VQ%$E6aWS13vL``=`Yg3`*=gq@dLZ03YTJfAWA{K$k8s<lL#Gq;<gWN}'
        'Uz4M8*^m3WoVZ=`<GvwB`eMjg0?*phx9c_Ju$33=k-1hw4%-<Q$ou%!8gk{XM~R&F2ptpH&%??}<l{m{(}{Dix)S+Kft{ukn#(jw'
        '<Tvc;gxo3EZ;v=3r^&?gg#1OPoeTDeU$Z9@&k^#w&WQI3^dkcMgg}0qkSo9Yz9O(YxbF(&lZ4&2@Rvo85;yI$ItPn?Nnn?_Ul92k'
        'JOCk=xbJv&meHs)f!#qqN!VYL*lWlq3H$4E)UVo;2|_+e*gO3Gmv&W6*!!ydyQ)5McU1Ym`K4V{&i*L>cfNuA4MqN@B7aMfzpcpM'
        'QRMF`^7q2?;SWOuV=9565=^QDQ!2r<N?@r3D=NX7O0c04Y^nrXD#5l&u%i;}sswuq0pfuWf$syP$0j=PuR})B!4EY$AUoZi=zu&#'
        'Sad)=eE-owKX6|UL<cn=8;lP61a`uG^)ZVMB=W2Fj^^XO=peY?{&9~E)cdZdkQ+q@QFQP~M+YDq58M3TtlXe=rE)%W_g8+Y)MN+P'
        ')5;xS?|=Ay-OjI;Hh!gv{LKARA{NX2PW)4J8PBDjGoAu-J=6KBWI7Ax;*uC3yUJo#WG&@I-p|Wsv7{R`R2g$Fn>RDM0H-_01Yd2+'
        'g-V7q5iy(*!x=H0M$JZ@b@VOe)wdM%twodNtfN@JwT|b$91?2wyWHQAS@{husXQ?v{`rT5y`-|{7?{<b8<=D|pPdu<ZIf4TYVMNN'
        'z*<USY1u54vSv{)S?Q843h6VZzK8~dl@ZpbWSRO*xj0_UebC?5p4VneF%9;?&i7*<tW)x(+yWiX{^ztn_4|Zmrgiu53v2UTx%)*J'
        'x8!6k(`)p+`Ske5{~rsyu99E1000'
    )
    assert isinstance(_MODEL_, _pydsdl_.UnionType)
