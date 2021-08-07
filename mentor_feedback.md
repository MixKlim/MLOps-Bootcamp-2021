# Feedback:

Congrats on finishing up and presenting the bootcamp!
Overall the project reached the goal: Having a model that allows us to determine our energy consumption. 

## Top Highlights of the project:

- The goal was achieved in two different ways, with batch and near real time monitoring dashboard.
- The batch monitoring takes seasonality seasonality into account
- The blob function is set up properly with its requirements, and triggers.

## Points to improve:

- The READMEs in the project could be more descriptive in how to set up and deploy the project, however it had the instructions or some copies of certain documentation.
- It would've been nice to structure the project in a way that's not dependant on the notebook, since it would make some functions more usable, such as getting the workspace and the creation of global variables such as `model` in the notebook `create_batch_pipeline.ipynb` that creates the batch pipeline.
- The naming of the variables can improve as well, for instance when picking up one week of data, the variable for this is called X. When working on a team, this can lead to confusion, and more time spent in reading the code in order to maintain it.