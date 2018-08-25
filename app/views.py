# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import KakaoDHCPService
import json
import datetime
from lib import *

#### 데이터베이스 Databases ####
# default_menu_btn: 카카오톡 메뉴 버튼에 사용되는 변수형 데이터
#
default_menu_btn = ['자정/심야시간 귀가안내', '자정/심야시간 귀가안내 미리 확인',
'5호선 - 4호선 환승방법 안내', '서비스 이용 규칙', '서울 1~9호선 통학통근러 오픈채팅방']

#################***************** 키보드 요청시 *****************################
@csrf_exempt
def keyboard(response):
    return JsonResponse({
        'type': 'buttons',
        'buttons': default_menu_btn
    })

#################***************** 챗봇 메시지 *****************#################
@csrf_exempt
def message(request):
    # 카카오 서버로부터 받은 JSON request에서 데이터를 추출한다.
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)  # JSON 파일 디코딩
    content_name = received_json['content']

    user_name = received_json['user_key']
    # user_name은 사용자를 구별하기 위해 사용됨
    # type_name = received_json['type']
    # type_name은 사용자가 보낸 값의 속성을 구별(text, photo 등)

    # 메시지를 메뉴 버튼 리스트에 대응하여 인덱스를 찾기
    # 찾지 못하면 -1이 된다.
    #
    try:
        menu_idx = default_menu_btn.index(content_name)
    except ValueError:
        menu_idx = -1

    # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 불러온다.
    try:
        cur_dhcp = KakaoDHCPService.objects.get(user=user_name)
        cur_dhcp.save()  # updated_time 현재 시각 동기화
    except ObjectDoesNotExist:
        cur_dhcp = KakaoDHCPService.objects.create(user=user_name)
        cur_dhcp.save()

    ################# 자정/심야시간 귀가안내 #################
    if menu_idx == 0:
        now = datetime.datetime.now()  # 현재 시각 불러오기
        if now.hour == 23 or now.hour == 0:  # 오후 11시~(익일)자정 여부
            return JsonResponse({
                'message': {
                    'text': MidnightServiceKakao,
                    'photo': {
                        # url form: http://<host>/static/Response_Input.png
                        'url': 'http://' + request.get_host() + \
                        '/static/Response_Input.png',
                        'width': 1058,
                        'height': 794
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['상담 취소/완료']
                }
            })
        elif now.hour >= 1 and now.hour <= 4:  # 오전 1시~4시 여부
            return JsonResponse({
                'message': {
                    'text': LatenightServiceKakao,
                    'photo': {
                        # url form: http://<host>/static/Response_Input.png
                        'url': 'http://' + request.get_host() + \
                        '/static/Response_Input.png',
                        'width': 1058,
                        'height': 794
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['상담 취소/완료']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': MidnightUnavailableKakao,
                    'photo': {
                        # url form:
                        # http://<host>/static/Response_Unavailable.png
                        #
                        'url': 'http://' + request.get_host() + \
                        '/static/Response_Unavailable.png',
                        'width': 1058,
                        'height': 794
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })

    ################# 자정/심야시간 귀가안내 미리 확인 #################
    elif menu_idx == 1:
        return JsonResponse({
            'message': {
                'text': MidnightAdvanceKakao
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['상담 취소/완료']
            }
        })

    ################# 5호선 - 4호선 환승방법 안내 #################
    elif menu_idx == 2:
        cur_dhcp.status = True
        cur_dhcp.save()
        return JsonResponse({
            'message': {
                'text': DHCPServiceKakao,
                'photo': {
                    # url form: http://<host>/static/DHCP_Transfer.jpg
                    'url': 'http://' + request.get_host() + \
                    '/static/DHCP_Transfer.jpg',
                    'width': 1266,
                    'height': 1775
                }
            },
            'keyboard': {
                'type': 'text'
            }
        })

    ################# 서비스 이용 규칙 #################
    elif menu_idx == 3:
        return JsonResponse({
            'message': {
                'text': '서비스 이용 규칙입니다.',
                'message_button': {
                    "label": "바로가기",
                    "url": "http://pf.kakao.com/_GskxcC/21769650"
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    ################# 통학통근러 오픈채팅방 #################
    elif menu_idx == 4:
        return JsonResponse({
            'message': {
                'text': '서울 1~9호선 통학통근러 오픈채팅방',
                'message_button': {
                    "label": "바로가기",
                    "url": "https://open.kakao.com/o/gY4BH4v"
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    ################# 귀가 안내 취소 혹은 완료시 #################
    elif content_name == '상담 취소/완료':
        return JsonResponse({
            'message': {
                'text': '서비스가 종료되었습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    ################# 5호선 - 4호선 환승안내 자동화 코드 #################
    elif cur_dhcp.status and '/' in content_name:
        # 현재 사용자의 요청을 받아들인다. (Reset)
        cur_dhcp.status = False
        cur_dhcp.save()

        # 환승안내를 통해 응답받은 '5호선 / 4호선' 역명을 슬래시로 분리하여
        # splited[0]에 5호선역, splited[1]에 4호선역이 대입된다.
        #
        splited = content_name.split('/')
        splited[0] = splited[0].strip()   # line5
        splited[1] = splited[1].strip()   # line4

        result = DHCP_guide(splited[0], splited[1])

        # 경로 찾기 결과가 둘 중 하나가 빈 칸일 경우
        # '경로를 찾을 수 없다'고 메시지를 보낸다.
        #
        if result[0] == '':
            return JsonResponse({
                'message': {
                    'text': PathNotFoundKakao
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })

        # 성공적으로 경로 2가지를 찾았으면 2가지 경로를 메시지로 보낸다.
        return JsonResponse({
            # (예시: 강동역 / 혜화역)
            # 출발지는 강동역(이)고,
            # 목적지는 혜화역(으)로 요청하셨습니다.
            #
            # 5호선에서 4호선으로 환승하는
            # 2가지 방법은:
            #
            # 1. 강동 - 5호선 - 동대문역사문화공원
            # 7번출구 - 을지로5가......
            #
            # 2. 강동 - 5호선 - 왕십리 - 2호선 -
            # 동대문역사문화공원 - 4호선 - 혜화
            #
            'message': {
                'text': '출발지는 '+splited[0]+'(이)고,\n목적지는 '+splited[1]+ \
                '(으)로 요청하셨습니다.\n\n'+ \
                '5호선에서 4호선으로 환승하는\n2가지 방법은:\n\n'+ \
                '1. '+result[0]+'\n\n2. '+result[1]
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    ################# 자동화된 코드에서 형식에 맞지 않게 입력했을 경우 #################
    elif cur_dhcp.status:  # 현재 사용자의 DHCP 안내가 True일 경우
        if '취소' in content_name:  # 취소 요청시
            # 현재 사용자의 요청을 취소시킨다. (Reset)
            cur_dhcp.status = False
            cur_dhcp.save()
            return JsonResponse({
                'message': {
                    'text': '취소되었습니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': InvalidFormatKakao
                },
                'keyboard': {
                    'type': 'text'
                }
            })

    ################# 나머지 #################
    else:
        return JsonResponse({
            'message': {
                'text': '잘못된 입력입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

###############*************** 친구 추가/차단 알림 ***************###############
@csrf_exempt
def friend_add(request):
    # 카카오 서버로부터 받은 JSON request에서 데이터를 추출한다.
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)  # JSON 파일 디코딩
    user_name = received_json['user_key']  # 사용자 키

    # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 아무런 동작을 하지 않는다.
    try:
        cur_dhcp = KakaoDHCPService.objects.get(user=user_name)
    except ObjectDoesNotExist:
        cur_dhcp = KakaoDHCPService.objects.create(user=user_name, status=False)
        cur_dhcp.save()
    return HttpResponse()

@csrf_exempt
def friend_block(request, user_key):
    if request.method == 'DELETE':
        # 사용자 키가 데이터베이스에 없다면 아무런 동작을 하지 않고, 있으면 삭제한다.
        try:
            cur_dhcp = KakaoDHCPService.objects.get(user=user_key)
            cur_dhcp.delete()
        except ObjectDoesNotExist:
            pass
    return HttpResponse()

###############*************** 채팅방 나가기 알림 ***************###############
@csrf_exempt
def friend_leave(request, user_key):
    if request.method == 'DELETE':
        # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 기본값으로 변경한다.
        try:
            cur_dhcp = KakaoDHCPService.objects.get(user=user_key)
            cur_dhcp.status = False
            cur_dhcp.save()
        except ObjectDoesNotExist:
            cur_dhcp = KakaoDHCPService.objects.create(user=user_key, status=False)
            cur_dhcp.save()
    return HttpResponse()

#################***************** 이미지 로딩 *****************#################
def image_load(request, image_name):
    link = image_name

    # 이미지를 read binary로 불러오고 http로 전송한다.
    images = []
    image_data_ = open(link, "rb").read()
    images.append(image_data_)

    return HttpResponse(images, content_type="image/jpg")
