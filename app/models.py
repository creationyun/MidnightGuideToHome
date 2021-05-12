from django.db import models


############################## 모    델 ################################
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


class WebPubTransRoutesComparisons(models.Model):
    num = models.BigAutoField(primary_key=True)
    route = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
