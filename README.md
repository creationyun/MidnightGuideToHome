# 자정시간 귀가안내 서비스 API

## app
카카오톡 플러스친구 서비스를 운영하는데 필요한 기능들을 모은 장고 앱이다.

## app_fb
페이스북 챗봇 서비스를 운영하는데 필요한 기능들을 모은 장고 앱이다.

## 필요한 구성 요소
Linux (Ubuntu, Debian, etc.), Python 3, Django 2.1, uWSGI, nginx, MongoDB (+pymongo)

## 별도로 추가해야 할 파일
### `MidnightGuideToHome/settings.py`
`settings_secret_removed.py` 파일에서 `SECRET_KEY` 등을 추가해서 이름을 원래대로 변경 후 사용하면 된다.
### `tokens.py`
```
PAGE_ACCESS_TOKEN = 페이스북 페이지 액세스 토큰
VERIFY_TOKEN = 콜백 URL에 대한 검증 토큰
```

### 문의사항
이메일: creationyun@gmail.com
페이스북: https://www.facebook.com/creationyun
