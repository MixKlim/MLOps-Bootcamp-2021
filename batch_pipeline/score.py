
import os
import numpy as np
from azureml.core import Model
import joblib

def init():
    # Runs when the pipeline step is initialized
    global model

    # load the model
    model_path = Model.get_model_path('fourier_regression')
    model = joblib.load(model_path)

def run(mini_batch):
    # This runs for each batch
    resultList = []

    # process each file in the batch
    for f in mini_batch:
        # Read comma-delimited data into an array
        data = np.genfromtxt(f, delimiter=',', skip_header=1)
        # Reshape into a 2-dimensional array for model input
        data = data[:, 1:]
        prediction = model.predict(data)
        # log results (for application insights)
        log = 'Data:' + str(data) + ' - Prediction:' + str(prediction)
        print(log)
        # Append prediction to results
        resultList.append("{}: {}".format(os.path.basename(f), np.mean(prediction)))
    return resultList
