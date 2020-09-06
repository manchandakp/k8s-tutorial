docker build -t image-flask ./api
docker run --name cont-flask -p 5000:5000 image-flask python manage.py run -h 0.0.0.0
docker ps -a
docker image ls
docker image rm -f <image_id>

docker build -t image-postgres ./db
docker run -d --name cont-postgres image-postgres

docker exec -it dockerpoc_db_1 psql -d pocdb -U pocuser
psql -d pocdb -U pocuser

docker run --name cont-frontend -p 3000:3000 -v '' dockerpoc_frontend 

docker push kamalmanchanda/dockerpoc:frontend
docker push kamalmanchanda/dockerpoc:api
docker push kamalmanchanda/dockerpoc:db
docker push kamalmanchanda/dockerpoc:nginx
docker push kamalmanchanda/dockerpoc:nginxk8s

kubectl create secret generic regcred --from-file=.dockerconfigjson=/Users/kamalmanchanda/.docker/config.json --type=kubernetes.io/dockerconfigjson
kubectl get secret regcred --output=yaml

kubectl create secret docker-registry regcred --docker-server="https://index.docker.io/v1/" --docker-username="kamalmanchanda" --docker-password="Axtria@123" --docker-email="manchandakp@gmail.com"