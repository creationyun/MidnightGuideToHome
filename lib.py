#################### 데이터베이스 Databases ####################
# line5_west: 5호선 서쪽 지역의 역명 (방화~행당)
# line5_east: 5호선 동쪽 지역의 역명 (왕십리~상일동/마천)
# line4_south: 4호선 동대문역사문화공원역 기준 남부 지역의 역명 (숙대입구~충무로)
# line4_north: 4호선 동대문역사문화공원역 기준 북부 지역의 역명 (동대문~쌍문)
# seoul_districts: 서울의 각 자치구
# nightbus_list: 서울의 각 자치구별로 모은 심야버스
# subway_names: 지하철 노선들
# toilet_list: 지하철 노선들 별로 모은 운임구역 내 화장실이 있는 역
#
# MidnightServiceKakao: 카카오톡 플러스친구 자정시간 귀가안내 서비스 안내 메시지
# LatenightServiceKakao: 카카오톡 플러스친구 심야시간 귀가안내 서비스 안내 메시지
# MidnightUnavailableKakao: 자정시간 귀가안내 서비스 불가 메시지
# MidnightAdvanceKakao: 카카오톡 플러스친구 자정시간 귀가안내 미리확인 메시지
# DHCPServiceKakao: 카카오톡 플러스친구 5호선 - 4호선 환승방법 안내 메시지
# NightBusServiceKakao: 카카오톡 플러스친구 서울 심야버스 알아보기 안내 메시지
# PaidToiletServiceKakao: 카카오톡 플러스친구 지하철 운임구역 화장실 알아보기 안내 메시지
# PathNotFoundKakao: 카카오톡 플러스친구 환승 경로를 찾을 수 없을 때 나오는 메시지
# InvalidFormatKakao: 카카오톡 플러스친구 환승 경로 형식을 잘못 입력했을때 나오는 메시지
# ServiceErrorKakao: 카카오톡 플러스친구 에러 메시지
#
line5_west = [
['방화', '개화산', '김포공항', '송정', '마곡', '발산', '우장산', '화곡',
'까치산', '신정', '목동', '오목교', '양평', '영등포구청', '영등포시장', '신길', '여의도',
'여의나루', '마포', '공덕', '애오개', '충정로', '서대문', '광화문', '종로3가', '을지로4가',
'동대문역사문화공원', '청구', '신금호', '행당'],
['Banghwa', 'Gaehwasan', 'Gimpo International Airport', 'Songjeong', 'Magok',
'Balsan', 'Ujangsan', 'Hwagok', 'Kkachisan', 'Sinjeong', 'Mok-dong', 'Omokgyo',
'Yangpyeong', 'Yeongdeungpo-gu Office', 'Yeongdeungpo Market', 'Singil', 'Yeouido',
'Yeouinaru', 'Mapo', 'Gongdeok', 'Aeogae', 'Chungjeongno', 'Seodaemun',
'Gwanghwamun', 'Jongno 3-ga', 'Euljiro 4-ga', 'Dongdaemun History & Culture Park',
'Cheonggu', 'Singeumho', 'Haengdang']
]
line5_east = [
['왕십리', '마장', '답십리', '장한평', '군자', '아차산', '광나루', '천호',
'강동', '길동', '굽은다리', '명일', '고덕', '상일동', '둔촌동', '올림픽공원', '방이',
'오금', '개롱', '거여', '마천'],
['Wangsimni', 'Majang', 'Dapsimni', 'Janghanpyeong', 'Gunja', 'Achasan',
'Gwangnaru', 'Cheonho', 'Gangdong', 'Gil-dong', 'Gubeundari', 'Myeongil',
'Godeok', 'Sangil-dong', 'Dunchon-dong', 'Olympic Park', 'Bangi', 'Ogeum',
'Gaerong', 'Geoyeo', 'Macheon']
]
line4_south = [
['숙대입구', '서울역', '회현', '명동', '충무로'],
['Sookmyung Women\'s University', 'Seoul Station', 'Hoehyeon', 'Myeong-dong',
'Chungmuro']]
line4_north = [
['동대문', '혜화', '한성대입구', '성신여대입구', '길음', '미아사거리', '미아', '수유',
'쌍문'],
['Dongdaemun', 'Hyehwa', 'Hansung University', 'Sungshin Women\'s University',
'Gireum', 'Miasageori', 'Mia', 'Suyu', 'Ssangmun']
]

