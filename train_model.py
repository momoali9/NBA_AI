import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Read the CSV file
df = pd.read_csv('stats.csv', delimiter=';', encoding='latin1')

# Select features (excluding non-numeric columns)
X = df[['2P', '2P%', '2PA', '3P', '3P%', '3PA', 'Age', 'AST', 'BLK', 'DRB', 'eFG%', 'FG', 'FG%', 'FGA', 'FT', 'FT%', 'FTA', 'G', 'GS', 'MP', 'ORB', 'PF', 'PTS', 'Rk', 'STL', 'TOV', 'TRB']]

# Select the target variable
y = df['PTS']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a RandomForestRegressor model
model = RandomForestRegressor()

# Fit the model to the training data
model.fit(X_train, y_train)

# Print a message indicating successful training
print("Model training completed. Saving the model to model.pkl")

# Save the trained model to a file
joblib.dump(model, 'model.pkl')
