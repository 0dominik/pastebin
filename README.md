# Pastebin Application with Docker and MongoDB

This project is a containerized Pastebin-like application built using **Flask**, **MongoDB**, and **Docker**. It allows users to create, view, and share text entries via unique links.

## Features

- Create and view text entries with unique, shareable links.
- Fully containerized using Docker and Docker Compose.
- Persistent data storage using MongoDB.
- Easy deployment and portability across systems.

## Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed ([Install Docker Compose](https://docs.docker.com/compose/install/))

## Project Structure

```
PROJECT
├── app
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   ├── index.html
│   │   └── view_paste.html
│   └── app.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
```

### Explanation

- **app/**: Contains Flask application code, HTML templates, and static CSS files.
- **docker-compose.yml**: Orchestrates the Flask app and MongoDB containers.
- **Dockerfile**: Builds the Flask application container.
- **requirements.txt**: Lists Python dependencies for the Flask application.

## Setup Instructions

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Build and Run the Application

Using Docker Compose:
```bash
docker-compose up --build
```

- The application will be accessible at `http://localhost:5000`.
- MongoDB will run in a container, and data will persist using the Docker volume `mongodb_data`.

## Using the Application

1. **Create a Paste**:
   - Go to `http://localhost:5000`.
   - Enter a title, content, and (optional) author name.
   - Click **Publish** to generate a unique link for the paste.

2. **View a Paste**:
   - Use the unique link provided after creating a paste.
   - Example: `http://localhost:5000/your-paste-id`.

## Environment Variables

- `MONGO_URI`: MongoDB connection string (default: `mongodb://mongodb:27017/`).
- `DEBUG`: Enables/disables Flask debug mode.

## Author

Created by **0dominik**.

