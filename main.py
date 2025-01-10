from app.api import app
from app.monitoring import init_monitoring

if __name__ == "__main__":
    import uvicorn
    init_monitoring()
    uvicorn.run(app, host="0.0.0.0", port=8000)
