from django.db import models


class WebGuideRequests(models.Model):
    # user: 이름
    # request_time: 요청 날짜와 시간
    # startpoint: 출발지
    # destination: 목적지
    # finished: 진행중(False), 완료(True), 기본값: False
    user = models.CharField(max_length=100)
    request_time = models.DateTimeField(auto_now_add=True)
    startpoint = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)


class WebGuideReplies(models.Model):
    # reply_time: 답변 날짜와 시간
    # request_id: 관련된 요청 ID
    # reply_content: 답변 내용
    reply_time = models.DateTimeField(auto_now_add=True)
    request_id = models.IntegerField()
    reply_content = models.TextField(blank=True)


class WebPubTransRoutesComparisons(models.Model):
    # num: 게시글 번호
    # route: 경로 (예: "서울역 ~ 강남역")
    # url: 웹 사이트 주소
    num = models.BigAutoField(primary_key=True)
    route = models.CharField(max_length=100)
    url = models.CharField(max_length=200)


class WebBusTimetable(models.Model):
    # update_date: 버스 업데이트 날짜
    # region: 버스가 다니는 주요 지역 (혹은 운수업체 소재지)
    # category: 버스 카테고리 (seoul, incheon, gyeonggido 등)
    # bus_num: 버스 번호
    # bus_start_point: 버스 기점
    # bus_end_point: 버스 종점 (회차점)
    # post_url: 버스 시간표 관련 게시글 링크
    # img_url: 버스 시간표 이미지 링크
    update_date = models.DateField()
    region = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    bus_num = models.CharField(max_length=10)
    bus_start_point = models.CharField(max_length=100)
    bus_end_point = models.CharField(max_length=100)
    post_url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
