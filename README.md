______________________
# Шаблон для разворота telegram бота в Docker

1. Установите docker и docker-compose
2. Добавьте файл .env на основе шаблона .env_docker_example и заполните необходимые значения
3. Выполните  ``` docker-compose build ``` или  ``` sudo docker-compose build ``` для загрузки образа
4. Старт контейнера. 
   1. Для запуска контейнера ``` docker-compose up ``` или  ``` sudo docker-compose up ```
   2. Для запуска конетйнера в фоне выполните ```  docker-compose up -d ``` или   ``` sudo docker-compose up -d```
