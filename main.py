from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Testing deployment"}

@app.get("/health")
async def health():
    return {"status": "healthy"}