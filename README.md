# GoutCare Application Setup

## Prerequisites
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd goutcare
   ```

2. **Copy the `.env.example` to `.env` and configure the environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file to set the appropriate values for your environment.

3. **Start the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Access the application:**
   - Backend API: `http://localhost:8000`
   - Frontend: `http://localhost:3001`

## Running Tests

1. **Backend Tests:**
   ```bash
   docker-compose exec backend pytest
   ```

2. **Frontend Tests:**
   ```bash
   docker-compose exec frontend npm test
   ```
