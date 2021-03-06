# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.2.uavcan
#
# Generated at:  2021-11-11 23:08:22.796228 UTC
# Is deprecated: no
# Fixed port ID: 500
# Full name:     uavcan.internet.udp.HandleIncomingPacket
# Version:       0.2
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class HandleIncomingPacket_0_2(_dsdl_.FixedPortServiceObject):
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
        def __init__(self,
                     session_id: _ty_.Optional[_ty_.Union[int, _np_.uint16]] = None,
                     payload:    _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Request.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param session_id: saturated uint16 session_id
            :param payload:    saturated uint8[<=508] payload
            """
            self._session_id: int
            self._payload:    _np_.ndarray

            self.session_id = session_id if session_id is not None else 0

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
        def _serialize_(self, _ser_: HandleIncomingPacket_0_2.Request._SerializerTypeVar_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.session_id, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.payload) <= 508, 'self.payload: saturated uint8[<=508]'
            _ser_.add_aligned_u16(len(self.payload))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 4096, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: HandleIncomingPacket_0_2.Request._DeserializerTypeVar_) -> HandleIncomingPacket_0_2.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "session_id"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "payload"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u16()
            assert _len0_ >= 0
            if _len0_ > 508:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 508')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 508, 'saturated uint8[<=508]'
            self = HandleIncomingPacket_0_2.Request(
                session_id=_f0_,
                payload=_f1_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 4096, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'session_id=%s' % self.session_id,
                'payload=%s' % repr(bytes(self.payload))[1:],
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Request.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
            'ABzY8W}=N@0{?|rZEqb%6?RJ6xSNKg2~9zj=pdj<CFk0$C@mm?+=M8WW5;rwv{I>7b9d+78L~UG%*@{Fi-e#;pjKKzr7nMlPyH$V'
            '34GxjA9&8p?tQVZAyVvncjx7t=bYy`=lD;T|MAb88{uE`W;M%QUJOzvtm1|GJs%cgkY=W=j8k5;&9(cYP$fR*C$mblU$t+4*8ZWr'
            ')4Y@_t%YsnMsw|nw{_-gD^{1hm}*|)h@F~GGOh<odttTkgF3GU54p|@v8QpB(&HnZJ;#e<@w-|$-!_}+L|CVcrt_~n>pp+g?r-eB'
            '@YnXUwz-;e@2wivUbyyCTy}vc^Hpv0;sYg$d|_Ua=G^ntlg$@xuPphlCRlOnsdj3tMZO0&#=@@pdNmy?pB6%oy=?by;P8w)pOz*U'
            't^8hd`=~#Nwhiv#-2uHKkN(mgx6OA_=Ya^f`SL-Z*F%{!i4%_ePgUMFm($#2ZS(IFsT>=TN6blH6f85^bETP=f;r&MCcLNxzH-l|'
            '+_Bn;oDFB;ePJ?QFbxaXR0_?U&^e+I-etyG;VKiKnA(pGJ|tC$5KigWl`x8raRD4+kGo}E99gg~8ZcEbZYVCg-y2qPpULn%UhG6N'
            'RbDdXUAK~a6Q_RA0*}`s;_|!A8yAG!T0U!=*Pn4b#gj(?%Uyc98nbJuC`2i=k2xUU=uZCr{-%6W{!so1@Ha0bknmmkS$puGOU=zL'
            'G--hT+{PQ&_=EjR6w<i;ayl$r+q~7Ax(F_;_GiDh%_|=&9}RwjubrvQw^CEJ4ZG+NH!FvxP)Lhg2ck3p!XsTCSHf~{>@sIFsXzhw'
            'tLC+PMrYg$y>=;iO)IU?L@unqepnX;x3hCAUrIxm+rPJW_HTUYhH|$9<34u1e$4e)9E(bLb&*NW(~_SOw%G9~Je7~>uuU8m0E9k('
            'CG>&TeRI9JLbR$2P6zB?qO}`e?r+B5HJB$(E3SiJ9M(etlRiOQesl1z>+;ieJ0!<4x(ighQt??~I3RlK<A;|vHhw)CiHvB=x))t)'
            'lXA>6dt~es#6^0KtSP%hE{zvV8s{05YzUOgLGtwe5sN%>k(WJZOJf65HG6O81CRuw#>}X{69k#jJ-Ibi6-new8JS1x5@={yYn6pq'
            'GH9r(D6I$VSd4@viXA_=$KL<hI}8%T-u=l>cgSXZVM^c4MFp-|F;QYVNbbY2vE^lFpg7G0ZVbB6(SQu|%i?2d{37#|%OVUN%Srso'
            'z;Yt4Xl^ZOb~>EJ>OiUTV|iN&d8dYo!Wt_mG4u9|=G$P|smRmHSWn`2*u0uLQ`=17MIq9PLnE6%ZcCuC4SliOa7#d>w`0YbymMFS'
            'QBj}f!@E<98fLevdI+MVR*aEAxMfiTT(@bvFH_qnQ`_(D?5r<UJA-!zaRXSFO738dB`tv&6P1bfbEMGUUf$RU`O=Fe0I~`}Th0WC'
            'uaB9-SMtV0E#K?RVH7d;X!nrf$)k97OQJ|V-F<csZ-=!TBu9ndj?%D;Kds8eNa;Ys7{dQ4;W0tjSfIw^Y%?LR#I)a8%@<MTQ++7R'
            'SY?AGS<oY#3Sf{MC^036y_|LE#Fx+lN%m3V^Hpm=3WHp-u|7N(p%{1zUc)2Dcn)pCa>)Bug6e0cRF()6M>|AW6=sIZZ4UczZ<Zm;'
            'xyHpv98V{ZfAMoy=9XxjuabaH(8l+diad#kmIJn%=K)ceFxvv$pq}juBy902>g&QXUQGGSb%icxHGbj?S+^9I^Ohv0656qln&DWO'
            'ToEm5im2$^si_A8XCdn(f9}kAw5zhlo6Hmgwin;^0a1ElIst)J36}tptur)c2rU#Gjf^KzFd<zhVolqCl(w^l93JkTFi*i^sw_pW'
            'z&yf>K%H_$?j+;@#rWjpQHbDarK~_c?fE5%!G@ql2#R0Lv!&!FkaQmu1|m#IC2Jqu4f4^4vQu+9$!NkLnJ1l7$RRa~N=BbUrw{<5'
            'K<9N9{RZ7AFGnMl1(ry`^R1w>L+BVpDXc;oP-tR2&geB%j2P}HHt4#0{Zyn3p0;$vAS3aEK*P$33VcHGRXISMk<D{6Lsa1h=?Efu'
            'fl4r7i(9yJb=kwZ=*%3%N)zZt1IDaSIM+qbh_!;GHYCVwUI;^ky-9N6DNA(py~DasM(Q<TTEKTku9m#2dd_q;W!~?0+NEqv{TR{`'
            'C6me~Y(~?JVlqe`)Rv4YgH0;9RfFv|RM#mvrd+tdfM_K=B*b8lrE)_8+#9f(AH<v_x*jq4d3X2<W~&{oi*S^H9=1{f+&_H6sMfg^'
            '!P`5U3kqO$h~6jyn^3pT&sjpqY%P%y_XJu<J_%hkhzV;;s^ri&F^6?d!o`I#Y9u@8Y@lW&R-Mpv%gq{2_ip_Ek%F4{0CrbW`V5YA'
            'OJJBa94&ul1%;2QSzQhR45f%QRHCs7x1;zV3mq*%+QE8SJK{(OUYc45c1V@ys4q0K7UDFjVYEM4rEQ?n0=}p%inN&cNLiUL<9J>e'
            'ak*cNSA8)88I`fr7!^RiKx!<oAyFH`*PMnyQn`Q>`RwD=vjk3Xe%&nf&`c?$h`kV9o-SJ*eT%se3y@gIcGAyS3u)l<lEp&J-U2@q'
            'g3&dZHE?jshEWRPniG9~Kq$YsV`N1*IY;LRk3!-k>rA82A&pS1V&@Wiy0fS$?YyA&dQW%VrVEIyU*2&%;rT?l7`9$%(Fzc{7er^!'
            '$`9l(;*{~rl~LvT5dove=SCE~U95W$x9-tUw0P?0pOyz0nueN9w1wf^cK=e{O(OV@K_rYF^20cvFw7?#OOOA&zge$&9;Xy}RlXu`'
            '$XCgT+wzW(<K-q=sxRbk59M=N$PzuM)R>n-OW@msuWvTD(PGCx=-8BM6@Hx^Vi|_m_rv(Q9;{^$mK|oR<KId5>7#>>UsyZa$xja9'
            '-q$zDy?z>V!Os8+z5Hg)OWHd4FHcj!%Eb}@00'
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
        def __init__(self) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Response.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: HandleIncomingPacket_0_2.Response._SerializerTypeVar_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: HandleIncomingPacket_0_2.Response._DeserializerTypeVar_) -> HandleIncomingPacket_0_2.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = HandleIncomingPacket_0_2.Response(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Response.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 63

        _MODEL_: _pydsdl_.DelimitedType = _dsdl_.CompositeObject._restore_constant_(
            'ABzY8W}=N@0{?YWOHUL*5MB@kd8h<=_(&ic4IY>UBgTs{5f74;l`QIwbb6+X?GCd&lkT2%*Muks4J4gNLV5FtdbE0XNp^Y6WvWwE'
            'U-kEW)jvl5{2eKEKEIf^g%xSUEEvU8^^M0VL@db~d1jRZ^i%I3RSgQor*;l_iq8)50GIs@rnClwvgD_BoGB7l7#J+M&NOcj#9G0d'
            '3D=R*4vYpD6(Wz`b1hQX)HF)z`ZiDYDNzHPXWCNF7;A#DD$`-W=$Br6ij`7j_!l0cpJ3cMqvFDW#a;9>eP<T8yQ2?6oq*gx!ifPM'
            '`&(>JwLq{uGma^NRX@#aR+t1Rkpj!Pljy&fW!8XlL8_GZG6Slv%Uu%9wH2lJ(xN5em9K_mG3C67Q<X3S^&$;ZnBa~xM^e~cQ~8W}'
            'nV6T?S644*zZyM{x($Jj<d$w@K)Ya0Qzd{$euRlEL0>|O;?$yldS+m(97{phouqPi{)~R|t#Tha=N&rsJo49AmZM*~3dFV>aYp3m'
            'K3mYpXgwU+@G%F&U1s{1A(1K-C?EUV+gu3ZbfHKthitV-Q*PSlvxLy(X#w~fmn)?c8`A>hT_CKC6*18zp~(FZ@Ky*$StApqc<3Hy'
            '(8{^)>`1kUZCu21Tu#VIc}Gs~qMSKEIeRSUs&ZZ~$a_cfzI;Fc&~hX%Zv7kbbF?PiJvU4O7xW7b;#DssH=$THsbc0c4X$eto8)pG'
            '%-|!K=o1wyOLWzQTNmyQC|~=z?K7az7Hv>&E2L=ChkjxW{at1qEekiIALxh(K9q}{8S;^Q(kJokMyA8I>r1`zH@jBRUeT*rmQfdC'
            'E$F^Px(`6j*SM}j4RUbmD&zONe!P)`SYsz06JAv1I>{?v9*~VaZ{;hp2y8F8Fnlo?TBHB}U)m6-1ONa'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.internet.udp.HandleIncomingPacket.0.2()'


    _FIXED_PORT_ID_ = 500
    _MODEL_: _pydsdl_.ServiceType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{^vGTaO$^6`l=Fyy;xlv9W`&fRaFw1MAs!M7RkA#>RNH-p#UJTR{SKYPxHt3U_yPs;XypkPzenWJ|3iQkwt30}_8B'
        'e<A|$l%K!@NIdYscdEMQvO8<w0ZZQL>AIcso%4O?)coe$?=M{L`G577%4urTtRGup6wlNz`5+VhIMI2jt#YENU$`&KSS8|UT8ieQ'
        '=JofQUp3e2mtrH{t%P;4qxZ5`zjRw<D#wy^dFFGmDhgrzl>5$9iL1<s&7O@5p5v(PijNas^i|=6DTM1+Y1zNai!>8E1x!-K=zu4W'
        'FmM<SZ|e1UER0pUp#9H3Y@a`Bc6+<e{H}Qq=EvMQqXv}|w)r^@JHzAItfqeUjuKfqH!q4)?s#zYtmUO4-_;m1E<Gr$8Wkelfg2-X'
        'mVJF89w--Qq8K^Z>|Vg;2?vU~PJ!YV>njJ{MzpMd3uAjUL>~RNIc)0B#?}E5Zqmh#9#;doQAbu-@;_E-Q=f}doiz17j-;||NFFgO'
        'd6uz67mllfIVqS0?rhAnO5iJZY{D(8tVr2l>c=yk@Qf9(fK8+*m=#5eDEP5N8zXF~!y8?>k;X$*`Uqi{Ze9+f_y`BUA@)`~t&Jn|'
        ')&&D53dRk@S?4>=a_$o8--m;(h$hNOrkrhOl5gVJ^&8;v`GC0mLVfj&kQ>9NP5tUaj<<Mo&trL$-kwZ$k%?RsU9z)w=P&QB%dg05'
        '@^!#pKaW7dcjczd-oMuBi*0CP5B;fy7qIZP-8BknSbi=ZWVWea>r9;o7goEI-<$fyA1W6NzK^f1sr6@KT{bm4YZE)o2Rc(oi%WYV'
        '*8svHUEV5%;ZB=H&L&cU0`hi!`Iasc?nJS2DtS#ajVOp*n7^@KWf?cqQ!}57eVCgMnrpikKC}aQrv+mNt6n|i#Yh~AQaE*%Nsr>3'
        '9}~7%@e}`69?@p&*vtb6eE>`7f#!X>QJ*JTRT-xZcGqZb@59~o@L7R*;<)667mWRCAYjrvhzsBQ+lCyhS|Nv+MrVO)=Sx1#GzUaq'
        'd;9KMulJ+jP$WcK)(*6(P0BIL?4dRj5Etn^G&*k+IoD1wsjXvBvH?)e`_Y5j2Q2W&23~fY&9(7NE!dme-vUV>YD^EiGeM9kos$|}'
        'mVrc8=Ye@NFM@{VRiP3eO9l;9C8c$r9g3kaM6ts=x7atoeS<+_*c)H}#x~iEFH9BJQ&ECzMvRr1^rPEwY-D)e8YqqvffKzhv@{^Y'
        '+@kpC3Lj*ivPpoUWjTpo?paR674@YB&5j4tP#q{$zACTEU&!kfR20@2L5Z0*PwJP!vSX3Pr8bVlZ@+#ewz@Kjz(6MAl0zfwUvEjE'
        'u?2lGTX0K2q_;xF8Q-|BieXkAr-SPggBoVG%4z_jpvsMqKsaSy18lo!t1DAmC{tT+Zf~zHRoneH`e6ZB7fWtojUg?up{_QMkwWi3'
        '-|P8&>BJHM8HJ!NW&*_5h0Nhgd831t@3iJHiWs|hbD!eLgLt-6f=E8N`S2D-2bJwd2btiO(y)y`%}T{k6`qD6gin?5kRWU%P~)+;'
        '9+OvM(yc6KlPL44K4f~Nl71A;>EU+;Fvty*n4H62&RTTBAhbY|eU$io*&2{SBbQ95508W|2F`%j@W?WrLYpuh^1d0N`soRkCBnqg'
        '3XzwYp5kzm!akgvB*=1J;9w+<qaDb<@Z6TU1sbQzB%mD%?Ycun8U;l2KD(Kw9#NPu-DK1|Dbp25*y2>s*STdpoA9Y^3th@8{KXft'
        'ZXqtGEs1m~3d?+I`fXuyNwlaaqM~)Dq8<#Kg{+hO*%SNGs?unu6P@+hP8jO~qKdI@1q50pYy?O)Ptcelv`}y~GLA$+`*a<P6>S4j'
        '+DzwixPSAAISLk2c`i}~<`G^5>VzwDCn5(Z#z#l@d<2h6Wd!nR$1O+<7I-y6P~38!EhIOARCGaMAi|hbvU0&)FCSefTQ#ShbU_$I'
        'v!t^MIi!X`$>`a43LYQ|bXq0BZ_thMayV3pXNeR%-Sj#;fQ~_w{4Asag(k$~gkD3%h~buEgYLZ3Pesb$Xh};9G7^6XG|U_;&nFaL'
        'l>)>m**r7TM-_gMjv$g}s00JHIE7nV<sGc^&dfrr3IbghfHBDw_O-z?Vyz&l^$9Ya6+$0jr=wIj%90}Z-eTP)BlVgv&Eq>IS94yL'
        '9cS8_GV6C+?NTPBeh6ufl1XI~Hlt}qG3iHlDnmx)-X`VUs=#*RtLuauQ`R4#L9`qm5@ImOP`M!i?hIJY4`NOfTo0Ihr`>!Bv*nJ~'
        '1~_s+4_he#Ztve`RO{@L;O!jD1O>2KL~j^?ji_7arz|04HW$c<b3831ANwvE#DujuRdVQ?n87+D;rzf5HIf~4Hc&GXt5#^*>3RjH'
        'J2(FGm4cdg4|ZEpx(p6<i(r`194&uh1ci^PS(Og}45f(CRHCs6r=$2F3oT7S+QE97JLE_Qp6jac?2sx=QD5k4n~CF~hQa=5nYNxv'
        'bNGU`DAHo$BV}c}h~sHt#Nlp!z3Pe)$f&fT#wY{w8B$}84T;(SzNT~;B$e|>k<TvNdKSR(&ab*l-PIEcDPk`~o2QFb2j4<2gaRby'
        'vK@7IthqGsS;=C)W^aNY3c+Zb%nCSIW&BkN;hGVBwt+9dIAdsp-#JC+2#<W?M5|1r&>@XbtU~AFd%BaTslqxz?e$L4cAM5CvU+;U'
        '@rb8mWkc9Hr9~@1=$;Xsej~ppe-LgNx0bFd8wUhTF*<cc!RUP6Zdkfcm!kRG>FjCo0z<c<dL3<{-?!OatJ<3g{^KIzuO0Ho;eG-Z'
        '@AVd5Ki*xhR=f|l6nR0uA}`A;WW-f@UC3;)iI&9^srO|m-<1YEsI<5*`If*ndmmq{ub{;aKj@g4Y85_CUSb(8vETLA*VSMxg0Sc?'
        'TfYANw0-*7-rLWtyxYll_Tk>g7s<WuHfFt_9uyk<bj6^*7QP&JzZJCRpKni#<csaoMt$Rd_~9vR)^x}crYDfBduJri>hSjnjV_Ko'
        'M7?)1jDLK}Ve(J%{k?y#$q)XIaoPR;Q^JC?&koDyo>?6hV1Dht#k`p(@$4rZxlVWR_9w`OP+0uINB#k$>t+@zKip>jpXDd=uktS;'
        '`}h977Jz(0`CkqC{|0m-Jp3CK000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
