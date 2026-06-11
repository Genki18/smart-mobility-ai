# Smart Mobility Cloud App

This project is a cloud-native prototype for the SDGs topic **Mobilitas & Kota Cerdas**. It includes:

- Frontend web UI
- FastAPI backend with AI congestion prediction
- PostgreSQL database schema
- MinIO object storage bucket
- Docker Compose networking for separate VPC-style segments
- GitHub Actions CI/CD workflow

## Quick start

1. Build the stack:
   docker compose up --build
2. Open the frontend at http://localhost:8080
3. Test the backend at http://localhost:8000/health

## Architecture

- Frontend VPC: Nginx frontend container
- Backend VPC: FastAPI backend container
- Database VPC: PostgreSQL container
- Storage VPC: MinIO bucket container
- AI VPC: dedicated network segment for AI services

## AI feature

The backend exposes an AI-powered congestion prediction endpoint that estimates traffic congestion intensity using a lightweight ML model derived from route, weather, and time-of-day indicators.

## CI/CD

The workflow in .github/workflows/ci.yml performs build and test automation, then builds the backend Docker image.
