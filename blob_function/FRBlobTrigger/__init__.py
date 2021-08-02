import logging
import io
import numpy as np
import azure.functions as func
import pandas as pd
import datetime


def main(inputBlob: func.InputStream, predictions: func.Out[str]):

    df = pd.read_csv(io.BytesIO(inputBlob.read()), sep=',')
    # logging.info(f"data loaded: {df}")

    # Baseline model: Shifted by 15 minutes
    df_load_rt = df.copy(deep=True).reset_index()[["load_actuals_mw"]]
    df_load_rt["data_index_"] = pd.to_datetime(df.reset_index()["data_index_"]) + datetime.timedelta(minutes=15)
    df_load_rt = df_load_rt.set_index("data_index_").rename(columns={"load_actuals_mw": "predictions"})
    prediction = df_load_rt['predictions'].to_numpy()

    # logging.info(f"prediction: {prediction}")
    result = np.array_str(prediction)
    predictions.set(result)