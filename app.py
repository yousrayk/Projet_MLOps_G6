import uvicorn
from fastapi import FastAPI
import joblib
import pandas as pd 
from prometheus_client import Counter, make_asgi_app


negative_counter = Counter("negative", "Counter for negative")
positive_counter = Counter("positive", "Counter for positive")

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get('/predict')

def predict(Area =float , Grey_Level=float, Gradient_Strength=float, Noise_Fluctuation=float,Contrast=float, Shape_Descriptor=float):
    classifier=joblib.load("fichier.joblib")

    X = pd.DataFrame([[Area, Grey_Level, Gradient_Strength,Noise_Fluctuation,Contrast, Shape_Descriptor]])
    prediction = classifier.predict(X)
    result = int(prediction) == 1
    if result:
        negative_counter.inc()
    else:
        positive_counter.inc()
    return result
    

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)