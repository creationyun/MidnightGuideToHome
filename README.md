# 자정시간 귀가안내 서비스 (Midnight Guide To Home Service) API

자정시간 귀가안내 서비스의 챗봇 소프트웨어는 자유 소프트웨어입니다.
(GPLv3 사용, LICENSE 파일 참고)

Midnight Guide To Home Service chatbot software is a free software.
(Used GPLv3, see LICENSE file.)

## app
카카오톡 플러스친구 서비스를 운영하는데 필요한 기능들을 모은 장고 앱입니다.

Django app is collected functions required to operate the
KakaoTalk Plusfriend service.

## app_fb
페이스북 챗봇 서비스를 운영하는데 필요한 기능들을 모은 장고 앱입니다.

Django app_fb is collected functions required to operate the
Facebook chatbot service.

## lib.py
서비스를 운영하는데 필요한 라이브러리 파이썬 파일입니다.
각종 메서드, 서비스 안내문 (문자열 변수), 소규모 정적 데이터베이스 등을 모아놓았습니다.

It is a library Python file required to operate the service.
Various methods, service announcements (string variables), small static database,
and so on.

## static
이미지, admin 페이지 css, js 파일 등을 관리하는 장고 static 파일입니다.

자정시간 귀가안내 서비스 요청에 사용되는 이미지도 포함되어 있습니다.

It is a Django static files managing the images, css, js files
of the admin page, etc.

It contains images used by Midnight Guide To Home requests.

## 필요한 구성요소 (Required Components)
Linux (Ubuntu, Debian, etc.), Python 3.6 or more, Django 2.1, uWSGI, nginx,
MongoDB (+pymongo, djongo)

settings.py 파일을 수정한 후에, 다른 데이터베이스 모듈을 사용할 수도 있습니다.

After modifying settings.py file, you can also use the other database module.

## 별도로 추가해야 할 파일 (Files to Add Separately)

### MidnightGuideToHome/settings.py
settings_secret_removed.py 파일에서 `SECRET_KEY` 등을 추가해서
이름을 settings.py로 원래대로 변경 후 사용하면 됩니다.

In settings_secret_removed.py file, add `SECRET_KEY`, etc.,
and change the name back to its original name, settings.py.

### tokens.py
다음과 같이 2개의 문자열 변수를 지정해주면 됩니다. 페이스북 챗봇 운영시 반드시 필요합니다.

You can specify two string variables as follows. It is absolutely necessary to operate Facebook chatbot.

```
PAGE_ACCESS_TOKEN = Own Facebook Page Access Token
VERIFY_TOKEN = Verification Token for Callback URL
```

## 설치 과정 (Installation Process)
(우분투 18.04 기준, Based on Ubuntu 18.04)
### 1. 업데이트 후 Python 3의 pip를 설치합니다.
### After updates, and install pip of Python 3.
```
$ sudo apt update
$ sudo apt install python3-pip
```

### 2. pip를 통해 virtual environment를 설치합니다.
### Install virtual environment through pip.
```
$ sudo pip3 install virtualenv
```

### 3. virtual environment를 생성한 후, 활성화합니다.
### Generate your own virtual environment, and activate.
```
$ virtualenv venv
$ cd venv
$ source bin/activate
```

### 4. Django를 설치합니다.
### Install Django.
```
(venv) $ pip3 install django
```

### 5. 자정시간 귀가안내 서비스의 Django 패키지를 가져옵니다.
### Import the Midnight Guide To Home Service Django package.
```
(venv) $ cd ..
(venv) $ git clone https://github.com/creationyun/MidnightGuideToHome.git
```

### 6. 비활성화 후, uwsgi를 설치합니다.
### Deactivate, and install uwsgi.
```
(venv) $ deactivate
$ pip3 install uwsgi
```

### 7. /etc/uwsgi/sites에 ini 파일을 편집합니다.
### Generate an ini file in /etc/uwsgi/sites and edit it.
```
$ cd /etc
$ sudo mkdir -p uwsgi/sites
$ cd uwsgi/sites
$ sudo nano MidnightGuideToHome_uwsgi.ini
```
```
[uwsgi]
project = MidnightGuideToHome
base = /home/user

chdir = %(base)/%(project)
home = %(base)/venv
module = %(project).wsgi:application

master = true
processes = 5

socket = %(base)/%(project)/%(project).sock
chmod-socket = 666
vacuum = true
```

(base: MidnightGuideToHome이 있는 위치.
/home/ubuntu 형태인 경우가 많다.)

(base: location with MidnightGuideToHome.
It is often in the form of /home/ubuntu.)

### 8. /etc/systemd/system/uwsgi.service를 편집합니다.
### Edit /etc/systemd/system/uwsgi.service file.

```
$ cd /etc/systemd/system
$ sudo nano uwsgi.service
```
```
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=on-failure
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

### 9. nginx를 설치하고 /etc/nginx/sites-available 디렉토리에 MidnightGuideToHome 파일을 생성합니다.
### Install nginx, and generate MidnightGuideToHome file in /etc/nginx/sites-available.
```
$ sudo apt install nginx
$ sudo nano /etc/nginx/sites-available/MidnightGuideToHome
```
```
server {
    listen 80;
    server_name localhost example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user/MidnightGuideToHome;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/user/MidnightGuideToHome/MidnightGuideToHome.sock;
    }
}
```

### 10. /etc/nginx/sites-enabled에 해당 파일의 바로가기를 만든 후 nginx가 제대로 설정됐는지 테스트합니다.
### Create a shortcut to the file in /etc/nginx/sites-enabled, and test for configuration of nginx.
```
$ sudo ln -s /etc/nginx/sites-available/MidnightGuideToHome /etc/nginx/sites-enabled
$ sudo nginx -t
```

### 11. mongoDB, Djongo, requests를 설치합니다.
### Install mongoDB, Djongo, and requests.
```
$ sudo apt install mongodb
$ cd /home/user
$ source venv/bin/activate
(venv) $ pip3 install djongo
(venv) $ pip3 install requests
```
(Djongo: Django의 mongoDB 연결을 수행함)

(Djongo: connecting to mongoDB in Django)

### 12. mongoDB 서비스를 구동하고 Django의 migration을 수행합니다.
### Start the mongoDB service, and run migration of Django.

settings.py 파일을 수정하고(비밀 키 추가), tokens.py 파일을 만든 다음에...

Modify settings.py (add secret key), make tokens.py file and...

```
(venv) $ sudo systemctl start mongodb
(venv) $ cd MidnightGuideToHome
(venv) $ ./manage.py migrate
```

비밀 키와 호스트를 MidnightGuideToHome/MidnightGuideToHome/settings.py의
ALLOWED_HOSTS에 추가해주세요.

Please add your secret key and hosts in ALLOWED_HOSTS of
MidnightGuideToHome/MidnightGuideToHome/settings.py

## 문의사항 (Contact Us)
- Email: creationyun@gmail.com
- Facebook: https://www.facebook.com/creationyun
