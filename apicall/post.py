import requests

url = "http://127.0.0.1:8000/store-features/"
data = {
    "features": {
        "petal length (cm)": 0.8,
        "petal width (cm)": 0.7,
        "sepal length (cm)": 0.6,
        "sepal width (cm)": 0.4
    }
}

response = requests.post(url, json=data)
print(response.json())