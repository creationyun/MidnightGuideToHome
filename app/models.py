from django.db import models

############################## 모    델 ################################
# KakaoService
###############################
# user: 카카오톡 사용자 ID (hashed)
# created_time: DB 초기화 후 플러스친구 서비스 처음 사용 날짜와 시간
# updated_time: 플러스친구 서비스 마지막 사용 날짜와 시간
# dhcp_status: (사용안함)
# nightbus_status: 서울 심야버스 알아보기 메뉴 on/off 상태
# paidtoilet_status: 지하철 운임구역 화장실 알아보기 메뉴 on/off 상태
#########################################
# WebGuideRequests
###############################
# user: 이름
# request_time: 요청 날짜와 시간
# startpoint: 출발지
# destination: 목적지
# finished: 진행중(False), 완료(True), 기본값: False
#########################################
# WebGuideReplies
###############################
# reply_time: 답변 날짜와 시간
# request_id: 관련된 요청 ID
# reply_content: 답변 내용
#########################################

# Create your models here.
class KakaoService(models.Model):
    user = models.CharField(max_length=100, primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # dhcp_status = models.BooleanField(default=False)
    nightbus_status = models.BooleanField(default=False)
    paidtoilet_status = models.BooleanField(default=False)

class WebGuideRequests(models.Model):
    user = models.CharField(max_length=100)
    request_time = models.DateTimeField(auto_now_add=True)
    startpoint = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

class WebGuideReplies(models.Model):
    reply_time = models.DateTimeField(auto_now_add=True)
    request_id = models.IntegerField()
    reply_content = models.TextField(blank=True)
