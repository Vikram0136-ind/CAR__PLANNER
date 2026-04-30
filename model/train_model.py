import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
import pickle
import os

# Get correct path to CSV
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "data", "cars.csv")

# Load dataset
df = pd.read_csv(file_path)

# Encode categorical columns
le_fuel = LabelEncoder()
le_trans = LabelEncoder()
le_type = LabelEncoder()

df['fuel'] = le_fuel.fit_transform(df['fuel'])
df['transmission'] = le_trans.fit_transform(df['transmission'])
df['type'] = le_type.fit_transform(df['type'])

# Features
X = df[['price', 'mileage', 'fuel', 'transmission', 'seats', 'type']]

# Train model
model = NearestNeighbors(n_neighbors=5)
model.fit(X)

# Save model
model_path = os.path.join(base_dir, "model.pkl")
pickle.dump((model, df, le_fuel, le_trans, le_type), open(model_path, "wb"))

print("✅ Model trained and saved successfully!")