#Create network
docker network create -d bridge bigdata-network
#Create hadoop cluster
cd hadoop && docker-compose up -d --build && cd ..
#Create spark cluster
cd spark && docker-compose up -d --build && cd ..
#Create airflow
cd airflow && docker-compose up -d --build && cd ..