seoul_districts = [
'종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구',
'도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
'영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'
]
nightbus_list = {
    '종로구':[
'N13: 노원 ~~ 동묘앞~동대문~광희동(동역사)~동대입구~약수~버티고개 ~~ 송파',
'N15: 우이동(강북) ~~ 동묘앞~동대문~종로3가~종각~을지로입구~서울역 ~~ 사당/남태령',
'N16: 도봉산 ~~ 혜화~동대문~광희동(동역사)~충무로~명동~회현~서울역~(시청역) ~~ 온수동(구로)',
'N26: 신내역(중랑) ~~ 동묘앞~동대문~종로3가~광화문~서대문 ~~ 강서',
'N30: 강동 ~~ 동묘앞~동대문~동역사~을지로~서울역',
'N37: 송파 ~~ 명동~종각~광화문~서대문 ~~ 진관동(은평)',
'N62: 양천 ~~ 시청~을지로입구~종각~종로3가~동대문~동역사~신당 ~~ 면목동(중랑)',
    ],
    '중구':[
'N13: 노원 ~~ 동묘앞~동대문~광희동(동역사)~동대입구~약수~버티고개 ~~ 송파',
'N15: 우이동(강북) ~~ 동묘앞~동대문~종로3가~종각~을지로입구~서울역 ~~ 사당/남태령',
'N16: 도봉산 ~~ 혜화~동대문~광희동(동역사)~충무로~명동~회현~서울역~(시청역) ~~ 온수동(구로)',
'N26: 신내역(중랑) ~~ 동묘앞~동대문~종로3가~광화문~서대문 ~~ 강서',
'N30: 강동 ~~ 동묘앞~동대문~동역사~을지로~서울역',
'N37: 송파 ~~ 명동~종각~광화문~서대문 ~~ 진관동(은평)',
'N62: 양천 ~~ 시청~을지로입구~종각~종로3가~동대문~동역사~신당 ~~ 면목동(중랑)',
    ],
    '용산구':[
'N13: 노원 ~~ 한강진~한남동 ~~ 송파',
'N15: 우이동(강북) ~~ 숙대입구(남영)~삼각지~용산역 ~~ 사당/남태령',
'N37: 송파 ~~ 한남동~한강진 ~~ 진관동(은평)',
    ],
    '성동구':[
'N30: 강동 ~~ 용답(장한평)~신답(답십리) ~~ 서울역',
'N61: 양천 ~~ 성수동 ~~ 노원',
'N62: 양천 ~~ 상왕십리~왕십리~한양대~뚝섬~성수 ~~ 면목동(중랑)',
    ],
    '광진구':[
'N30: 강동 ~~ 광나루~아차산~군자 ~~ 서울역',
'N61: 양천 ~~ 건대입구~어린이대공원(세종대)~군자~중곡동 ~~ 노원',
'N62: 양천 ~~ 건대입구~어린이대공원(세종대)~군자~중곡역 ~~ 면목동(중랑)',
    ],
    '동대문구':[
'N13: 노원 ~~ 이문동~외대~회기역~청량리~제기동~신설동 ~~ 송파',
'N26: 신내역(중랑) ~~ 휘경동~회기역~청량리~제기동~신설동 ~~ 강서',
'N30: 강동 ~~ 장한평~답십리~용신동(동대문구청)~신설동 ~~ 서울역',
    ],
    '중랑구':[
'N26: 신내역~망우~상봉역~중화동~중랑역 ~~ 강서',
'N61: 양천 ~~ 면목동~중화역~묵동(먹골역) ~~ 노원',
'N62: 양천 ~~ 용마산역~면목동(서일대앞)',
    ],
    '성북구':[
'N13: 노원 ~~ 석관동(석계역)~돌곶이역~석관동(한예종앞) ~~ 송파',
'N15: 우이동(강북) ~~ 길음동~길음역~돈암동~성신여대입구역~성북구청~보문 ~~ 사당/남태령',
'N16: 도봉산 ~~ 길음동~길음역~돈암동~성신여대입구역~한성대입구역 ~~ 온수동(구로)',
    ],
    '강북구':[
'N15: 북한산우이역 ~~ 도봉구 ~~ 수유~미아~송천동~미아사거리역 ~~ 사당/남태령',
'N16: 도봉산 ~~ 수유~미아~송천동~미아사거리역 ~~ 온수동(구로)',
    ],
    '도봉구':[
'N15: 우이동(강북) ~~ 방학동~쌍문동~쌍문역 ~~ 사당/남태령',
'N16: 도봉산역~도봉역~방학역~쌍문동~쌍문역 ~~ 온수동(구로)',
    ],
    '노원구':[
'N13: 노원역~중계~하계~공릉~태릉입구 ~~ 송파동',
'N61: 양천 ~~ 태릉입구~공릉~하계~중계~노원역',
    ],
    '은평구':[
'N37: 송파 ~~ 녹번~불광~연신내역~갈현동~구파발역~진관동~창릉동(고양시)',
    ],
    '서대문구':[
'N26: 신내역(중랑) ~~ 충정로역~아현역~이대역~신촌역 ~~ 강서',
'N37: 송파 ~~ 천연동(감신대앞)~독립문역~무악재역~홍제~홍은동 ~~진관동(은평)',
'N62: 양천 ~~ 신촌역~이대역~아현역~충정로역 ~~ 면목동(중랑)',
    ],
    '마포구':[
'N16: 도봉산 ~~ 공덕동~공덕역~마포역 ~~ 온수동(구로)',
'N26: 신내역(중랑) ~~ 홍대입구역~합정 ~~ 강서',
'N62: 양천 ~~ 합정~홍대입구역 ~~ 면목동(중랑)',
    ],
    '양천구':[
'N61: 양천공영차고지(신정) ~~ 노원',
'N62: 양천공영차고지(신정)~신월동~신정역~목동역~강서고앞~(등촌역~염창역) ~~ 면목동(중랑)',
'N65: 강서 ~~ 신정역~목동역~오목교역 ~~ 시흥동(금천)',
    ],
    '강서구':[
'N26: 신내역(중랑) ~~ 염창~등촌~발산역~마곡역~송정역~공항시장역~방화동~개화산역~개화역',
'N62: 양천 ~~ 등촌~염창 ~~ 면목동(중랑)',
'N65: 개화역~개화산역~신방화역~마곡나루역~발산역~우장산역~화곡~까치산역 ~~ 시흥동(금천)',
    ],
    '구로구':[
'N16: 도봉산 ~~ 신도림~구로역~고척돔구장~개봉~오류~온수',
'N61: 양천 ~~ 개봉동~개봉역~철산동(광명시)~구로동~가리봉동(디지털단지) ~~ 노원',
'N65: 강서 ~~ 신도림~구로동~(대림역) ~~ 시흥동(금천)',
    ],
    '금천구':[
'N65: 강서 ~~ 독산동~금천구청입구~시흥동',
    ],
    '영등포구':[
'N16: 도봉산 ~~ 여의도(여의동)~영등포역~문래동 ~~ 온수동(구로)',
'N26: 신내역(중랑) ~~ 당산역~선유도공원입구 ~~ 강서',
'N62: 양천 ~~ 선유도공원입구 ~~ 면목동(중랑)',
'N65: 강서 ~~ 양평동~영등포유통상가~영등포역~문래동 ~~ 시흥동(금천)',
    ],
    '동작구':[
'N15: 우이동(강북) ~~ 노들역~노량진역~장승배기역~신대방삼거리역 ~~ 사당/남태령',
'N61: 양천 ~~ 사당 ~~ 노원',
    ],
    '관악구':[
'N15: 우이동(강북) ~~ 보라매동~신림~봉천~서울대입구역~낙성대역~사당역~남태령역',
'N61: 양천 ~~ 조원동~신림~봉천~서울대입구역~낙성대역~사당역 ~~ 노원',
    ],
    '서초구':[
'N37: 송파 ~~ 양재(서초구청)~(강남역~신논현역~논현역~신사역) ~~ 진관동(은평)',
'N61: 양천 ~~ 방배동~방배역~예술의전당앞~남부터미널역~교대역 ~~ 노원',
    ],
    '강남구':[
'N13: 노원 ~~ 신사역~논현역~신논현역~강남역~역삼~선릉역~삼성 ~~ 송파',
'N37: 송파 ~~ 수서~일원~대모산입구역~학여울역~대치~도곡~매봉역~양재역~강남역~논현~신사 ~~ 진관동(은평)',
'N61: 양천 ~~ 강남역~역삼~선릉역~삼성~봉은사역~청담 ~~ 노원',
    ],
    '송파구':[
'N13: 노원 ~~ 종합운동장~잠실새내역~잠실~석촌~송파역~가락시장~문정~장지역~복정역~송파공영차고지(위례)',
'N37: 송파공영차고지(위례)~복정역~장지역~문정~가락시장 ~~ 진관동(은평)',
    ],
    '강동구':[
'N30: 강동공영차고지(강일)~상일동~고덕~명일~굽은다리역~길동~강동역~천호 ~~ 서울역',
    ],
}
subway_names = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선',
'8호선', '9호선', '분당선', '경의중앙선', '신분당선', '공항철도',
# '인천1호선', '인천2호선', '우이신설선', '경춘선', '수인선', '서해선', '용인경전철',
# '의정부경전철', '경강선'
]
toilet_list = {
    '1호선':[
'망월사', '도봉산', '도봉', '방학', '창동', '녹천', '월계', '석계(6호선)', '신이문',
'외대앞', '*동묘앞', '동대문(4호선)', '종로3가', '시청(2호선)', '서울역(공항철도)',
'*남영', '용산', '노량진(9호선)', '신길', '영등포', '신도림', '구로', '구일', '간석',
'*석수(신창행승강장)', '관악', '*명학(광운대행승강장)', '*금정', '화서', '수원'
    ],
    '2호선':[
'시청', '을지로3가', '동대문역사문화공원', '왕십리', '건대입구', '종합운동장', '강남',
'사당(4호선)', '신림', '신대방', '구로디지털단지', '(대림)', '신도림(1호선)',
'영등포구청', '당산', '홍대입구(공항철도)', '신답', '용두', '양천구청'
    ],
    '3호선':[
'대곡', '지축', '연신내', '무악재', '독립문', '경복궁', '종로3가', '을지로3가',
'충무로(4호선)', '동대입구', '약수', '금호', '옥수', '잠원', '고속터미널(9호선)',
'남부터미널', '양재', '대치', '대청', '가락시장', '경찰병원', '오금'
    ],
    '4호선':[
'상계', '노원', '창동', '성신여대입구', '동대문', '동대문역사문화공원', '충무로', '명동',
'회현', '서울역(공항철도)', '삼각지', '이촌', '동작', '이수', '사당', '남태령', '과천',
'정부과천청사', '*금정', '상록수', '한대앞', '중앙', '고잔', '초지(서해선)'
    ],
    '5호선':[
'김포공항(9호선,공항철도)', '신정', '양평', '영등포구청(2호선)', '신길(1호선)',
'여의도(9호선)', '공덕(공항철도)', '종로3가', '(동대문역사문화공원(4호선))',
'왕십리(2호선)', '오금'
    ],
    '6호선':[
'디지털미디어시티', '월드컵경기장', '삼각지(4호선)', '한강진', '약수(3호선)',
'동묘앞(1호선)', '창신', '안암', '고려대', '석계'
    ],
    '7호선':[
'도봉산', '상봉(경의중앙선,경춘선)', '*건대입구', '뚝섬유원지', '고속터미널(9호선)',
'이수', '남성', '대림(2호선)', '부천종합운동장', '부평구청'
    ],
    '8호선':[
'가락시장(3호선)'
    ],
    '9호선':[
'김포공항', '당산', '국회의사당', '*여의도', '샛강', '노량진', '동작', '고속터미널',
'종합운동장(2호선)'
    ],
    '분당선':[
'왕십리', '정자(신분당선)', '기흥', '수원'
    ],
    '경의중앙선':[
'대곡(3호선)', '디지털미디어시티(6호선)', '신촌', '홍대입구(공항철도)', '공덕(공항철도)',
'용산', '이촌', '서빙고', '옥수', '*응봉(용문행승강장)', '왕십리', '상봉'
    ],
    '신분당선':[
'강남', '양재', '양재시민의숲', '청계산입구', '판교', '정자'
    ],
    '공항철도':[
'서울역', '공덕', '홍대입구', '디지털미디어시티', '김포공항', '계양', '검암', '운서',
'공항화물청사'
    ]
}

