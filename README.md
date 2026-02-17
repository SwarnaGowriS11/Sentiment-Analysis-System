# Sentiment-Analysis-System
This project performs sentiment classification on Twitter data using the Sentiment140 dataset (1.6 million tweets). The goal is to automatically determine whether a tweet expresses positive or negative sentiment using Natural Language Processing (NLP) and Machine Learning techniques.
The project demonstrates a complete end-to-end NLP pipeline, from raw data to model deployment.

Objectives
Clean and preprocess unstructured tweet text
Convert text data into meaningful numerical representations
Train and evaluate a sentiment classification model
Enable real-time sentiment prediction

Dataset Information
Dataset Name: Sentiment140
Size: 1.6 million tweets
Labels:
0 → Negative
4 → Positive
Features Used: Tweet text

Methodology
1)Data Preprocessing
Converted text to lowercase
Removed URLs and user mentions (@username)
Removed punctuation and special characters
Removed stopwords
Tokenized text

2) Feature Engineering
Applied TF-IDF Vectorization
Converted text into numerical feature vectors
Optimized feature dimensions for better performance

3) Model Training
Algorithm: Logistic Regression
Binary classification (Positive / Negative)
Trained on large-scale dataset
Model saved using pickle

4) Deployment (Flask-based Web App)
Built a simple web interface
User inputs tweet text
Model predicts sentiment in real-time

Tech Stack
Python
Pandas
NumPy
Scikit-learn
NLP (Regex, Stopword Removal)
TF-IDF Vectorizer
Logistic Regression
Flask
Pickle

Model Performance
Binary Sentiment Classification
Efficient training on large dataset
Optimized preprocessing pipeline
