#SPAM SMS DETECTION
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

#library used to convert raw documents to  matrix of TF-IDF features
#Term Frequency-Inverse Document Frequency
from sklearn.feature_extraction.text import TfidfVectorizer



#Naive Bayes algorithm specifically designed for
# classification tasks where the features are discrete counts
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
#importing Support Vector Classification
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the SMS Spam Collection dataset (replace 'sms_spam_dataset.csv' with your dataset)
df = pd.read_csv('sms_spam_dataset.csv', encoding='latin-1')
df = df[['v1', 'v2']]  # Selecting only the relevant columns
df.columns = ['label', 'message']

# Map labels to integers (0 for 'ham' and 1 for 'spam')
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Create TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust the number of features

# Fit and transform the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Model 1: Naive Bayes
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)
nb_predictions = nb_classifier.predict(X_test_tfidf)

# Model 2: Logistic Regression
lr_classifier = LogisticRegression()
lr_classifier.fit(X_train_tfidf, y_train)
lr_predictions = lr_classifier.predict(X_test_tfidf)

# Model 3: Support Vector Machine (SVM)
svm_classifier = SVC()
svm_classifier.fit(X_train_tfidf, y_train)
svm_predictions = svm_classifier.predict(X_test_tfidf)

# Evaluate models
def evaluate_model(model_name, predictions):
    accuracy = accuracy_score(y_test, predictions)
    classification_rep = classification_report(y_test, predictions)
    
    print(f'{model_name} Model:')
    print(f'Accuracy: {accuracy}')
    print('Classification Report:\n', classification_rep)

# Evaluate Naive Bayes model
evaluate_model('Naive Bayes', nb_predictions)

# Evaluate Logistic Regression model
evaluate_model('Logistic Regression', lr_predictions)

# Evaluate SVM model
evaluate_model('Support Vector Machine', svm_predictions)
