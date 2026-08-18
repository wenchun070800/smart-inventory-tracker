# edge/Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY infer.py smoothing.py /app/
# Copy models into /models in your build context if available
COPY models /models
ENV PYTHONUNBUFFERED=1
CMD ["python", "infer.py", "--backend", "http://backend:8000/api/detections"]