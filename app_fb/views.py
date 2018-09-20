from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import pprint
import requests
import datetime
from lib import *
# from .models import FacebookDHCPService
from django.core.exceptions import ObjectDoesNotExist
# tokens.py는 보안상 github에 업로드하지 않았다.
from tokens import PAGE_ACCESS_TOKEN, VERIFY_TOKEN

#### 데이터베이스 Databases ####
# MenuBtn: 메뉴 버튼 Dictionary 데이터
#

# 1번 메뉴 payload: report
# 2번 메뉴 payload: gohome
# 3번 메뉴 payload: dhcp_transfer
#
MenuBtn = {
    'recipient':{'id':''},
    'message':{
        'attachment':{
            'type':'template',
            'payload':{
                'template_type':'button',
                'text':
'''메뉴를 선택하세요...
Please select menu...

1. 문의하기
Contact us

2. 자정/심야시간 귀가안내 서비스 실행
Run Midnight Guide to Home Service
''',
                'buttons':[
                    {
                        'type':'postback',
                        'title':'1',
                        'payload':'contact'
                    },
                    {
                        'type':'postback',
                        'title':'2',
                        'payload':'gohome'
                    },
                ]
            }
        }
    }
}

#############************* 사용자 이름/프로필 얻어오기 *************############
# def user_get(fbid):
#     user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
#     user_details_params = {'fields':'first_name,last_name,profile_pic',
#         'access_token':PAGE_ACCESS_TOKEN}
#     user_details = requests.get(user_details_url, user_details_params).json()

#############************* 사용자에게 메시지 보내기 *************############
def post_facebook_message(fbid, response_message_json):
    post_message_url = \
        'https://graph.facebook.com/v2.6/me/messages?access_token=%s' \
        %PAGE_ACCESS_TOKEN
    response_message_json['recipient']['id'] = fbid
    response_msg = json.dumps(response_message_json)
    status = requests.post(post_message_url,
        headers={'Content-Type': 'application/json'}, data=response_msg)
    print('status: ' + str(status.json()))

###########*********** postback 메시지에 따라 메시지 보내기 ***********##########
def postback_message(fbid, payload):
    ###### 메뉴 선택 ######
    if payload == 'choose_menu':
        post_facebook_message(fbid, MenuBtn)

    ###### 제보 요청 ######
    if payload == 'contact':
        post_facebook_message(fbid, {
            'messaging_type': 'RESPONSE',
            'recipient':{'id':''},
            'message':{'text':'문의사항을 말씀해주시면 친절하게 답변해드리겠습니다.\n'+ \
                'If you have any questions, we will reply kindly.'}
        })

    ###### 자정/심야시간 귀가안내 서비스 실행 ######
    if payload == 'gohome':
        now = datetime.datetime.now()  # 현재 시각 불러오기
        if now.hour == 23 or now.hour == 0:  # 오후 11시~(익일)자정 여부
            post_facebook_message(fbid, {
                'messaging_type': 'RESPONSE',
                'recipient':{'id':''},
                'message':{'text':
'''자정/심야시간 귀가안내 서비스를 이용해주셔서 감사합니다.
자정시간 귀가안내 서비스는 오후 11시 정각부터 익일 오전 12시 59분(한국시간)까지 운영됩니다.

출발지와 도착지를 알려주시면
현재 시간에 맞는 막차 경로(들)을 알려드리겠습니다.
(지하철막차, 일반버스, 심야버스, 단거리 택시 등)

출발지 / 목적지를 입력해주세요.
예) 청량리역 / 서울역

그리고 마음을 차분히 가라앉히고
잠시만 기다려주세요...

Thank you for using the Midnight Guide to Home Service.
It is the guide service for midnight time, available at 11:00 PM ~ 12:59 AM (KST).

If you send me your starting point and destination,
then we will inform you the possible path(s) to go home.
(Last Train, Normal Buses, Midnight Buses, Short-path Taxi, etc.)

Please send me your starting point / destination.
Ex) Cheongnyangni Station / Seoul Station

Calm down slowly, and wait for a moment...'''
                }
            })
        elif now.hour >= 1 and now.hour <= 4:  # 오전 1시~4시 여부
            post_facebook_message(fbid, {
                'messaging_type': 'RESPONSE',
                'recipient':{'id':''},
                'message':{'text':
'''자정/심야시간 귀가안내 서비스를 이용해주셔서 감사합니다.
오전 1시 정각부터 오전 4시 59분(한국시간)까지 운영되는 심야시간 귀가안내 서비스입니다.
심야시간대는 모든 지하철은 물론이고 버스까지 대부분 다 끊긴 시간대이기 때문에
택시거리를 줄여 최대한 교통비를 절약하기 위해 최선을 다하겠습니다.

출발지 / 목적지를 입력해주세요.
예) 청량리역 / 서울역

그리고 마음을 차분히 가라앉히고
잠시만 기다려주세요...

Thank you for using the Midnight Guide to Home Service.
It is the guide service for late-night time, available at 1:00 ~ 4:59 AM (KST).
At the late-night time, not only all subways but also buses are mostly disconnected,
so we will do our best to reduce the taxi distance as much as possible.

Please send me your starting point / destination.
Ex) Cheongnyangni Station / Seoul Station

Calm down slowly, and wait for a moment...'''
                }
            })
        else:  # 이 외의 시간에는 요청 거부를 한다.
            post_facebook_message(fbid, {
                'messaging_type': 'RESPONSE',
                'recipient':{'id':''},
                'message':{'text':
'''자정/심야시간 귀가안내 서비스를 이용해주셔서 감사합니다.
자정시간 귀가안내 서비스는 오후 11시 정각부터 익일 오전 12시 59분(한국시간)까지 운영되며,
심야시간 귀가안내 서비스는 오전 1시 정각부터 오전 4시 59분(한국시간)까지 운영됩니다.

지금은 자정/심야시간이 아닙니다.

Thank you for using the Midnight Guide to Home Service.
The guide service for midnight time is available at 11:00 PM ~ 12:59 AM (KST),
and the service for late-night time is available at 1:00 ~ 4:59 AM (KST).

It is not midnight or late-night time yet.'''
                }
            })

