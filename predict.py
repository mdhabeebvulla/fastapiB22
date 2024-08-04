import pickle
import pandas as pd
from config.core import config
def predict(new_data):
    model_path = config.get('model_save_path')
    with open(model_path,'rb') as model_file:
        model = pickle.load(model_file)
    predictions = model.predict(new_data)
    return predictions

if __name__ == "__main__":
    new_data = pd.DataFrame({
    'sepal_length' : [5.1,4.1],
    'speal_width' : [2.5,6.1],
    'petal_length' :[1.4,1.4],
    'petal_width' :[0.2,0.2]
    })
    print(predcit(new_data))
    