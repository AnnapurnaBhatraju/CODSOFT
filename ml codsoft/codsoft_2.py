#CREDIT CARD FRAUD DETECTION

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the Credit Card Fraud Detection dataset (replace 'credit_card_dataset.csv' with your dataset)
df = pd.read_csv('credit_card_dataset.csv')

# Explore the dataset
print(df.head())

# Separate features and labels
X = df.drop('Class', axis=1)
y = df['Class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features using Standard Scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train_scaled, y_train)
logistic_predictions = logistic_model.predict(X_test_scaled)

# Model 2: Decision Tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train_scaled, y_train)
tree_predictions = tree_model.predict(X_test_scaled)

# Model 3: Random Forest
forest_model = RandomForestClassifier(n_estimators=100)
forest_model.fit(X_train_scaled, y_train)
forest_predictions = forest_model.predict(X_test_scaled)

# Evaluate models
def evaluate_model(model_name, predictions):
    accuracy = accuracy_score(y_test, predictions)
    confusion_mat = confusion_matrix(y_test, predictions)
    classification_rep = classification_report(y_test, predictions)
    
    print(f'{model_name} Model:')
    print(f'Accuracy: {accuracy}')
    print('Confusion Matrix:\n', confusion_mat)
    print('Classification Report:\n', classification_rep)

# Evaluate Logistic Regression model
evaluate_model('Logistic Regression', logistic_predictions)

# Evaluate Decision Tree model
evaluate_model('Decision Tree', tree_predictions)

# Evaluate Random Forest model
evaluate_model('Random Forest', forest_predictions)
