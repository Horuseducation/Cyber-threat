# train_model.py
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib

# Create synthetic dataset for demo
# We'll simulate 8 numeric features that represent simplified network metrics
X, y = make_classification(
    n_samples=3000,
    n_features=8,
    n_informative=6,
    n_redundant=1,
    n_clusters_per_class=2,
    weights=[0.8, 0.2],
    random_state=42
)

# Convert to DataFrame with friendly column names
cols = ["duration", "src_bytes", "dst_bytes", "wrong_fragment", "urgent", "count", "srv_count", "time_window"]
df = pd.DataFrame(X, columns=cols)
df["label"] = y

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df[cols], df["label"], test_size=0.2, random_state=42, stratify=df["label"])

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Evaluate
pred = clf.predict(X_test_scaled)
acc = accuracy_score(y_test, pred)
print("Test accuracy:", acc)
print(classification_report(y_test, pred))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))

# Save model and scaler
joblib.dump(clf, "model_rf.joblib")
joblib.dump(scaler, "scaler.joblib")
print("Saved model_rf.joblib and scaler.joblib")