"""
    ###### 동대문역사문화공원역 5호선-4호선 환승방법 안내 실행 ######
    if payload == 'dhcp_transfer':
        cur_dhcp = FacebookDHCPService.objects.get(fbid=fbid)
        cur_dhcp.status = True  # 요청 상태: On
        cur_dhcp.save()  # 데이터베이스 반영
        post_facebook_message(fbid, {
            'messaging_type': 'RESPONSE',
            'recipient':{'id':''},
            'message':{'text':
'''7월 18일~10월 31일동안 5호선 동대문역사문화공원역 환승통로가 폐쇄되어
5호선에서 4호선, 4호선에서 5호선으로 환승하실 수 없습니다.
그래서 5호선에서 4호선으로 환승하려고 동대문역사문화공원역을 이용하셨던 분들은
10월까지 우회해서 환승해야 합니다.

자정시간 귀가안내 서비스는 당황스러우셨던 여러분의 마음을 정리하고, 5호선-4호선 환승방법을
친절하게 안내해드리고자 노력하고 있습니다.

5호선 지하철역과 4호선 지하철역을 알려주시면 동대문역사문화공원역 환승통로 폐쇄시의 경로를
알려드리겠습니다.
예) 강동역 / 혜화역

(반드시 5호선역 / 4호선역 순서로 입력하셔야 합니다.)

During the period from July 18 to October 31, the passage to the Seoul Metro
Dongdaemun History & Culture Park on Line 5 is closed.
You can not transfer from Line 5 to Line 4, and Line 4 to Line 5.
So those who used Dongdaemun History & Culture Park Station have to transfer
to bypass until October.

The Midnight Guide to Home Service will organize your minds who are embarrassed,
we are trying to guide you kindly.

If you inform me the subway station of line 5 and of line 4,
I will let you know how to transfer.
Ex) 강동역 (Gangdong Station) / 혜화역 (Hyehwa Station)

(You must enter in the order of line 5 / line 4.)'''}
        })
"""

