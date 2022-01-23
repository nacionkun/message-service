# message-service

MessagingService in Python

## mongo-app
> core_service.py

## mongo-db
> mongodb container actions

docker-compose up --build

docker inspect core-py-mongo-1

> IP may change when container is run, so need to get from inspect
> Update IP in core_service.py

docker cp core_service.py core-py-mongo-1:/var/www/html

docker exec -it core-py-mongo-1 /bin/bash

python3 /var/www/html/core_service.py

docker-compose down

