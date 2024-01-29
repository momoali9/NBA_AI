import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the data
df = pd.read_csv('stats.csv', delimiter=';', header=0, encoding='latin1')

# Extract features and target variable
features = ['Age', 'G', 'MP', 'FG%', '3P%', 'FT%']
X = df[features]
y = df['PTS']

# Train a Random Forest Regressor model
model = RandomForestRegressor()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Add the predicted points column to the dataframe
df['Predicted_PTS'] = predictions

# Display the dataframe with predicted points
print(df[['Player', '3P%', 'Predicted_PTS']])
