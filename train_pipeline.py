import pandas as pd
import pickle
from config.core import config
from pipeline import create_pipeline
from processing.data_manager import load_data

def train():
    data_path = config.get('data_path')
    data  = load_data(data_path)
    pipeline = create_pipeline()
    pipeline.fit(data.drop(columns = [config.get('target_variable')]),data[config.get('target_variable')])
    model_path = config.get('model_save_path')
    with open(model_path,'wb') as model_file:
        pickle.dump(pipeline,model_file)
    
    
if __name__ == "__main__":
    train()