MidnightServiceKakao = \
'''자정/심야시간 귀가안내
서비스를 이용해주셔서
감사합니다.

자정시간 귀가안내 서비스는
오후 11시 정각부터
익일 오전 12시 59분까지
운영됩니다.

출발지와 도착지를 알려주시면
현재 시간에 맞는
막차 경로들을
알려드리겠습니다.

(지하철막차, 일반버스,
심야버스, 단거리 택시 등)

아직 자동답변은
지원되지 않습니다.
'상담원으로 전환하기'
버튼을 눌러
상담원 채팅으로 전환한 다음

[ 출발지 / 목적지 ] 를
형식에 맞게 입력해주세요.
예) 청량리역 / 서울역

그리고 마음을
차분히 가라앉히고
잠시만 기다려주세요...'''

LatenightServiceKakao = \
'''자정/심야시간 귀가안내
서비스를 이용해주셔서
감사합니다.

오전 1시 정각부터
오전 4시 59분까지 운영되는
심야시간 귀가안내
서비스입니다.

심야시간대는
모든 지하철은 물론이고
버스까지 대부분 다 끊긴
시간대이기 때문에
택시거리를 줄여서
최대한 교통비를
절약하기 위해
최선을 다하겠습니다.

아직 자동답변은
지원되지 않습니다.
'상담원으로 전환하기'
버튼을 눌러
상담원 채팅으로 전환한 다음

[ 출발지 / 목적지 ] 를
형식에 맞게 입력해주세요.
예) 청량리역 / 서울역

그리고 마음을
차분히 가라앉히고
잠시만 기다려주세요...'''

