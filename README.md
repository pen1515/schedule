# schedule

### 使い方
```
### 起動時
#### docker起動
docker compose up
#### DB操作時
<!-- bash bin/connect_mysql.sh -->
docker compose exec db /bin/bash
mysql -u root -p
show databases;

mysqlでなく、sqliteを使うことになった。

####Django起動
docker compose exec app /bin/bash
cd Schedule/
./mahou.sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
http://localhost:8080/


### データベーススーパーユーザー
Username : isi
Email address: test@sample.com
Password: pass

### docker落とし方
docker compose down -v
#これでもいい(これは全部消すもの)
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
 
 docker network prune -f
 docker rmi -f $(docker images --filter dangling=true -qa)
 docker volume rm $(docker volume ls --filter dangling=true -q)
 docker rmi -f $(docker images -qa)

 ### マイグレーション消し方
 find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
 find . -path "*/migrations/*.pyc"  -delete


 
http://localhost:8080/suhedeleapp/test/

```