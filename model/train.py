import torch
import torch.nn as nn
import torch.nn.functional as Functional
import torch.optim as optim

# Imports for math
import numpy as np
import matplotlib.pyplot as plt

import time
from geopy.geocoders import Nominatim

print(time.time())

geolocator = Nominatim(user_agent="Simple_test")

reversed_location = geolocator.reverse("1.3200423, 103.9076766")
print(reversed_location.address)

location = geolocator.geocode("Spring court restaurant")
print(location.address)
print(location.latitude, location.longitude)
