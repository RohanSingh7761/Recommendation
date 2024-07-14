import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

users_df = pd.read_csv('RecommendationAlgo\users_100k_with_relationships.csv')
posts_df = pd.read_csv('posts_100k_with_relationships.csv')
interactions_df = pd.read_csv('interactions_100k_with_relationships.csv')