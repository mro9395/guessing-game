import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import pickle
import random
import pprint
from scipy.special import entr

def load_pickle(filename):
    with open(filename, 'rb') as file:
        loaded_pickle = pickle.load(file)
    return loaded_pickle

def save_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