MidnightUnavailableKakao = \
'''자정/심야시간 귀가안내
서비스를 이용해주셔서
감사합니다.

자정시간 귀가안내 서비스는
오후 11시 정각부터
익일 오전 12시 59분까지
운영되며,

심야시간 귀가안내 서비스는
오전 1시 정각부터
오전 4시 59분까지
운영됩니다.

지금은 자정/심야시간이
아닙니다.'''

MidnightAdvanceKakao = \
'''자정시간 귀가안내 서비스를
이용해주셔서 감사합니다.
자정~심야 시간대에 대한 귀가안내를
미리 확인하는 서비스입니다.
이 서비스는 24시간 언제든지
이용 가능하며,
오후 11시부터 오전 4시 사이의
심야시간에 어떻게 귀가할 것인지
미리 확인이 가능합니다.

아직 자동답변은 지원되지 않습니다.
'상담원으로 전환하기' 버튼을 눌러
상담원 채팅으로 전환한 다음

[ (자정 혹은 심야) / 출발지 / 목적지 ]
를 형식에 맞게 입력해주세요.
예) 심야 / 청량리역 / 신월동 우성상가

그리고 마음을 차분히 가라앉히고
잠시만 기다려주세요...'''

DHCPServiceKakao = \
'''7월 18일~9월 20일동안
5호선 동대문역사문화공원역
환승통로가 폐쇄되어

5호선에서 4호선,
4호선에서 5호선으로
환승하실 수 없습니다.

그래서,
5호선에서 4호선으로
환승하기 위해
동대문역사문화공원역을
이용하셨던 분들은
9월까지 우회해서
환승해야 합니다.

자정시간 귀가안내 서비스는
당황스러우셨던 여러분의
마음을 정리하고,
5호선-4호선 환승방법을
친절하게 안내해드리고자
노력하고 있습니다.

5호선 지하철역과
4호선 지하철역을
[ 5호선역 / 4호선역 ]
형식으로 알려주시면

동대문역사문화공원역
환승통로 폐쇄시의 경로를
자동으로 알려드리겠습니다.

예) 강동역 / 혜화역

(취소를 원하신다면
'취소'라고 입력해주세요)
'''

