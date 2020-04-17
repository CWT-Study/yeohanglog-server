# TripLogAPIServer

## 필요 라이브러리
```
$ pip install flask-bcrypt
$ pip install flask-restplus
$ pip install Flask-Migrate
$ pip install pyjwt
$ pip install Flask-Script
$ pip install flask_testing
$ pip install flask_restful
$  pip install boto3
```

## DynamoDB 로컬 사용법

### CLI를 통해 키설정
```
pip install awscli
aws configure
    - Access키 설정
    - secret키 설정
    - region : ap-northest-2입력
    - output format : 엔터

```

Dynamo 사용 설명법[https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html]

1. 해당 사이트에서 윈도우용 파일을 받음
2. 원하는 위치에 압축을 품
3. 터미널에서 cd 명령어를 통해 해당 폴더로 이동
4. 'java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb'커맨드 실행