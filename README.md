# Smart Inventory Tracker

This repository contains a production-style AI Smart Inventory Tracker:
- ML training (YOLOv8)
- Edge inference (TFLite/Ultralytics)
- Backend (FastAPI, PostgreSQL, Celery, Redis)
- Frontend (React)
- Docker Compose for local dev

## Quickstart (local dev)
1. Copy `.env.example` to `.env` and adjust if needed.
2. Build and run services:
   - From `infra/` run: `docker-compose up --build`
3. Start edge inference locally (recommended for webcam):
   - `python edge/infer.py --use_ultralytics`
4. Open frontend at `http://localhost:3000` and backend at `http://localhost:8000`.

## Notes
- For a real deployment, export your trained model to TFLite/ONNX and place it in `edge/models/`.
- The ultralytics pretrained model is used for quick demos; train a custom model for SKU-level accuracy.
- The edge container may not have access to your host webcam; run `edge/infer.py` locally for demos.

## Next steps
- Add authentication, RBAC, and audit logs.
- Implement reorder automation (email/webhook).
- Add forecasting (Prophet or ARIMA) in `backend/app/utils/forecasting.py`.
