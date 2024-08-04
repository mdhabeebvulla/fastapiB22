from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from typing import List
from config.core import config
model_path = config.get('model_save_path')
with open(model_path,'rb') as model_file:
    model = pickle.load(model_file)
app = FastAPI()

class IrisData(BaseModel):
    sepal_length :  float
    sepal_width :float
    petal_length :float
    petal_width :float
    
class Prediction(BaseModel):
    species : str
    
@app.get("/predict",response_model = List[Prediction])
def predict(data : List[IrisData]):
    input_data =  pd.DataFrame([item.dict() for item in data])
    
    predictions = model.predict(input_data)
    
    return [Prediction(species=pred)for pred in predictions]
    
@app.get("/")
def read_ex():
    return{'message' :' welcome to fastapi'}
    
