# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import WebGuideRequests, WebGuideReplies, WebPubTransRoutesComparisons, WebBusTimetable


#################***************** 첫 페이지 *****************#################
def web_index(request):
    return render(request, 'web/index.html', {})


###############***************** 요청 뷰 페이지 *****************###############
def web_request_view(request, condition):
    if condition == 'all':  # 모든 요청
        guideRequests = WebGuideRequests.objects.all()
    elif condition == 'process':  # 진행 중인 요청
        guideRequests = WebGuideRequests.objects.filter(finished=False)
    elif condition == 'complete':  # 완료된 요청
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


#################***** 대중교통 경로의 장단점 비교 페이지 *****#################
def web_pub_trans_routes_comparisons(request):
    all_posts = WebPubTransRoutesComparisons.objects.all()
    return render(request, 'web/pub_trans_routes_comparisons.html', {'posts': all_posts})


#################***** 버스 시간표 페이지 *****#################
def web_bus_timetable_view(request, category):
    buses = WebBusTimetable.objects.filter(category=category)
    return render(request, 'web/bus_timetable_view.html', {'buses': buses})


#################***** 버스 시간표 detail 페이지 *****#################
def web_bus_timetable_detail(request, bus_id):
    try:
        bus = WebBusTimetable.objects.get(id=bus_id)
    except ObjectDoesNotExist:
        raise Http404("404 Not Found. Cannot find this id...")

    return render(request, 'web/bus_timetable_detail.html', {'bus': bus})
