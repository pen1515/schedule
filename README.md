# schedule

### 使い方
```
### 起動時
#### docker起動
docker compose up
#### DB操作時
bash bin/connect_mysql.sh

####Django起動
docker compose exec app /bin/bash
./mahou.sh
python -m pip install Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixture1.json
python manage.py runserver 0.0.0.0:8080
http://localhost:8080/

### docker落とし方
docker compose down -v



http://localhost:8080/suhedeleapp/test/

```