NightBusServiceKakao = \
'''자정시간 귀가안내 서비스를
이용해주셔서 감사합니다.

서울의 심야버스 알아보기
서비스입니다.

이 서비스를 통해
서울의 각 '구' 별로
어떤 심야버스가 다니고 있는지
확인할 수 있습니다.

당신이 거주하고 있는,
혹은 그 근처의
지역을 선택해주세요.
'''

PaidToiletServiceKakao = \
'''자정시간 귀가안내 서비스를
이용해주셔서 감사합니다.

수도권 지하철 노선에서
게이트 내(운임구역)
화장실이 있는 역을
알아보는 서비스입니다.

이 서비스를 통해
화장실이 급한 경우
돈을 더 지불하거나
비상 게이트를 여는 등의
수고를 하지 않아도 되는
지하철 화장실을 바로
알아볼 수 있습니다.

당신이 지금 타고 있거나
자주 이용하는 지하철 노선을
선택해주세요.
'''

PathNotFoundKakao = \
'''경로를 찾을 수 없습니다.
5호선 / 4호선 순서로 입력하셔야 합니다.

참고로 4호선은
숙대입구~쌍문 구간만 검색 가능합니다.
(동대문역사문화공원 제외)

다시 시도해주세요.'''

InvalidFormatKakao = \
'''출발지와 목적지를 형식에 맞게
다시 입력해주십시오:

[ 출발지 / 목적지 ]'''

ServiceErrorKakao = \
'''서비스에 에러가 발생했습니다.
다시 시도해주십시오.

1. 서비스를 실행시킨 후 종료하지 않고
10분 이상 경과하면 원래 메뉴로 돌아옵니다.
하지만 챗봇서버는 이를 인식하지 못해
에러가 발생합니다.

2. 메뉴가 표시되지 않을 경우,
채팅방에서 나간 후 다시 들어오십시오.'''

# 한글과 영어 플래그
KOR = 0
ENG = 1

