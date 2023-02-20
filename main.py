import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing the dataset
dataset = pd.read_csv('realest.csv')

# preprocessing
dataset = dataset.dropna()
