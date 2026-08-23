# Runbook

## Restart Backend
docker-compose restart backend

## Restart Edge
python edge/infer.py

## Check Logs
docker logs backend
docker logs celery
docker logs traefik