def DHCP_guide(line5_station, line4_station):
    # 기본값 설정
    result = ['', '', '', '']  # 4가지의 지하철 환승 안내 결과 (Kor 2개, Eng 2개)
    is_line5_west = False      # 5호선 역의 서쪽 여부
    is_line5_east = False      # 5호선 역의 동쪽 여부
    line5_idx = -1             # 5호선 역의 인식 위치 인덱스
    is_line4_south = False     # 4호선 역의 남쪽 여부
    is_line4_north = False     # 4호선 역의 북쪽 여부
    line4_idx = -1             # 4호선 역의 인식 위치 인덱스

    # 5호선 서쪽 역 중에서 일치된 위치 찾기
    for lang in range(0, 2):
        for i in range(0, len(line5_west[lang])):
            if line5_west[lang][i] in line5_station:
                is_line5_west = True
                line5_idx = i
                break
        # 5호선 동쪽 역 중에서 일치된 위치 찾기
        for i in range(0, len(line5_east[lang])):
            if line5_east[lang][i] in line5_station:
                is_line5_east = True
                line5_idx = i
                break
        # 4호선 남쪽 역 중에서 일치된 위치 찾기
        for i in range(0, len(line4_south[lang])):
            if line4_south[lang][i] in line4_station:
                is_line4_south = True
                line4_idx = i
                break
        # 4호선 북쪽 역 중에서 일치된 위치 찾기
        for i in range(0, len(line4_north[lang])):
            if line4_north[lang][i] in line4_station:
                is_line4_north = True
                line4_idx = i
                break

    # 5호선 서/동, 4호선 북/남 중 어느 쪽에도 해당되지 않을 경우
    # 결과는 무효이므로 빈 칸이 된다.
    #
    if not (is_line5_west or is_line5_east) \
    or not (is_line4_south or is_line4_north):
        return ['', '', '', '']

    # 5호선은 서쪽 역이고 4호선이 남쪽 역일 경우
    if is_line5_west and is_line4_south:
        ##### 첫 번째 안내 #####
        # 5호선 역이 마곡역 또는 그 서쪽이면 김포공항역 환승으로 공항철도로 안내한다.
        if line5_idx <= line5_west[KOR].index('마곡'):
            # 만약 김포공항역이 아니면 5호선을 이용해야 하므로 ' - 5호선 - '을 추가.
            if line5_idx != line5_west[KOR].index('김포공항'):
                result[0] = line5_west[KOR][line5_idx] + ' - 5호선 - '
                result[2] = line5_west[ENG][line5_idx] + ' - Line5 - '
            result[0] += '김포공항 - 공항철도 - 서울역'
            result[2] += 'Gimpo International Airport - Airport Railroad'+ \
            ' - Seoul Station'
            # 만약 서울역이 아니면 4호선으로 환승해야 하므로 ' - 4호선 - '을 추가.
            if line4_idx != line4_south[KOR].index('서울역'):
                result[0] += ' - 4호선 - ' + line4_south[KOR][line4_idx]
                result[2] += ' - Line4 - ' + line4_south[ENG][line4_idx]
        # 5호선 역이 공덕보다 서쪽이면 공덕역 환승으로 6호선 삼각지로 안내한다.
        elif line5_idx < line5_west[KOR].index('공덕'):
            result[0] = line5_west[KOR][line5_idx]+ \
            ' - 5호선 - 공덕 - 6호선 - 삼각지 - 4호선 - '+ \
            line4_south[KOR][line4_idx]
            result[2] = line5_west[ENG][line5_idx]+ \
            ' - Line5 - Gongdeok - Line6 - Samgakji - Line4 - '+ \
            line4_south[ENG][line4_idx]
        # 5호선 역이 공덕역이면 '... - 5호선 - ...'을 생략한다.
        elif line5_idx == line5_west[KOR].index('공덕'):
            result[0] = '공덕 - 6호선 - 삼각지 - 4호선 - '+ \
            line4_south[KOR][line4_idx]
            result[2] = 'Gongdeok - Line6 - Samgakji - Line4 - '+ \
            line4_south[ENG][line4_idx]
        # 애오개~행당일 경우 종로3가역 환승으로 3호선 충무로로 안내한다.
        else:
            if line5_idx != line5_west[KOR].index('종로3가'):
                result[0] = line5_west[KOR][line5_idx]+' - 5호선 - '
                result[2] = line5_west[ENG][line5_idx]+' - Line5 - '
            result[0] += '종로3가 - 3호선 - 충무로'
            result[2] += 'Jongno 3-ga - Line3 - Chungmuro'
            if line4_idx != line4_south[KOR].index('충무로'):
                result[0] += ' - 4호선 - '+line4_south[KOR][line4_idx]
                result[2] += ' - Line4 - '+line4_south[ENG][line4_idx]

        ###### 두 번째 안내 #####
        # 5호선 서쪽역 위치 상관없이 2호선 을지로4가역으로 안내한다.
        if line5_idx != line5_west[KOR].index('을지로4가'):
            result[1] = line5_west[KOR][line5_idx]+' - 5호선 - '
            result[3] = line5_west[ENG][line5_idx]+' - Line5 - '
        result[1] += '을지로4가 - 2호선 - 동대문역사문화공원 - 4호선 - ' + \
        line4_south[KOR][line4_idx]
        result[3] += 'Euljiro 4-ga - Line2 - Dongdaemun History & Culture Park' + \
        ' - Line4 - ' + line4_south[ENG][line4_idx]

    # 5호선은 서쪽 역이고 4호선이 북쪽 역일 경우
    if is_line5_west and is_line4_north:
        ##### 첫 번째 안내 #####
        # 5호선 역이 마곡역 또는 그 서쪽이면 김포공항역 환승으로 공항철도로 안내한다.
        if line5_idx <= line5_west[KOR].index('마곡'):
            # 만약 김포공항역이 아니면 5호선을 이용해야 하므로 ' - 5호선 - '을 추가.
            if line5_idx != line5_west[KOR].index('김포공항'):
                result[0] = line5_west[KOR][line5_idx] + ' - 5호선 - '
                result[2] = line5_west[ENG][line5_idx] + ' - Line5 - '
            result[0] += '김포공항 - 공항철도 - 서울역 - 4호선 - ' + \
            line4_north[KOR][line4_idx]
            result[2] += 'Gimpo International Airport - Airport Railroad'+ \
            ' - Seoul Station - '+line4_north[ENG][line4_idx]
        # 5호선 역이 공덕보다 서쪽이면 공덕역 환승으로 6호선 삼각지로 안내한다.
        elif line5_idx < line5_west[KOR].index('공덕'):
            result[0] = line5_west[KOR][line5_idx]+ \
            ' - 5호선 - 공덕 - 6호선 - 삼각지 - 4호선 - '+line4_north[KOR][line4_idx]
            result[2] = line5_west[ENG][line5_idx]+ \
            ' - Line5 - Gongdeok - Line6 - Samgakji - Line4 - '+ \
            line4_north[ENG][line4_idx]
        elif line5_idx == line5_west[KOR].index('공덕'):  # 공덕역일 경우
            result[0] = '공덕 - 6호선 - 삼각지 - 4호선 - '+line4_north[KOR][line4_idx]
            result[2] = 'Gongdeok - Line6 - Samgakji - Line4 - '+ \
            line4_north[ENG][line4_idx]
        # 애오개~광화문이면 종로3가역 환승으로 3호선 충무로로 안내한다.
        elif line5_idx < line5_west[KOR].index('종로3가'):
            result[0] = line5_west[KOR][line5_idx]+ \
            ' - 5호선 - 종로3가 - 3호선 - 충무로 - 4호선 - '+ \
            line4_north[KOR][line4_idx]
            result[2] = line5_west[ENG][line5_idx]+ \
            ' - Line5 - Jongno 3-ga - Line3 - Chungmuro - Line4 - '+ \
            line4_north[ENG][line4_idx]
        elif line5_idx == line5_west[KOR].index('종로3가'):  # 종로3가역일 경우
            result[0] = '종로3가 - 3호선 - 충무로 - 4호선 - '+ \
            line4_north[KOR][line4_idx]
            result[2] = 'Jongno 3-ga - Line3 - Chungmuro - Line4 - '+ \
            line4_north[ENG][line4_idx]
        # 을지로4가~행당일 경우 4호선 북쪽 역의 위치에 따라 다르게 안내한다.
        else:
            # 동대문일 경우 1호선으로 안내한다.
            if line4_idx == line4_north[KOR].index('동대문'):
                if line5_idx != line5_west[KOR].index('종로3가'):
                    result[0] = line5_west[KOR][line5_idx]+' - 5호선 - '
                    result[2] = line5_west[ENG][line5_idx]+' - Line5 - '
                result[0] += '종로3가 - 1호선 - 동대문'
                result[2] += 'Jongno 3-ga - Line1 - Dongdaemun'
            # 혜화일 경우 100, 104번 버스로 안내한다.
            elif line4_idx == line4_north[KOR].index('혜화'):
                if line5_idx != line5_west[KOR].index('동대문역사문화공원'):
                    result[0] = line5_west[KOR][line5_idx]+' - 5호선 - '
                    result[2] = line5_west[ENG][line5_idx]+' - Line5 - '
                result[0] += '동대문역사문화공원 7번출구' + \
                ' - 을지로5가.훈련원종합체육관 정류장 - 100, 104 - 혜화'
                result[2] += 'Dongdaemun History & Culture Park [Exit 7]' + \
                ' - Euljiro 5-ga, Hullyeonwon Physical Plant [Bus Stop]' + \
                ' - 100, 104 - Hyehwa Station'
            else:  # 나머지 (한성대입구~쌍문), 100, 104번 버스로 안내한다.
                if line5_idx != line5_west[KOR].index('동대문역사문화공원'):
                    result[0] = line5_west[KOR][line5_idx]+' - 5호선 - '
                    result[2] = line5_west[ENG][line5_idx]+' - Line5 - '
                result[0] += '동대문역사문화공원 7번출구' + \
                ' - 을지로5가.훈련원종합체육관 정류장 - 100, 104 - 혜화 - 4호선 - '+ \
                line4_north[KOR][line4_idx]
                result[2] += 'Dongdaemun History & Culture Park [Exit 7]' + \
                ' - Euljiro 5-ga, Hullyeonwon Physical Plant [Bus Stop]' + \
                ' - 100, 104 - Hyehwa Station - Line4 - '+ \
                line4_north[ENG][line4_idx]

        ##### 두 번째 안내 #####
        # 5호선 서쪽역 위치 상관없이 2호선 을지로4가역으로 안내한다.
        if line5_idx != line5_west[KOR].index('을지로4가'):
            result[1] = line5_west[KOR][line5_idx]+' - 5호선 - '
            result[3] = line5_west[ENG][line5_idx]+' - Line5 - '
        result[1] += '을지로4가 - 2호선 - 동대문역사문화공원 - 4호선 - '+ \
        line4_north[KOR][line4_idx]
        result[3] += 'Euljiro 4-ga - Line2 - Dongdaemun History & Culture Park'+ \
        ' - Line4 - '+ line4_north[ENG][line4_idx]

    # 5호선은 동쪽 역이고 4호선이 남쪽 역일 경우
    if is_line5_east and is_line4_south:
        ##### 첫 번째 안내 #####
        # 5호선 동쪽역 위치에 상관없이 종로3가역 환승으로 3호선 충무로로 안내한다.
        result[0] = line5_east[KOR][line5_idx]+' - 5호선 - 종로3가 - 3호선 - 충무로'
        result[2] = line5_east[ENG][line5_idx]+' - Line5 - Jongno 3-ga - Line3'+ \
        ' - Chungmuro'
        if line4_idx != line4_south[KOR].index('충무로'):
            result[0] += ' - 4호선 - '+line4_south[KOR][line4_idx]
            result[2] += ' - Line4 - '+line4_south[ENG][line4_idx]

        ##### 두 번째 안내 #####
        # 5호선 동쪽역 위치에 상관없이 왕십리역 2호선으로 안내한다.
        if line5_idx != 0:  # 왕십리가 아닐 경우 ' - 5호선 - '을 붙인다.
            result[1] = line5_east[KOR][line5_idx]+' - 5호선 - '
            result[3] = line5_east[ENG][line5_idx]+' - Line5 - '
        result[1] += '왕십리 - 2호선 - 동대문역사문화공원 - 4호선 - ' + \
        line4_south[KOR][line4_idx]
        result[3] += 'Wangsimni - Line2 - Dongdaemun History & Culture Park'+ \
        ' - Line4 - ' + line4_south[ENG][line4_idx]

    # 5호선은 동쪽 역이고 4호선이 북쪽 역일 경우
    if is_line5_east and is_line4_north:
        ##### 첫 번째 안내 #####
        # 4호선 북쪽 어느 역인가에 따라 6호선 경유가 될 수도, 버스 경유가 될 수도 있다.
        if line4_idx == 0:  # 동대문역일 경우 6호선으로 안내
            result[0] = line5_east[KOR][line5_idx]+' - 5호선 - 청구 - 6호선' + \
            ' - 동묘앞 8번출구 - 동대문역까지 도보'
            result[2] = line5_east[ENG][line5_idx]+' - Line5 - Cheonggu' + \
            ' - Line6 - Dongmyo [Exit 8] - Work to the Dongdaemun station'
        else:  # 나머지는 버스 경유로 안내
            result[0] = line5_east[KOR][line5_idx]+ \
            ' - 5호선 - 동대문역사문화공원 7번출구 - 을지로5가.훈련원종합체육관 정류장' + \
            ' - 100, 104 - 혜화'
            result[2] = line5_east[ENG][line5_idx]+ \
            ' - Line5 - Dongdaemun History & Culture Park [Exit 7]' + \
            ' - Euljiro 5-ga, Hullyeonwon Physical Plant [Bus Stop]' + \
            ' - 100, 104 - Hyehwa Station'
            if line4_idx != 1:  # 혜화역이 아닐 경우 ' - 4호선 - '을 붙인다.
                result[0] += ' - 4호선 - '+line4_north[KOR][line4_idx]
                result[2] += ' - Line4 - '+line4_north[ENG][line4_idx]

        ##### 두 번째 안내 #####
        # 5호선 동쪽역 위치에 상관없이 왕십리역 2호선으로 안내한다.
        if line5_idx != 0:
            result[1] = line5_east[KOR][line5_idx]+' - 5호선 - '
            result[3] = line5_east[ENG][line5_idx]+' - Line5 - '
        result[1] += '왕십리 - 2호선 - 동대문역사문화공원 - 4호선 - '+ \
        line4_north[KOR][line4_idx]
        result[3] += 'Wangsimni - Line2 - Dongdaemun History & Culture Park' + \
        ' - Line4 - ' + line4_north[ENG][line4_idx]

    return result
