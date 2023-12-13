import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Read the Heart Disease dataset from the CSV file
heart_disease = pd.read_csv('heart-disease.csv')

# Display the first few rows of the dataset
print(heart_disease.head())

# Separate features (X) and target variable (y)
X = heart_disease.drop('target', axis=1)
y = heart_disease['target']

# Display the target variable
print(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the model (K-nearest neighbors in this case)
model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print the results

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(report)
