# **YouTube Search**

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for music query in a paginated response.

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
