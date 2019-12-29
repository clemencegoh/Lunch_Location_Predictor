# Lunch_Location_Predictor
Lunch Location Predictor service in python, 
using machine learning to predict the next day's lunch 
location of choice

## Implementation specifics
* Initial Idea:
    * Use Random forest to predict
* Current Stats:
    * Average Accuracy achieved: 83%
    * Works better when probability does not favor too heavily on any location


## TODO:
- [X] Encode all data into one-hot vectors
- [X] Write code for train and validate/test
- [X] Write code for prediction based off model
    * **Redo this**
- [ ] Integrate such that one function call with a new datapoint re-trains the model and predicts based off the new model
- [X] Deploy as a microservice
    * Deployed to heroku for now, to scale when needed