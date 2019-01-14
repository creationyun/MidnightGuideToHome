# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib
from static_lib import *

ver = "2.0"

#################***************** 경로 찾기 *****************#################
@csrf_exempt
def kakaoi_findpath(request):
	# 올바른 POST 요청이 맞는지 검증
    if request.method != 'POST':
        return HttpResponse('Wrong request.')

    # 카카오 서버로부터 받은 JSON request에서 데이터를 추출한다.
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)  # JSON 파일 디코딩

    try:
        # req_time: 시간
        # req_origin: 출발지
        # req_dest: 목적지
        #
        req_time = received_json['action']['params']['midnight_time']
        req_origin = received_json['action']['params']['location_origin']
        req_dest = received_json['action']['params']['location_dest']
    except KeyError:
        # 비정상적인 JSON 요청
        return JsonResponse({
            "version": ver,
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "요청이 비정상적입니다. 관리자에게 문의해주세요."
                        }
                    }
                ]
            }
        })

    # 구글 지도 URL 파라미터
    google_maps_param = {
        # api=1&origin={}&destination={}&travelmode=transit
        "api": "1",
        "origin": req_origin,
        "destination": req_dest,
        "travelmode": "transit"
    }

    # format에 맞춰서 JSON response를 보냄.
    return JsonResponse({
        "version": ver,
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": MidnightGuideResultKakao.format(
                            req_origin, req_dest, req_time,
                            urllib.parse.urlencode(google_maps_param))
                    }
                }
            ]
        }
    })

############################################################################

'''
블록 형식
{
  "intent": {
    "id": "ef5jxscq867w3jnqyyksbt65",
    "name": "블록 이름"
  },
  "userRequest": {
    "timezone": "Asia/Seoul",
    "params": {
      "ignoreMe": "true"
    },
    "block": {
      "id": "ef5jxscq867w3jnqyyksbt65",
      "name": "블록 이름"
    },
    "utterance": "발화 내용",
    "lang": null,
    "user": {
      "id": "056184",
      "type": "accountId",
      "properties": {}
    }
  },
  "bot": {
    "id": "5c125ed85f38dd62e312d599",
    "name": "봇 이름"
  },
  "action": {
    "name": "dylm5jurse",
    "clientExtra": null,
    "params": {
      "midnight_time": "12:30",
      "location_origin": "서울역",
      "location_dest": "강남역"
    },
    "id": "x80y6dnrgkcy5496lbrb2cr7",
    "detailParams": {
      "midnight_time": {
        "origin": "12:30",
        "value": "12:30",
        "groupName": ""
      },
      "location_origin": {
        "origin": "서울역",
        "value": "서울역",
        "groupName": ""
      },
      "location_dest": {
        "origin": "강남역",
        "value": "강남역",
        "groupName": ""
      }
    }
  }
}
'''
