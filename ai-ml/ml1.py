from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample labeled data: (email_content, label)
data = [
    # Spam emails
    ("Congratulations! You have won a free iPhone", "spam"),
    ("Limited time offer! Buy now and save 50%", "spam"),
    ("Earn money quickly from home!", "spam"),
    ("You are selected for a prize", "spam"),
    ("Cheap loans available instantly", "spam"),
    ("Get Viagra at a discount", "spam"),
    ("Exclusive deal just for you", "spam"),
    ("Click here to claim your reward", "spam"),
    ("Free tickets for a concert", "spam"),
    ("Act now to win cash prizes", "spam"),

    # Not spam emails
    ("Meeting rescheduled to 3 PM tomorrow", "not spam"),
    ("Project report attached for your review", "not spam"),
    ("Please find the invoice for last month", "not spam"),
    ("Team lunch is scheduled next Friday", "not spam"),
    ("Reminder: submit your assignment by Monday", "not spam"),
    ("Your subscription has been renewed successfully", "not spam"),
    ("Regarding your recent inquiry", "not spam"),
    ("Minutes of meeting attached", "not spam"),
    ("Thank you for your feedback", "not spam"),
    ("Monthly performance report", "not spam"),
]

# Separate features (emails) and labels
emails = [email for email, label in data]
labels = [label for email, label in data]

# Convert text data into numerical features using CountVectorizer
# This creates a vocabulary of words and counts their occurrences in each email
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails) # X is a sparse matrix of word counts

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Initialize and train a Naive Bayes classifier (a common choice for text classification)
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)

# Example of predicting on a new email
new_email = ["Special discount just for you!"]
new_email_vectorized = vectorizer.transform(new_email)
prediction = model.predict(new_email_vectorized)
print(f"Prediction for '{new_email[0]}': {prediction[0]}")

'''
In this snippet:
We have a list of emails (emails) and their corresponding labels (labels).
CountVectorizer converts the text into a numerical representation (word counts).
train_test_split divides the data for training and evaluation.
MultinomialNB is a simple classification model.
model.fit() trains the model on the training data.
model.predict() makes predictions on unseen data.
accuracy_score and classification_report help us understand how well the model performs.
'''

'''
import libraries
load the data
seprate the data
convert the tect to numbers
split the data into traning and testing
train the model
evaluate the model
predict a new email
'''