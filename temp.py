import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #visualize random distribution using  matplotlib underneath to plot garaphs 
import csv
from tqdm import tqdm #for output  progress bar 
sns.set()

data = pd.read_csv('D:\\DS PROJECT\\spotify.csv')
data.head()
data.info