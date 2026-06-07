# Project 2: Data Classification Using AI
# Dataset: Iris Dataset
# Algorithm: K-Nearest Neighbors (KNN)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import os
os.makedirs("outputs", exist_ok=True)

# STEP 1: Load and Understand the Dataset

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("=" * 50)
print("         IRIS DATASET - OVERVIEW")
print("=" * 50)
print(f"\nTotal Samples  : {df.shape[0]}")
print(f"Total Features : {df.shape[1] - 1}")
print(f"Classes        : {list(iris.target_names)}")
print("\nFirst 5 Rows:")
print(df.head())
print("\nBasic Statistics:")
print(df.describe())
print("\nClass Distribution:")
print(df['species'].value_counts())


# STEP 2: Split Data - Training & Testing

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n" + "=" * 50)
print("         TRAIN / TEST SPLIT")
print("=" * 50)
print(f"Training Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")


# STEP 3: Feature Scaling

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# STEP 4: Apply KNN Classification

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# STEP 5: Evaluate the Model

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("         MODEL EVALUATION")
print("=" * 50)
print(f"\nModel Accuracy : {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# STEP 6: Confusion Matrix Plot

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title('Confusion Matrix - KNN Classifier', fontsize=14, fontweight='bold')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.savefig("outputs/confusion_matrix.png", dpi=150)
plt.show()
print("\n[Saved] outputs/confusion_matrix.png")


# STEP 7: Feature Distribution Plot

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
features = iris.feature_names
colors = ['#e74c3c', '#2ecc71', '#3498db']

for idx, feature in enumerate(features):
    ax = axes[idx // 2][idx % 2]
    for i, species in enumerate(iris.target_names):
        ax.hist(df[df['species'] == species][feature],
                alpha=0.7, label=species, color=colors[i], bins=15)
    ax.set_title(feature, fontweight='bold')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()

plt.suptitle('Feature Distribution by Species', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig("outputs/feature_distribution.png", dpi=150)
plt.show()
print("[Saved] outputs/feature_distribution.png")

# STEP 8: KNN Accuracy vs K Value Plot

k_range = range(1, 21)
k_scores = []

for k in k_range:
    knn_k = KNeighborsClassifier(n_neighbors=k)
    knn_k.fit(X_train, y_train)
    k_scores.append(accuracy_score(y_test, knn_k.predict(X_test)))

plt.figure(figsize=(9, 5))
plt.plot(k_range, k_scores, marker='o', color='steelblue', linewidth=2)
plt.title('KNN Accuracy for Different K Values', fontsize=14, fontweight='bold')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy')
plt.xticks(k_range)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/knn_k_values.png", dpi=150)
plt.show()
print("[Saved] outputs/knn_k_values.png")

print("\n" + "=" * 50)
print("   All outputs saved in /outputs folder!")
print("=" * 50)
