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

## Installation with Docker
  - Clone the repository and build the image.

    ```bash
    git clone
    docker-compose up -d --build
    ```
      
  - Run the container.
    
    ```bash
    docker-compose up
    ```

## Installation without Docker
  - Clone the repository and build the image.
    
    ```bash
    git clone
    docker build -t youtubedb .
    ```
    
  - Run the container.
    
    ```bash
    docker run -p 8080:8080 youtubedb
    ```