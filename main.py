from poker import Rank, Card
from fastapi import FastAPI
import uvicorn
import random
app = FastAPI()

@app.get('/random')
def root():
    return {'myCard': random.randint(1, 100)}


if __name__ == "__main__":
   
    uvicorn.run(app, host="pythonapp.127.0.0.1.nip.io", port=80)

