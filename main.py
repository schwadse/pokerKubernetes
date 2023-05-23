from fastapi import FastAPI
import uvicorn
import random
app = FastAPI()

@app.get('/random')
def root():
    return {'myCard': random.randint(1, 100)}

@app.get('/health')
def health():
    return {'healthy': True}


if __name__ == "__main__":
   
    uvicorn.run(app, host="0.0.0.0", port=8080)

