
### Build Docker Image
docker build -t feature-store .

### Run Locally
uvicorn app.api:app --reload --host 0.0.0.0 --port 8000


### Deploy to Kubernetes
kubectl apply -f kubernetes_deployment.yaml


### GET
curl -X GET "http://127.0.0.1:8000/get-features/"

### POST 
curl -X POST "http://127.0.0.1:8000/store-features/" \
-H "Content-Type: application/json" \
-d '{"features": {"petal length (cm)": 0.8, "petal width (cm)": 0.7, "sepal length (cm)": 0.6, "sepal width (cm)": 0.4}}'


## Execution 

