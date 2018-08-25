#################### 데이터베이스 Databases ####################
# line5_west: 5호선 서쪽 지역의 역명 (방화~행당)
# line5_east: 5호선 동쪽 지역의 역명 (왕십리~상일동/마천)
# line4_south: 4호선 동대문역사문화공원역 기준 남부 지역의 역명 (숙대입구~충무로)
# line4_north: 4호선 동대문역사문화공원역 기준 북부 지역의 역명 (동대문~쌍문)
# MidnightServiceKakao: 카카오톡 플러스친구 자정시간 귀가안내 서비스 안내 메시지
# LatenightServiceKakao: 카카오톡 플러스친구 심야시간 귀가안내 서비스 안내 메시지
# MidnightUnavailableKakao: 자정시간 귀가안내 서비스 불가 메시지
# MidnightAdvanceKakao: 카카오톡 플러스친구 자정시간 귀가안내 미리확인 메시지
# DHCPServiceKakao: 카카오톡 플러스친구 5호선 - 4호선 환승방법 안내 메시지
# PathNotFoundKakao: 카카오톡 플러스친구 환승 경로를 찾을 수 없을 때 나오는 메시지
# InvalidFormatKakao: 카카오톡 플러스친구 환승 경로 형식을 잘못 입력했을때 나오는 메시지
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
'''7월 18일~10월 31일동안
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
10월까지 우회해서
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
