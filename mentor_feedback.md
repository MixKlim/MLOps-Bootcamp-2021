# Feedback:

Congrats on finishing up and presenting the Bootcamp!
Overall the project reached the goal: Having a model that allows us to determine our energy consumption.

## Top Highlights of the project:

- The goal was achieved in two different ways, with batch, and near real-time monitoring dashboard.
- The batch monitoring takes seasonality into account
- The blob function is set up properly with its requirements, and triggers.

## Points to improve:

- The READMEs in the project could be more descriptive in how to set up and deploy the project, however it had the instructions or some copies of certain documentation.
- It would've been nice to structure the project in a way that's not dependant on the notebook, since it would make some functions more usable, such as getting the workspace and the creation of global variables such as `model` in the notebook `create_batch_pipeline.ipynb` that creates the batch pipeline.
- The naming of the variables can improve as well, for instance when picking up one week of data, the variable for this is called X. When working on a team, this can lead to confusion, and more time spent in reading the code in order to maintain it.

## Additional feedback:
**Notebook `process_data.ipynb`**.

The goal of this notebook is a little bit fuzzy. Is it EDA? Is it a data preprocessing for a specific use case (batch and near real-time processing)?

The best option to keep it separately:
- 1 notebook dedicated to EDA, learn more about the data, distributions, outliers, insights, with comments, ideas, hypothesis in markdown.
- 1 notebook to prepare data (preprocess) for a batch use case (as we need to resample data on a daily basis instead of 15min). Preprocess energy generation predictions (wind and solar) separately.
- 1 notebook to prepare data (preprocess) for a near real-time use case. Preprocess energy generation predictions (wind and soldar) separately.

Why it is important to split them?

EDA notebook will remain, probably, as a guidance and a reminder about why specific decisions and steps were taken, the other 2 notebooks could be converted into python scripts and scheduled for incoming data preprocessing. It is better to keep energy generation predictions (wind + solar) apart as for the batch scenario they should be used only during the last step; and for near real-time scenario they could be replaced by direct API calls to get up-to-date predictions.

Regarding Dashboiard KPI and splitting the data into three quantiles. This is no go situation without a domain knowledge. In case with the Capstone such questions had to be addressed to a Dexter representative (who was availble via Slack and waiting for such questions). In real life a conversation (set of conversations) with domain knowledge expert is a must. The business metrics should be crystal clear, especially when end users are envolved.

Where is the train test split taking place? Creating features and transforming data before this split could lead to data leakage, that we have to avoid.

**Notebook `model_training_evaluation.ipynb`**.

The same advice to keep batch and near real-time model separately.

_Batch model_

As the batch model generates predictions on a daily level for the upcoming week, it is better to train the model on data, aggregated on daily level. So, train test split with aggregated and registered data is expected to be done before running this notebook. Train dataset will be used for training and validating the models, test dataset will be used for model evaluations.

Feature engineering for a linear regression model could be encapsulated into functions (such as two functions provided for you in the capstone notebook). The functions from the notebook could be easily translated to Python script and run as a part of scheduled training/retraining job in the future. On top of it, all functions could be easily tested with pytest or unittest framework.

_Backtesting_

In our case we need to baktest batch models with a sliding window approach and based our choice on MAPE.

To start with we need to define the size of the sliding window and a step. Each window is split into training data, which is used to train the model, and testing data, which is used to calculate the error rate for the trained model.

For example: historical training data contains datapoints between 01/01/2020 and 01/03/2021 (14 months); sliding window size is 5 months (where 3 months to train and 2 months to test), step - 1 month. As a result you need to train and test 10 models on the following windows:
- 01/01/2020-01/04/2020 train, 01/04/2020-01/06/2020 test
- 01/02/2020-01/05/2020 train, 01/05/2020-01/07/2020 test
- 01/03/2020-01/06/2020 train, 01/06/2020-01/08/2020 test
- 01/04/2020-01/07/2020 train, 01/07/2020-01/09/2020 test
- 01/05/2020-01/08/2020 train, 01/08/2020-01/10/2020 test
- 01/06/2020-01/09/2020 train, 01/09/2020-01/11/2020 test
- 01/07/2020-01/10/2020 train, 01/10/2020-01/12/2020 test
- 01/08/2020-01/11/2020 train, 01/11/2020-01/01/2021 test
- 01/09/2020-01/12/2020 train, 01/12/2020-01/02/2021 test
- 01/10/2020-01/01/2021 train, 01/01/2021-01/03/2021 test

In case with expanding window you will train and test the same amount of models (in our case 10), but the training window will look differently.

- 01/01/2020-01/04/2020 train, 01/04/2020-01/06/2020 test
- 01/01/2020-01/05/2020 train, 01/05/2020-01/07/2020 test
- 01/01/2020-01/06/2020 train, 01/06/2020-01/08/2020 test
- 01/01/2020-01/07/2020 train, 01/07/2020-01/09/2020 test
- 01/01/2020-01/08/2020 train, 01/08/2020-01/10/2020 test
- 01/01/2020-01/09/2020 train, 01/09/2020-01/11/2020 test
- 01/01/2020-01/10/2020 train, 01/10/2020-01/12/2020 test
- 01/01/2020-01/11/2020 train, 01/11/2020-01/01/2021 test
- 01/01/2020-01/12/2020 train, 01/12/2020-01/02/2021 test
- 01/01/2020-01/01/2021 train, 01/01/2021-01/03/2021 test


TODO:  add comments on
batch pipeline

TODO: add comments on
azure functions

TODO: add comments on
overall structure, yamls, txts
