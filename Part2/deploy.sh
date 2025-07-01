#!/bin/bash

# Build Docker image
docker build -t ai-agent-service .

# Run container with environment variables
docker run -d -p 8000:8000 -p 8501:8501 --env-file part1/.env \
  --memory="512m" --cpus="1" ai-agent-service

# Example AWS ECS deployment (adjust for your platform)
# aws ecs register-task-definition --cli-input-json file://task-definition.json
# aws ecs update-service --cluster my-cluster --service my-service --task-definition ai-agent-service