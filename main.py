import uvicorn
from Engine.app import app

if __name__ == "__main__":
    port = int(__import__("os").environ.get("PORT", 8000))
    print(f"Initializing AI.ftware on port {port}...")
    uvicorn.run(app, host="0.0.0.0", port=port, reload=False)
