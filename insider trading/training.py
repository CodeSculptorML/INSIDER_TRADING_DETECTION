import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# Sample data for demonstration
# Replace this with your actual data
data = np.array([[100, 500], [2000, 3000], [1500, 2500], [800, 1200]])
labels = np.array([0, 1, 1, 0])  # Example labels: 0 for no insider trading, 1 for insider trading

# Function to train SVM model and save it to a file
def train_and_save_model(data, labels, filename):
    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Training SVM model
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train_scaled, y_train)

    # Evaluate model
    train_accuracy = svm_model.score(X_train_scaled, y_train)
    test_accuracy = svm_model.score(X_test_scaled, y_test)
    print("Training Accuracy:", train_accuracy)
    print("Testing Accuracy:", test_accuracy)

    # Save trained model to a file
    joblib.dump(svm_model, filename)
    print("SVM model trained and saved successfully.")

# Train and save the SVM model
train_and_save_model(data, labels, "svm_model.pkl")
