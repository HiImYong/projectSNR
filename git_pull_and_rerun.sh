#!/bin/bash

# git_pull_and_rerun.sh 파일 내용

# 테스트 환경에서 테스트 먼저
{
  docker start snr__test
  docker exec snr bash -c "cd /data/site_projects/snr/src/ ; git pull origin master"
  docker exec snr bash -c "cd /data/site_projects/snr/src/ ; pip install -r requirements/prod.txt"
  docker exec snr__test bash -ce "cd /data/site_projects/snr/src/ ; python manage.py test -v 2 --settings=base.settings.prod 2>&1"
} || {
  docker stop snr__test
  exit 1
}

# 기존장고 종료
docker stop snr__test

# 기존장고 종료
docker exec snr pkill "gunicorn"

# 폴더에 깃에 있는 최신소스코드 가져오기
docker exec snr bash -ce "cd /data/site_projects/snr/src/ ; git pull origin master"

# 의존성 설치
docker exec snr bash -ce "cd /data/site_projects/snr/src/ ; pip install -r requirements/prod.txt"

# 마이그레이트
docker exec snr bash -ce "cd /data/site_projects/snr/src/ ; python manage.py migrate --settings=base.settings.prod"

# 장고를 운영모드로 실행
docker exec snr bash -ce "cd /data/site_projects/snr/src ; nohup gunicorn --bind=0.0.0.0:8000 base.wsgi &"

# static collect 다시 수행
docker exec snr bash -ce "cd /data/site_projects/snr/src ; echo yes | python manage.py collectstatic --settings=base.settings.prod"

exit 0