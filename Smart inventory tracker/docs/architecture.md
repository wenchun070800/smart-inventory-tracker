# Architecture Overview

## Components
- Edge: YOLO/TFLite inference, sends counts to backend.
- Backend: FastAPI + PostgreSQL + Redis + Celery.
- Frontend: React dashboard with WebSocket live updates.
- Infra: Docker Compose + Traefik + Kubernetes manifests.

## Data Flow
Camera -> Edge -> Backend API -> DB -> WebSocket -> Frontend
