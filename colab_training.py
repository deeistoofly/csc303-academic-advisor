# Run this file's code in Google Colab (or copy it into a Colab notebook).
# It trains a small demonstration classifier and saves a .pkl model.

import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Small demonstration dataset. Replace/add examples based on sound academic guidance.
rows = [
    ["200 Level","Cybersecurity","Computer Networks","Protect systems","Cybersecurity"],
    ["300 Level","Cybersecurity","Computer Networks","Protect systems","Cybersecurity"],
    ["200 Level","Cybersecurity","Programming","Protect systems","Cybersecurity"],
    ["400 Level","Cybersecurity","Computer Networks","Manage networks","Cybersecurity"],
    ["100 Level","Software Development","Programming","Build applications","Software Development"],
    ["200 Level","Software Development","Programming","Build applications","Software Development"],
    ["300 Level","Software Development","Databases","Build applications","Software Development"],
    ["400 Level","Software Development","Programming","Build applications","Software Development"],
    ["100 Level","Data Science","Mathematics","Analyse data","Data Science"],
    ["200 Level","Data Science","Mathematics","Analyse data","Data Science"],
    ["300 Level","Data Science","Databases","Analyse data","Data Science"],
    ["400 Level","Data Science","Programming","Analyse data","Data Science"],
    ["100 Level","Networking","Computer Networks","Manage networks","Networking"],
    ["200 Level","Networking","Computer Networks","Manage networks","Networking"],
    ["300 Level","Networking","Computer Networks","Manage networks","Networking"],
    ["400 Level","Networking","Databases","Manage networks","Networking"],
    ["200 Level","Cybersecurity","Databases","Protect systems","Cybersecurity"],
    ["300 Level","Software Development","Mathematics","Build applications","Software Development"],
    ["200 Level","Data Science","Programming","Analyse data","Data Science"],
    ["300 Level","Networking","Programming","Manage networks","Networking"],
    ["100 Level","Cybersecurity","Computer Networks","Protect systems","Cybersecurity"],
    ["100 Level","Software Development","Databases","Build applications","Software Development"],
    ["400 Level","Data Science","Mathematics","Analyse data","Data Science"],
    ["400 Level","Networking","Computer Networks","Manage networks","Networking"],
]
columns = ["level", "interest", "subject", "goal", "recommendation"]
df = pd.DataFrame(rows, columns=columns)

X = df[["level", "interest", "subject", "goal"]]
y = df["recommendation"]

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), ["level", "interest", "subject", "goal"])
    ]
)
model = Pipeline([
    ("preprocess", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Small dataset: train on all rows for the demo model; report this limitation in your assignment.
# A larger, independently reviewed dataset is needed for meaningful evaluation.
model.fit(X, y)

with open("academic_advisor_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as academic_advisor_model.pkl")
print("Training rows:", len(df))
print("Note: this is a small demonstration dataset, not a validated academic recommendation model.")
