#MOVIE GENRE CLASSIFICATION
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

#library used to convert raw documents to  matrix of TF-IDF features
from sklearn.feature_extraction.text import TfidfVectorizer#Term Frequency-Inverse Document Frequency

#Naive Bayes algorithm specifically designed for
# classification tasks where the features are discrete counts
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the IMDb dataset (you can download a similar dataset from IMDb or use your own)
# For this example, I assume the dataset has 'plot_summary' and 'genre' columns
# Replace 'your_dataset.csv' with the actual filename
df = pd.read_csv('your_dataset.csv')

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Create TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust the number of features

# Fit and transform the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(train_data['plot_summary'])

# Transform the test data
X_test_tfidf = tfidf_vectorizer.transform(test_data['plot_summary'])

# Map genres to integers for classification
genre_mapping = {genre: idx for idx, genre in enumerate(df['genre'].unique())}
y_train = train_data['genre'].map(genre_mapping)
y_test = test_data['genre'].map(genre_mapping)

# Create and train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test data
predictions = classifier.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
classification_rep = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print('\nClassification Report:\n', classification_rep)