#########********* 페이스북으로부터 요청을 받을 때 처리하는 class *********########
class BotView(generic.View):
    ###### get 요청 (토큰 검증) ######
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    ###### dispatch override ######
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    ###### post 요청 (메시지 처리) ######
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        # 페이스북 서버로부터 받은 JSON request에서 메시지를 추출한다.
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                """
                # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 불러온다.
                try:
                    cur_dhcp = FacebookDHCPService.objects.get(
                        fbid=message['sender']['id']
                    )
                except ObjectDoesNotExist:
                    cur_dhcp = FacebookDHCPService.objects.create(
                        fbid=message['sender']['id'], status=False
                    )
                    cur_dhcp.save()  # 데이터베이스 반영
                """
                # 일반적인 사용자의 message 양식
                if 'message' in message:
                    print('message: ' + str(message))  # 디버그용

                    """
                    # 만약 동대문역사문화공원역 5호선-4호선 환승방법 안내 요청이 On이고
                    # 메시지 내용에 슬래시(/)가 포함되어 있으면
                    # 올바른 안내 요청을 한 것으로 승인한다.
                    #
                    if cur_dhcp.status and '/' in message['message']['text']:
                        # 요청이 승인되었으므로 Off한다.
                        cur_dhcp.status = False
                        cur_dhcp.save()

                        # 환승안내를 통해 응답받은 '5호선 / 4호선' 역명을 슬래시로 분리하여
                        # splited[0]에 5호선역, splited[1]에 4호선역이 대입된다.
                        #
                        splited = message['message']['text'].split('/')
                        splited[0] = splited[0].strip()   # line5
                        splited[1] = splited[1].strip()   # line4

                        result = DHCP_guide(splited[0], splited[1])

                        # 경로 찾기 결과가 둘 중 하나가 빈 칸일 경우
                        # '경로를 찾을 수 없다'고 메시지를 보낸다.
                        #
                        if result[0] == '':
                            post_facebook_message(message['sender']['id'], {
                                'messaging_type': 'RESPONSE',
                                'recipient':{'id':''},
                                'message':{'text':
'''경로를 찾을 수 없습니다. 5호선 / 4호선 순서로 입력하셔야 합니다.
참고로 4호선은 숙대입구~쌍문 (동대문역사문화공원 제외) 구간만 검색 가능합니다.

Transfer path not found. Line 5 / Line 4 must be entered in order.
For reference, line 4 can only be searched for sections of
Sookmyung Women's University (숙대입구) ~ Ssangmun (쌍문)
(excluding Dongdaemun History & Culture Park).'''}
                            })
                        else:
                            # 성공적으로 경로 2가지를 찾았으면 2가지 경로를 메시지로 보낸다.
                            post_facebook_message(message['sender']['id'], {
                                'messaging_type': 'RESPONSE',
                                'recipient':{'id':''},
                                'message':{'text':'출발지는 '+splited[0]+ \
                                    '(이)고, 목적지는 '+splited[1]+ \
                                    '(으)로 요청하셨습니다.\n'+ \
                                    '5호선에서 4호선으로 환승하는 2가지 방법은:\n\n'+ \
                                    '1. '+result[0]+'\n\n2. '+result[1]+'\n\n'+ \
                                    'Your request: starting point is '+splited[0]+ \
                                    ', and destination is '+splited[1]+'.\n'+ \
                                    'There are two ways to transfer '+ \
                                    'from Line 5 to Line 4:\n\n'+ \
                                    '1. '+result[2]+'\n\n2. '+result[3]
                                }
                            })

                    # 자동화된 코드에서 형식에 맞지 않게 입력했을 경우
                    if cur_dhcp.status:
                        post_facebook_message(message['sender']['id'], {
                            'messaging_type': 'RESPONSE',
                            'recipient':{'id':''},
                            'message':{'text':
'''출발지와 목적지를 형식에 맞게 다시 입력해주십시오:
출발지 / 목적지

Please re-enter the starting point and destination according to the format:
Starting point / Destination'''}
                        })
                    """
                    # '메뉴'를 입력했으면 메뉴를 띄워준다.
                    if message['message']['text'] == '메뉴' or \
                    message['message']['text'] == 'menu':
                        postback_message(message['sender']['id'], 'choose_menu')

                # postback 요청
                if 'postback' in message:
                    print('postback: ' + str(message))
                    postback_message(message['sender']['id'],
                        message['postback']['payload'])

        return HttpResponse()
