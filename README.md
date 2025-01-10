
### Build Docker Image
docker build -t feature-store .

### Run Locally
uvicorn app.api:app --reload --host 0.0.0.0 --port 8000


### Deploy to Kubernetes
kubectl apply -f kubernetes_deployment.yaml

https://chatgpt.com/c/677e24fa-0078-8013-a3f4-526311a51bd3