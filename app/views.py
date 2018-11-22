# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# from django.template import loader
from .models import KakaoService, WebGuideRequests, WebGuideReplies
import json
import datetime
from static_lib import *
# tokens.py는 보안상 github에 업로드하지 않았다.
from tokens import ACCESS_USER_AGENT

#### 데이터베이스 Databases ####
# default_menu_btn: 카카오톡 메뉴 버튼에 사용되는 변수형 데이터
#
default_menu_btn = ['자정/심야시간 귀가안내', '자정/심야시간 귀가안내 미리 확인',
'서울 심야버스 알아보기', '지하철 운임구역 화장실 알아보기', '서비스 이용 규칙',
'개인정보 처리방침', '서울 1~9호선 통학통근러 오픈채팅방']

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
    # 카카오톡 봇 외의 다른 User Agent의 진입을 차단
    if not ACCESS_USER_AGENT in request.META['HTTP_USER_AGENT']:
        return JsonResponse({
            'message': {
                'text': '올바른 카카오톡 챗봇 요청이 아닙니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    # 올바른 POST 요청이 맞는지 검증
    if request.method != 'POST':
        return HttpResponse('Wrong request.')

    # 카카오 서버로부터 받은 JSON request에서 데이터를 추출한다.
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)  # JSON 파일 디코딩

    try:
        # content_name은 요청된 메시지 판별에 사용됨
        content_name = received_json['content']
        # user_name은 사용자를 구별하기 위해 사용됨
        user_name = received_json['user_key']
        # type_name은 사용자가 보낸 값의 속성을 구별(text, photo 등)
        type_name = received_json['type']
    except KeyError:
        return JsonResponse({
            'message': {
                'text': 'JSON 형식이 잘못되었습니다. 다시 시도해주십시오.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    # 메시지를 메뉴 버튼 리스트에 대응하여 인덱스를 찾기
    # 찾지 못하면 -1이 된다.
    #
    try:
        menu_idx = default_menu_btn.index(content_name)
    except ValueError:
        menu_idx = -1

    # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 불러온다.
    try:
        cur_serv = KakaoService.objects.get(user=user_name)
        cur_serv.save()  # updated_time 현재 시각 동기화
    except ObjectDoesNotExist:
        cur_serv = KakaoService.objects.create(user=user_name)
        cur_serv.save()

    # 사용자가 보낸 값이 텍스트가 아니라면
    if type_name != 'text':
        # cur_serv.dhcp_status = False
        cur_serv.nightbus_status = False
        cur_serv.paidtoilet_status = False
        cur_serv.save()
        return JsonResponse({
            'message': {
                'text': '챗봇은 텍스트 형식으로만 반응할 수 있습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    '''
    ################# 5호선 - 4호선 환승안내 자동화 코드 #################
    if cur_serv.dhcp_status:
        # 출발지 / 목적지 형식으로 입력했다면...
        if '/' in content_name:
            # 현재 사용자의 요청을 받아들인다. (Reset)
            cur_serv.dhcp_status = False
            cur_serv.save()

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
                    'text': '출발지는 '+splited[0]+'(이)고,\n목적지는 '+ \
                    splited[1]+'(으)로 요청하셨습니다.\n\n'+ \
                    '5호선에서 4호선으로 환승하는\n2가지 방법은:\n\n'+ \
                    '1. '+result[0]+'\n\n2. '+result[1]
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 취소 요청시
        elif '취소' in content_name:
            # 현재 사용자의 요청을 취소시킨다. (Reset)
            cur_serv.dhcp_status = False
            cur_serv.save()
            return JsonResponse({
                'message': {
                    'text': '요청이 취소되었습니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 자동화된 코드에서 형식에 맞지 않게 입력했을 경우
        else:
            return JsonResponse({
                'message': {
                    'text': InvalidFormatKakao
                },
                'keyboard': {
                    'type': 'text'
                }
            })
    '''
    ################# 서울 심야버스 알아보기 자동화 코드 #################
    if cur_serv.nightbus_status:
        # 입력값이 서울 자치구를 선택했다면...
        if content_name in seoul_districts:
            # 현재 사용자의 요청을 받아들인다. (Reset)
            cur_serv.nightbus_status = False
            cur_serv.save()

            # (예시: 서초구)
            # 서초구를 지나는 서울 심야버스는
            # 다음과 같습니다:
            #
            # N37: 송파 ~~ 양재(서초구청)~(강남역~신논현역~논현역~신사역) ~~ 진관동(은평)
            #
            # N61: 양천 ~~ 방배동~방배역~예술의전당앞~남부터미널역~교대역 ~~ 노원
            #
            # 더 자세한 심야버스 정보를 알고 싶으시다면:
            # http://pf.kakao.com/_GskxcC/27592053
            #
            result_text = content_name + '를 지나는 서울 심야버스는\n'+ \
            '다음과 같습니다:\n\n'

            for bus in nightbus_list[content_name]:
                result_text += bus + '\n\n'

            result_text += '더 자세한 심야버스 정보를 알고 싶으시다면: ' + \
            "http://pf.kakao.com/_GskxcC/27592053"

            # 응답 전송
            return JsonResponse({
                'message': {
                    'text': result_text
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 취소 버튼을 선택했다면...
        elif '취소' in content_name:
            # 현재 사용자의 요청을 취소시킨다. (Reset)
            cur_serv.nightbus_status = False
            cur_serv.save()
            return JsonResponse({
                'message': {
                    'text': '요청이 취소되었습니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 취소 버튼이 아니면 에러를 띄운다.
        else:
            # cur_serv.dhcp_status = False
            cur_serv.nightbus_status = False
            cur_serv.paidtoilet_status = False
            cur_serv.save()
            return JsonResponse({
                'message': {
                    'text': ServiceErrorKakao
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })

    ################# 지하철 운임구역 화장실 알아보기 자동화 코드 #################
    elif cur_serv.paidtoilet_status:
        # 입력값이 지하철 노선을 선택했다면...
        if content_name in subway_names:
            # 현재 사용자의 요청을 받아들인다. (Reset)
            cur_serv.paidtoilet_status = False
            cur_serv.save()

            # (예시: 2호선)
            # 2호선 운임구역 내에 화장실이 있는 역의 목록입니다.
            #
            # * 승강장에 화장실이 있음
            # ? 운임구역에 있는지 불확실함.
            # (확실하면 건의해주시기 바랍니다.)
            #
            # 역 이름 옆에 (1호선)처럼 타 노선이 붙어있는 경우는
            # 화장실에 들어가기 위해 환승이 요구되는 역입니다.
            #
            # 시청  을지로3가  동대문역사문화공원  ...
            #
            result_text = content_name + \
            ' 운임구역 내에 화장실이 있는 역의 목록입니다.\n\n'
            result_text += '* 승강장에 화장실이 있음\n? 운임구역에 있는지 불확실함\n'
            result_text += '(확실하면 건의해주시기 바랍니다.)\n\n'
            result_text += '역 이름 옆에 (1호선)처럼 타 노선이 붙어있는 경우는 '
            result_text += '화장실에 들어가기 위해 환승이 요구되는 역입니다.\n\n--\n\n'

            for station in toilet_list[content_name]:
                result_text += station + '  '

            # 응답 전송
            return JsonResponse({
                'message': {
                    'text': result_text
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 취소 버튼을 선택했다면...
        elif '취소' in content_name:
            # 현재 사용자의 요청을 취소시킨다. (Reset)
            cur_serv.paidtoilet_status = False
            cur_serv.save()
            return JsonResponse({
                'message': {
                    'text': '요청이 취소되었습니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })
        # 취소 버튼이 아니면 에러를 띄운다.
        else:
            # cur_serv.dhcp_status = False
            cur_serv.nightbus_status = False
            cur_serv.paidtoilet_status = False
            cur_serv.save()
            return JsonResponse({
                'message': {
                    'text': ServiceErrorKakao
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': default_menu_btn
                }
            })


    ################# 자정/심야시간 귀가안내 #################
    elif menu_idx == 0:
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
        '''
    ################# 5호선 - 4호선 환승방법 안내 #################
    elif menu_idx == 2:
        cur_serv.dhcp_status = True
        cur_serv.save()
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
        '''

    ################# 서울 심야버스 알아보기 #################
    elif menu_idx == 2:
        cur_serv.nightbus_status = True
        cur_serv.save()
        return JsonResponse({
            'message': {
                'text': NightBusServiceKakao,
                'photo': {
                    # url form: http://<host>/static/Seoul_Nightbus.png
                    'url': 'http://' + request.get_host() + \
                    '/static/Seoul_Nightbus.png',
                    'width': 1000,
                    'height': 796
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': seoul_districts+['취소']
            }
        })

    ################# 지하철 운임구역 화장실 알아보기 #################
    elif menu_idx == 3:
        cur_serv.paidtoilet_status = True
        cur_serv.save()
        return JsonResponse({
            'message': {
                'text': PaidToiletServiceKakao,
                'photo': {
                    # url form:
                    # http://<host>/static/Toilet.jpg
                    #
                    'url': 'http://' + request.get_host() + \
                    '/static/Toilet.jpg',
                    'width': 720,
                    'height': 960
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': subway_names+['취소']
            }
        })

    ################# 서비스 이용 규칙 #################
    elif menu_idx == 4:
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

    ################# 개인정보 처리방침 #################
    elif menu_idx == 5:
        return JsonResponse({
            'message': {
                'text': '개인정보 처리방침입니다.',
                'message_button': {
                    "label": "바로가기",
                    "url": "http://pf.kakao.com/_GskxcC/28278836"
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

    ################# 통학통근러 오픈채팅방 #################
    elif menu_idx == 6:
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

    ################# 나머지 #################
    else:
        return JsonResponse({
            'message': {
                'text': ServiceErrorKakao
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': default_menu_btn
            }
        })

###############*************** 친구 추가/차단 알림 ***************###############
@csrf_exempt
def friend_add(request):
    # 카카오톡 봇 외의 다른 User Agent의 진입을 차단
    if not ACCESS_USER_AGENT in request.META['HTTP_USER_AGENT']:
        return HttpResponse('This service is only accessable on KakaoTalk bot.')

    # 카카오 서버로부터 받은 JSON request에서 데이터를 추출한다.
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)  # JSON 파일 디코딩
    user_name = received_json['user_key']  # 사용자 키

    # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 아무런 동작을 하지 않는다.
    try:
        cur_serv = KakaoService.objects.get(user=user_name)
    except ObjectDoesNotExist:
        cur_serv = KakaoService.objects.create(user=user_name)
        cur_serv.save()
    return HttpResponse()

@csrf_exempt
def friend_block(request, user_key):
    # 카카오톡 봇 외의 다른 User Agent의 진입을 차단
    if not ACCESS_USER_AGENT in request.META['HTTP_USER_AGENT']:
        return HttpResponse('This service is only accessable on KakaoTalk bot.')

    if request.method == 'DELETE':
        # 사용자 키가 데이터베이스에 없다면 아무런 동작을 하지 않고, 있으면 삭제한다.
        try:
            cur_serv = KakaoService.objects.get(user=user_key)
            cur_serv.delete()
        except ObjectDoesNotExist:
            pass
    return HttpResponse()

###############*************** 채팅방 나가기 알림 ***************###############
@csrf_exempt
def friend_leave(request, user_key):
    # 카카오톡 봇 외의 다른 User Agent의 진입을 차단
    if not ACCESS_USER_AGENT in request.META['HTTP_USER_AGENT']:
        return HttpResponse('This service is only accessable on KakaoTalk bot.')

    if request.method == 'DELETE':
        # 사용자 키가 데이터베이스에 없다면 생성하고, 있으면 기본값으로 변경한다.
        try:
            cur_serv = KakaoService.objects.get(user=user_key)
            # cur_serv.dhcp_status = False
            cur_serv.nightbus_status = False
            cur_serv.paidtoilet_status = False
            cur_serv.save()
        except ObjectDoesNotExist:
            cur_serv = KakaoService.objects.create(user=user_key)
            cur_serv.save()
    return HttpResponse()

'''
#################***************** 이미지 로딩 *****************#################
def image_load(request, image_name):
    link = image_name

    # 이미지를 read binary로 불러오고 http로 전송한다.
    images = []
    image_data_ = open(link, "rb").read()
    images.append(image_data_)

    return HttpResponse(images, content_type="image/jpg")
'''

#################***************** 첫 페이지 *****************#################
def web_index(request):
    return render(request, 'web/index.html', {})

###############***************** 요청 뷰 페이지 *****************###############
def web_request_view(request, condition):
    if condition == '':
        guideRequests = WebGuideRequests.objects.all()
    elif condition == 'process':
        guideRequests = WebGuideRequests.objects.filter(finished=False)
    elif condition == 'complete':
        guideRequests = WebGuideRequests.objects.filter(finished=True)
    else:
        raise Http404("404 Not Found. %s is not available" % condition)
        
    return render(request, 'web/request_view.html', {'requests': guideRequests})

###############************** 요청 detail 페이지 **************###############
def web_request_detail(request, req_id):
    # 해당 id에 맞는 요청 객체 불러오기
    try:
        guideRequest = WebGuideRequests.objects.get(id=req_id)
    except ObjectDoesNotExist:
        raise Http404("404 Not Found. Cannot find this id...")

    # 답변 내용 불러오기
    replyNotFound = False
    try:
        reply = WebGuideReplies.objects.get(request_id=req_id)
    except ObjectDoesNotExist:
        reply = None
        replyNotFound = True

    # 페이지 렌더링
    return render(request, 'web/request_detail.html', {
        'req': guideRequest, 'rep': reply, 'reply_notfound': replyNotFound
    })

#################***************** 요청 페이지 *****************#################
def web_guide_request(request):
    content = {}

    # POST 방식이라면 (즉, 요청 신청 버튼을 누른 상태라면)
    if request.method == 'POST':
        content['req_try'] = True
        content['success'] = True
        content['req_message'] = '요청이 완료되었습니다. 잠시만 기다려주세요!'

        # 데이터 로드
        name = request.POST['input_name']
        start = request.POST['input_startpoint']
        dest = request.POST['input_destination']

        # 입력값 검사
        if len(name) <= 0:
            content['success'] = False
            content['req_message'] = '이름을 입력해주세요.'
        elif len(name) >= 100:
            content['success'] = False
            content['req_message'] = '이름은 100자 이상 입력할 수 없습니다.'
        elif len(start) <= 0:
            content['success'] = False
            content['req_message'] = '출발지를 입력해주세요.'
        elif len(start) >= 100:
            content['success'] = False
            content['req_message'] = '출발지는 100자 이상 입력할 수 없습니다.'
        elif len(dest) <= 0:
            content['success'] = False
            content['req_message'] = '목적지를 입력해주세요.'
        elif len(dest) >= 100:
            content['success'] = False
            content['req_message'] = '목적지는 100자 이상 입력할 수 없습니다.'

        # 검사 통과시 DB(요청목록)에 등록
        if content['success']:
            WebGuideRequests.objects.create(
                user=name, startpoint=start, destination=dest
            )

    # 페이지 렌더링
    return render(request, 'web/guide_request.html', content)
