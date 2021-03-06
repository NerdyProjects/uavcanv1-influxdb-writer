# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/internet/udp/8174.OutgoingPacket.0.2.uavcan
#
# Generated at:  2021-11-11 23:08:22.805621 UTC
# Is deprecated: no
# Fixed port ID: 8174
# Full name:     uavcan.internet.udp.OutgoingPacket
# Version:       0.2
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class OutgoingPacket_0_2(_dsdl_.FixedPortCompositeObject):
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
    NAT_ENTRY_MIN_TTL: int = 86400

    def __init__(self,
                 session_id:          _ty_.Optional[_ty_.Union[int, _np_.uint16]] = None,
                 destination_port:    _ty_.Optional[_ty_.Union[int, _np_.uint16]] = None,
                 destination_address: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None,
                 use_masquerading:    _ty_.Optional[bool] = None,
                 use_dtls:            _ty_.Optional[bool] = None,
                 payload:             _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None) -> None:
        """
        uavcan.internet.udp.OutgoingPacket.0.2
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param session_id:          saturated uint16 session_id
        :param destination_port:    saturated uint16 destination_port
        :param destination_address: saturated uint8[<=45] destination_address
        :param use_masquerading:    saturated bool use_masquerading
        :param use_dtls:            saturated bool use_dtls
        :param payload:             saturated uint8[<=508] payload
        """
        self._session_id:          int
        self._destination_port:    int
        self._destination_address: _np_.ndarray
        self._use_masquerading:    bool
        self._use_dtls:            bool
        self._payload:             _np_.ndarray

        self.session_id = session_id if session_id is not None else 0

        self.destination_port = destination_port if destination_port is not None else 0

        if destination_address is None:
            self.destination_address = _np_.array([], _np_.uint8)
        else:
            destination_address = destination_address.encode() if isinstance(destination_address, str) else destination_address  # Implicit string encoding
            if isinstance(destination_address, (bytes, bytearray)) and len(destination_address) <= 45:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._destination_address = _np_.frombuffer(destination_address, _np_.uint8)
            elif isinstance(destination_address, _np_.ndarray) and destination_address.dtype == _np_.uint8 and destination_address.ndim == 1 and destination_address.size <= 45:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._destination_address = destination_address
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                destination_address = _np_.array(destination_address, _np_.uint8).flatten()
                if not destination_address.size <= 45:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'destination_address: invalid array length: not {destination_address.size} <= 45')
                self._destination_address = destination_address
            assert isinstance(self._destination_address, _np_.ndarray)
            assert self._destination_address.dtype == _np_.uint8
            assert self._destination_address.ndim == 1
            assert len(self._destination_address) <= 45

        self.use_masquerading = use_masquerading if use_masquerading is not None else False

        self.use_dtls = use_dtls if use_dtls is not None else False

        if payload is None:
            self.payload = _np_.array([], _np_.uint8)
        else:
            payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
            if isinstance(payload, (bytes, bytearray)) and len(payload) <= 508:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(payload, _np_.uint8)
            elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 508:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = payload
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                payload = _np_.array(payload, _np_.uint8).flatten()
                if not payload.size <= 508:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {payload.size} <= 508')
                self._payload = payload
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8
            assert self._payload.ndim == 1
            assert len(self._payload) <= 508

    @property
    def session_id(self) -> int:
        """
        saturated uint16 session_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._session_id

    @session_id.setter
    def session_id(self, x: _ty_.Union[int, _np_.uint16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._session_id = x
        else:
            raise ValueError(f'session_id: value {x} is not in [0, 65535]')

    @property
    def destination_port(self) -> int:
        """
        saturated uint16 destination_port
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, x: _ty_.Union[int, _np_.uint16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._destination_port = x
        else:
            raise ValueError(f'destination_port: value {x} is not in [0, 65535]')

    @property
    def destination_address(self) -> _np_.ndarray:
        """
        saturated uint8[<=45] destination_address
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .destination_address.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 45:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._destination_address = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 45:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._destination_address = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 45:  # Length cannot be checked before casting and flattening
                raise ValueError(f'destination_address: invalid array length: not {x.size} <= 45')
            self._destination_address = x
        assert isinstance(self._destination_address, _np_.ndarray)
        assert self._destination_address.dtype == _np_.uint8
        assert self._destination_address.ndim == 1
        assert len(self._destination_address) <= 45

    @property
    def use_masquerading(self) -> bool:
        """
        saturated bool use_masquerading
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._use_masquerading

    @use_masquerading.setter
    def use_masquerading(self, x: bool) -> None:
        self._use_masquerading = bool(x)  # Cast to bool implements saturation

    @property
    def use_dtls(self) -> bool:
        """
        saturated bool use_dtls
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._use_dtls

    @use_dtls.setter
    def use_dtls(self, x: bool) -> None:
        self._use_dtls = bool(x)  # Cast to bool implements saturation

    @property
    def payload(self) -> _np_.ndarray:
        """
        saturated uint8[<=508] payload
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .payload.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._payload

    @payload.setter
    def payload(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 508:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._payload = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 508:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._payload = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 508:  # Length cannot be checked before casting and flattening
                raise ValueError(f'payload: invalid array length: not {x.size} <= 508')
            self._payload = x
        assert isinstance(self._payload, _np_.ndarray)
        assert self._payload.dtype == _np_.uint8
        assert self._payload.ndim == 1
        assert len(self._payload) <= 508

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: OutgoingPacket_0_2._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.session_id, 65535), 0))
        _ser_.add_aligned_u16(max(min(self.destination_port, 65535), 0))
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.destination_address) <= 45, 'self.destination_address: saturated uint8[<=45]'
        _ser_.add_aligned_u8(len(self.destination_address))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.destination_address)
        _ser_.add_unaligned_bit(self.use_masquerading)
        _ser_.add_unaligned_bit(self.use_dtls)
        _ser_.skip_bits(6)
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.payload) <= 508, 'self.payload: saturated uint8[<=508]'
        _ser_.add_aligned_u16(len(self.payload))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 4488, \
            'Bad serialization of uavcan.internet.udp.OutgoingPacket.0.2'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: OutgoingPacket_0_2._DeserializerTypeVar_) -> OutgoingPacket_0_2:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "session_id"
        _f0_ = _des_.fetch_aligned_u16()
        # Temporary _f1_ holds the value of "destination_port"
        _f1_ = _des_.fetch_aligned_u16()
        # Temporary _f2_ holds the value of "destination_address"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 45:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 45')
        _f2_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f2_) <= 45, 'saturated uint8[<=45]'
        # Temporary _f3_ holds the value of "use_masquerading"
        _f3_ = _des_.fetch_unaligned_bit()
        # Temporary _f4_ holds the value of "use_dtls"
        _f4_ = _des_.fetch_unaligned_bit()
        # Temporary _f5_ holds the value of ""
        _des_.skip_bits(6)
        # Temporary _f6_ holds the value of "payload"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len1_ = _des_.fetch_aligned_u16()
        assert _len1_ >= 0
        if _len1_ > 508:
            raise _des_.FormatError(f'Variable array length prefix {_len1_} > 508')
        _f6_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len1_)
        assert len(_f6_) <= 508, 'saturated uint8[<=508]'
        self = OutgoingPacket_0_2(
            session_id=_f0_,
            destination_port=_f1_,
            destination_address=_f2_,
            use_masquerading=_f3_,
            use_dtls=_f4_,
            payload=_f6_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 4488, \
            'Bad deserialization of uavcan.internet.udp.OutgoingPacket.0.2'
        assert isinstance(self, OutgoingPacket_0_2)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'session_id=%s' % self.session_id,
            'destination_port=%s' % self.destination_port,
            'destination_address=%s' % repr(bytes(self.destination_address))[1:],
            'use_masquerading=%s' % self.use_masquerading,
            'use_dtls=%s' % self.use_dtls,
            'payload=%s' % repr(bytes(self.payload))[1:],
        ])
        return f'uavcan.internet.udp.OutgoingPacket.0.2({_o_0_})'

    _FIXED_PORT_ID_ = 8174
    _EXTENT_BYTES_ = 600

    _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{`t?OKcoRdgjQoM7JbcvTXTnwP{->z2u0ZUKIU^X;F@q(#V7!hLgaVt?8~|x7e@k2gxxIz<Wqw2Loi1odA2xB|wfj'
        '=ICRNIp(;>1Pd6OEP^bM9P<5D)jie2p=9fUWa9`BHSDhX>#zU+{#X4q`f~qY{oC4<{L?>~^xVu1n(a)aJ`emacqb6ewiAa*ocXyJ'
        '_K&QIzz^}!z12&^@MpuhpAP?cINLwa_M=FoLvN~o<Yt~0PF|#<KIHLs#6ysnDfpJdqoyC_B8^1eEZn5|Ns({FezdX9olTJs`_t_$'
        'k!F4z5ygX_>d!wLvMILjPlrDp_7Amro~M4N$VE2%9OU=ly&5&_KmL&~0(Zoa)pmK#+c|N$*YqT%-TGS?ar}0a`5TdNuY&Onk=A#2'
        'sNM1Nb|9jS+#9l^Anx!iZ-=ofhTaSP6YC`*n%2CGcP)BFJNlF1jbZ<pc9!$V<*92D`l{%7R^Q4*M*DC3?y$eV?Z(dVvulm1sau|('
        '*<IR{jSrc~?L4-5Wb+gxQl9qgEglrY?)2>36E+@28JNf+XFI~`wjbGX>WY-+b%ae@rjH@d9Zyb4MV7=-Cai5gS5Jc2;X%-|H${@$'
        'P7G1(<W2h)-gJw|$-$)^cQMlBY|BscLeBDC5#>H8&@#Ela~gbmZT<AsbvudE+=_~@17#CMnkd-^Scp5lzb`}@+Zpc)BG;8XWg>E`'
        'J-M;S@F}-Fz9sCi2y#Ecwlu35NLa3)kqiny^FTP?79wg6A?at8F1_cym-MGs*-`JL_qz9nQp8bL&`eI-Y!kmj?^OR~@NXM0<VI|@'
        'kviG_OM756O?hwFf9_L`r+9KrDu0!p)<JfpEdmijgbK6<o6{AW{U?CDggbuT8?uG|(;7-`sf~&AUSkb{pqjnE-3hW`|5VB82#jDl'
        'AOC&WKm4JeD}Ha{SIuevv38sc`}ST$vR>GU1K)vBwL}<04kWlw5|Q#ePED`kcs@+lyV8I5avV847tzF_v}qcdiin&6#y@qv2m+YE'
        'u8{}Y5>>-LAI`GrLDunpR}16!FzdM+JlYU9L?Uv3FP1jjA>V;$G2w=M=-n=9N%@6-1f!-87}oL{{e$EMih$F6)}XOd1GZ29`<VQf'
        'HQ2rZ+pnKJUOi)vvHb&fK>fatJ|C>TV~?`~12(PaJ+bQ@I|#m*Rn5l}{C;TSIQ9gy2JEnUH%)6D*>fB_#10SGlQp_{if2#Vbq+hi'
        'o*b~FdW``)cF)o5DRy+gp5C<*-r)K1?=+tsV^0s*GivO9ygy8HpZ(5r*>U#FfSs7g1K#4@bKi>=dzPITu;)ujgO?Y+_k8vodw#%P'
        '+><Aa!26f(i!OVCy*OYm*W`t_p!dps(_=5Omj~?CyYh=s7<2N0)?lx&R|m|lWJ_GX_P`X`NoEh&jG|-TjelDG^@p+^dyUNu*c;`V'
        'h8{>tZ$7j&*z4?#0Xub1&0vO&(HQ&ILtUG_$xaQ}Y`IUZv$==9278Om4%pk@d7qep@jrSbe6Tt8_JGZgbo&Nq&YJpNcx3CcAF=rX'
        'Ykn^|U>4?_e)v399I*w~9I(X^3T71!&fMRc^%d(fsMcer+2VjLeQ!x%Cgz>po3lD!bxG9aP}fYw6+6S02JGB!e9VL9Vu_LSbq?y1'
        'smrCViMk$Y$f(vo%gznhh5M2XTcWuacgv@)x4PEqI5AOTVnj-Ycw^@WY`Kn>MZ(Lal4DaRb*$8pV&cR^iGdNd9=pIUvgH9=xo??('
        '0_MLnlFM$?n3ypUW8%d`i^huN58Sa!Y-PaS-5WROKy#U}^Ipk?i5wF*CTdK~n1~s}i;@s{c!#|^VDCSWoY)G{_?>YKnFuoRW1{EY'
        '*pYHlTz;?%L(oxy@?GpCD3|HfL5=vbHPyhNuUgX$j2pC$HZb((t>+t<``0bIf$4wSnr(o>-?bJSSmN(n%MJDc`=<3lgMG~Yq4jZt'
        't+Rh@tvA?b?4MenHQ0~YFW7HdKW;FO{WIzWmat#3ok7tNC`vdgvra2%c+PK4(J)QP;v+5^ritSpe9=HD($xPK4UeQ~kg|Q~MT31W'
        'NB9Ve2D`3@|FcDdJu38mFhv9H`3<Sv-;Sc;5piS`4GINj(eR*aKDwgeyKwekMME7QyNiZLQ!*?)q@v-$ONLYTC>lz%EGoRnqT#!j'
        '3@`o<6%CV1h9@6l(V$|+-HV2C?ELR68Xk7ZaDG?OK(bQ#f-V}ozrkaw624^9R3&`HkhP*tpc(<C!h_TaR3-ezs1r~b$Wnn?4xZIN'
        'ZuX_P>!u>hhTf^q{%rr$)LI;JKeDO!YR9R4b=}qj>}^k^LN?G6-V0*x+L;#@flJM{Zk%rO)D^Cs$4%>coD0>i>!cV*oz0Sp$ZQTO'
        'JP6`#j3$!vG}{(CJWK-ovUL7@)BJ0FSkj=Loop<IJo`x@QZBoABBCCcYj4NtW~Tak#QQey**vq0$iL^*6*-Gquc0M-f_h&$-=uD0'
        'Dw~{+$D>FD#5r|FyItSGPEvo12w|s0B2GjEPGm!`o5rEdqn@3`Md}FEz!a+INTRV)0Y<VM<4vBLmg<dS71z*&>V{!tPxdOsjw3K}'
        '>HJwcc5;zt^EP*!IF-B7E3I9>X=jOWd~hl?-L!76etLQJy6sbYo)lqcdFo?+TGE%j`dXVe6>i}ut%o9vQwTM3D*<#0jKk<i4(Jrw'
        'ihb@pi7MqpHfvh7U#YoE19=!1k?iGW33oJ9@Qy^{rxHZ?oB%H(%5@t#+JLYi+AQ;_?F`6-M1V(t=+=c2Ue>I7aBd;wNdijd%ekg~'
        'MWHNPv21$=G>WjPuNTDW#*BT}KMSTtX#SZ?OU*MEmYZjqXYMgo&nLzzPC;O4aq-N`qT5+sSw7Ftt}Nn@`mxNH#LD8?i;F84&z?Ou'
        'V-l!#Gp|rWf~aU!q!fj50^`gWw4}|zUU(<of)T<32*V`gS?HlFQmAE))>-}V^4iLtKPr)&$KOkfGkVjeHVnS)Srd2jb?nU5TkJ3N'
        '4}BQNf#6ZC$L+n!8mgE5wQ9K+nP{5^MJ@N$D?2cR+@|{*c85Eg_N?C&&3Pa_lb26M4uGHs67s?I)m!iZK-=6{yZ_tCYfsbKZXS>?'
        '?f=njP+7x*8z~R%TXdH~`h{z}2g|xCoFet}UejJn<3u}Ey2?U#6xMECyGiCimYx*}O%ra@`XrIp1-b#>$RtC@`-j(|Ky0#pQ^k9}'
        '|KjAE16wg&37P&B|Cmz5Mh;}OgDG%+XJ2D#s<z!F{ptL~3k2SB>%SV_rLj8@@2Pk1d#h@NHKT8SO+EUAI`3vn{Aj(s{s;Qg=R|)}'
        '^W5WX%Ima#@l^fPOP^FBzFsd6$BtsyukJQX2gZXsvXKJ6z0&OhH2zi<@ANGbiK1;E7#<6J`U*@)(a($Ft+qtkf$I(7dDqspf-~jq'
        '=za<L61Y_9|04VR;<DZ8<?zdJYh{EbhmTcUfQ0O)L*WF5O4l-IoaMw}C_|it2D#6K?t3)t8)UP@(~XZV+ZQjLk#2kG+=WFMY_Xgl'
        'Ex00q?WJPN7uy<8)0g9jE*9kmm<-L@=Ixeau#fhY>$h(Fe!F$`di&O`Ym`I05A^(DCa^#EbE_pyiejD$`=*266e6jc8R9YG5e*GU'
        '>XOkMp^4H5c|&LvHy~7asUiv}F#!=v5x^L@ue2+Z3o>scExzL+h%1xs)shbxWkO8QYox*f2SJY<fLk#GB3-@(ULfvBY(uJXB(kP`'
        'x4jvcqbM$ia4j65sCIK^anYn-lR^_1@4r&ouh^k5NaxD6%VpCyq{ewrnegrY6J7G0c$(q;NBT3~_a9%raBgvNNSAg9=c0eyxD40s'
        '^wdQ=((s$!32)w;_5Q_cdjIPE()$nZ*LP;1&^wROkGJW^De?~eLv5GhGu^OphhO)fY<K+~;mSKsbnC43?aBVJw#t0)DiH02=iadY'
        '#c2=lJq`J$r=ecqZ$zh6{M|aU;78q{*l{}x+whDSkQAN3ciO4gC<0n%bp0;VlTMd+0#6ria(em9#dBj91DlJ@B^}_0*tN$qFp|=R'
        'C~&alJ7V}XAp7sn>AP_uB+WNu&L>r4TCK|GRQ{&(9eKBnvL31Dn&s;eS2cf>Npt(!>h-2&twudXMcz{z<;T_P<$XBXDUFAtQ7Ds+'
        'gP=wiwg_GrS$6={wYyylmpN?)U*|ye>f)YSF|*7irKiwtt(NU;2j@qwFZHf=N~2|9D>9i<?*Ml&A=ro%pQ|IFmB4Vy9m?oSxreVn'
        '4B_$(@>^;bepcEL#Vh0;P5Wj6D^^k{J#U$nNa1JJOgOT~8Hnww%qWEn{4|JUCw*tuL(&~;I_lD2<%5aq5gn}0{Xp8Jb%lcg;}u<?'
        'q|lrx21<Dec%NRiPvp{>5Xi2S7m_QY>MBxsxzR}l#Ar#TT(OY~sZe$IE0u|N<nqW-8F!Z#0o`W|kk&+wP**5T#FaG*Ra9hJh7Yn5'
        'gb$HoN$k<ZBb`O}Y_~`Pt;`Y&3h1tn;75j1mM>NLCcSE@I!U}t$xCA7fiNgfV=5io@;YgGZ8MGY*ogxOClf(eZiIYtYPiRIJGSG_'
        'mLC_Hg#-=!ZTKbr_3ci9G(PT)s2ieKu`J4OR~?7$oW@b0Ms)oYr1dtji;ak+R7s$`LyANdHtBe!KiA9Z9Z<z2I3?V6De*FrOFf1n'
        '=Q2Nt5KFKUz(8SaJTU-bTmcIW{Ya&nrIev*S$e^g<Qf2kP|P?2j^8DFLd`P9sw#auR3Oo6(6t}KNTu;1mnYjnYM;x?pn2MxSEamM'
        'pu7(Y>#T0VDx;CbYk8p;m7EmndK%NdWEET@h7jQdg{(dI7AMcLA~dCG$^$+llk9L=mBKfRbe^C>i^&2T>s2z)m2;+iPa1Fea_x#&'
        '5-&-uWFbxImL~ZZxdzJLz&AN@@GFo`xt3nTG>nl5Y~@o%CN`S<mSSIz^*erm<X$BhSsZNXW0TTSc-Zkb3Yq?|MkUgLfuJz_A6NLT'
        'psVCVCk_TvQUn^xG9>Z5Oi&Ox62l<Lz`EpP<XJ`x#|0E%G$d{Mnvh3a$;#H2*Bgfy)(OeMc1`3;r>KClhmNK9Bd94$scNx#=_WnW'
        'Fy@0{pW+8_=y!Y8s4mlqRwpi0G6-D9)k1Kl(iV}DB>KDtMj%Vfly;a^iMl)p@`Mb}Ruvs2GfKAF0giF6{B15AFY*CCvdamCp}5T`'
        '-lpUlsbWrYli<zh7_DU#rSlY*XW=w9M1)7doPAvlw^#LHn=BXu6%S{T8_p>Xq*%00Ei9*Zsr+Dw;#gJ>nNXMZDV)VhO-`ID%t%IM'
        '4G9<2_36B-Bajc1M(=jLzYOHr$PT5T3?V6l9A!pj)&lh?UulgMO!IZ!PAU)_k*YeWbgT*iu}<?wY^fZ<s>V@(&SN4)@k(hpE5B(n'
        'mOR)qRrWojouiKAl%$gZ5V&AuAq8%$^!P?`Li?hsLJF6Pae2bDAa$mMA#=&mO@9U5Z91XUDTFi)d5So`H!0|*wEuO?q>Ap`#pR3h'
        '+Nq3aV$U#b5GtdhnadP;3{Cp->ln?7IeNEnb*+TSNO6imWXyJT2)BzdMdnlatqV;+eTifA1(b1+$skguAJP%T<WF^|LQ$c=o1qhE'
        '^3|fs41v*G;|^gGXk^H&mzBMGIk~HJwN=TAd;`I(^rf;U+-2peu#&o~%n#_R@~`rslw3dg#;lahh;K3kvE%WA&VQu?^s@<NX$*q2'
        'jj~h}JVmrg=MAta2*7LhXce=LC162dAM-609JSGMqpB&38pDR?$8n>u?|8!59IMvLV`8h8%_!^9>eC0#vP6;&b(F>My}Ads4lLC|'
        'rM*#dqMQ-s9CxFaq2iQ<ygoOPG`V(U^i87};ZBmU%$@q`Sh6a7B-QFz$MF-HCdjd>*ip%oEF|rZWomsjLP0hvKdT_A2l>%ftV=aI'
        '!N|y@c1c{hb^78}4Gg=zxW+YfXpLzm1SEX~Z-`(PRlWuo<#wg5%<1GvZdycHk&02+HVsS_EtuJ%LzZllIxVuw90jOM+Lq3u#!6MF'
        'OrG6SQW6k8$O`eih*GjrRa~uBm0*D6v_`0`_R3)7`O$734Ivp}v$Pr+fTGyad_+PYq>*nSEA47!#yYF2D&4xYck8feuam*)XhOA+'
        'L=8DSfAq~Zsyp>m1t_Yqr8826=h#79=`1EV9-R-vsLit{Du{THjWV9HIfI-kk-3K7m769{V`d4i2zXEW+Ef_|eTH+eMxkDEubWN8'
        ')K7{y=j4SEu8J_^ss9B^DY+;4Ej_tGjQ1$vwqwUBAVKn{+BWq8o|f;(i|KQ#vT`d!rt%)rD5`^!Z0w|jq**`o8J&WZCl`P}2|(rO'
        'qiVf!HDk%^u3AloW-5oql2)OI*P4oyTj^@)iaHG#nf9nrR{AbYKyOGEG)j%xT|}fBI1~!a9-(ZY$!fzjk49_XH7t9%s%lcnk->mf'
        'wufXmf`z(0)nOYoipI}WWuAqYYk1#HUpn2rIfY1#zB2WOboPu#qmy(60%~JA@DzlzAjcvbo?NwJ6$!sO>WOkVHu{!lEoZ0_5LqeJ'
        'o!}UYyVR%>DnvdVLX;bY+6nU!Y*l&SamGhSxfPR`EX!~;p%ksy@yi529##42C^k@*t2Bx@Li3~8B%!BP3()QqPn7h-Cn%S#8S4m#'
        'Q&)@5msD~hJ8sH*s{l0N2)rV$&g+nk07-M2fw()K4iK|Rz?~{WkYy=`#spp2WwyJ2Qe_gZfe~#_tGW-6z}TS!7dmwEu>y>~d>(*C'
        'm64I%?n=Na`%|qD6|^k{C-NclDr%_Yha(b)Np4n^d~#wq)`FMK)RC?6U?WZ;nXo#Z1QRi0b)@%SHXbPtB+pYd4U^QTnNS;64O9W!'
        'F|S2br+4N_?!0Ao^5tQwEl<ql(VioenrJILSRl+*p=0Eyn)dC|)q4I0W$JZasHbni+4!4eda7_tWbZ+qjceSMM-$~~X6~hA$O$lR'
        '0CB>hVH_=VV#>$JD&xJ{T{5E>v9JZ91iew*iZfBKZ*)%D98T^}Ug<xj`>MOX&x^N{`<T_!J8O-psUObZ@&0Xpx}7N54Oyemy;uBo'
        'Fo+thyC$dxt&Kr;HR#TlSVB*)zwtg+<7d52YtWcDVeD0H!A7;<97g@cWCCNa_8{;!M*Zbv0%Nag1P)XL7BTAQlL?H!I)Ybf(g%3+'
        ')v>Wj)5U~Ws-x{4@(z1Py<?=o6W*-X^nU66+WSw{&!bkJxN{LdzfbS)&L#Z(`pyb|w!S@i=N)?SF8z3qo_nY6PzShwuq}3A@A<Ix'
        '&C~r8ZCC#{AZgn}<ikJX|FM95pLYiAz3vQrw(o9t2EKWk1XbPv$c(E3Hr*(g@RlYw{~OvyS~UGc000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
