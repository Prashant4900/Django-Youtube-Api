# **YouTube Search**

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for music query in a paginated response.

# Basic Requirements
  - Server should call the YouTube API continuously in background (async) with some interval (5 minutes) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
  - A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
  - A basic search API to search the stored videos using their title and description.
  - Dockerize the project.
  - It should be scalable and optimised.

## Task For Bonus Points
  - Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
  - Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`.

## Prequisites
  - ***.env.dev*** file should be present in the root directory of the project.
  - Environment file must contain these variables

        DB_HOST=db
        DB_NAME=app
        DB_USER=postgres
        DB_PASSWORD=findmypasswordlol
        REDIS_PASSWORD=findmypasswordlol
        POSTGRES_DB=app
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=findmypasswordlol
        DEBUG=True
        YOUTUBE_API_KEY=<YOUTUBE-API-KEY>

## Installation with Docker
  - Clone the repository and build the image.

    ```bash
    git clone https://github.com/Prashant4900/Fampay-Django-Youtube-Api
    docker-compose up -d --build
    ```
      
  - Run the container.
    
    ```bash
    docker-compose up
    ```

  - Create Superuser.
    
    ```bash
    docker exec -it <Project-Name> python manage.py createsuperuser
    ```

## Installation without Docker
  - Clone the repository
    
    ```bash
    git clone https://github.com/Prashant4900/Fampay-Django-Youtube-Api
    ```
   
  - Create Virtual Environment
    
    ```bash
    virtualenv env
    ```

  - Install dependencies.
    
    ```bash
    pip install -r requirements.txt
    ```
  
  - Run the migrations.
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

  - Run the server.
    
    ```bash
    python manage.py runserver
    ```

  - Create a superuser.
    
    ```bash
    python manage.py createsuperuser
    ```

# API Endpoint
  - Get all videos.
    
    ```bash
    curl -X GET http://localhost:8000/api/videos/list/
    ```

  - Get all videos in a paginated response.
    
    ```bash
    curl -X GET http://localhost:8000/api/videos/list/?page=1&page_size=10
    ```

  - Search videos.
    
    ```bash
    curl -X GET http://localhost:8000/api/videos/list/?title=game
    curl -X GET http://localhost:8000/api/videos/list/?description=game
    curl -X GET http://localhost:8000/api/videos/list/?title=game&description=game
    ```

# Screen Sorts

![image](https://raw.githubusercontent.com/Prashant4900/Fampay-Django-Youtube-Api/main/assets/get-all.png)
![image](https://raw.githubusercontent.com/Prashant4900/Fampay-Django-Youtube-Api/main/assets/get-filter.png)
![image](https://raw.githubusercontent.com/Prashant4900/Fampay-Django-Youtube-Api/main/assets/homepage-1.png)
![image](https://raw.githubusercontent.com/Prashant4900/Fampay-Django-Youtube-Api/main/assets/homepage-2.png)
