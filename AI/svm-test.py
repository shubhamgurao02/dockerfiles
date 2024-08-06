from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Sample dataset
questions = ["What is the capital of Germany?", "Who composed the Symphony No. 5 in C minor?"]
answers = ["Berlin", "Ludwig van Beethoven"]

# Create the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the questions to TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(questions)

# New question to predict the answer for
new_question = "What is the population of France?"
new_question_vector = tfidf_vectorizer.transform([new_question])

# Create and train the SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(tfidf_matrix, answers)

# Predict the answer for the new question
predicted_answer = svm_classifier.predict(new_question_vector)[0]
print("Predicted Answer:", predicted_answer)
