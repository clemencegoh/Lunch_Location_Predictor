"""
Use random forest
"""
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from data.generator import *


# create random forest model
random_forest_classifier = RandomForestClassifier(n_estimators=100)

# Generate random data
locations_data = genWithProbOf(weekday_probs=[0.5, 0.4, 0.05, 0.05], datapoints=30, start_day=0)
days_data = getDaysOfTheWeek(n=30, start_day=0)

vector_of_days = EncodeDaysToOneHotVector(days_data)
locations = EncodeLocationsToGroups(locations_data)

# train model
X_train, X_test, Y_train, Y_test = train_test_split(vector_of_days, locations, test_size=0.2)  # 20% test data
random_forest_classifier.fit(X_train, Y_train)

# predict
pred = random_forest_classifier.predict(X_test)

print("predictions:", pred)
print("Actual:", Y_test)

print("Accuracy:", metrics.accuracy_score(Y_test, pred))

next_day = [0, 1, 0, 0, 0, 0, 0]  # Tuesday
print("Predict Next:", random_forest_classifier.predict([next_day]))




