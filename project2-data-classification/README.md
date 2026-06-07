# 🌸 Project 2: Data Classification Using AI

## Overview
A beginner-friendly machine learning project that builds a classification model using the **Iris Dataset** and the **K-Nearest Neighbors (KNN)** algorithm.

---

## 🎯 Goal
Build a basic classification model using a small dataset, apply a supervised learning algorithm, and evaluate its performance.

---

## 📁 Project Structure
```
project2-data-classification/
│
├── classification_model.py   # Main Python script
├── requirements.txt          # Required libraries
├── README.md                 # Project documentation
└── outputs/
    ├── confusion_matrix.png       # Model evaluation heatmap
    ├── feature_distribution.png   # Dataset visualization
    └── knn_k_values.png           # Accuracy vs K plot
```

---

## 📊 Dataset
- **Name:** Iris Dataset
- **Source:** `sklearn.datasets`
- **Samples:** 150
- **Features:** 4 (sepal length, sepal width, petal length, petal width)
- **Classes:** 3 (Setosa, Versicolor, Virginica)

---

## ⚙️ Key Steps
1. Load and explore the dataset
2. Split into training (80%) and testing (20%) sets
3. Apply feature scaling
4. Train a KNN Classifier (k=5)
5. Evaluate with accuracy score and classification report
6. Visualize results with plots

---

## ✅ Results
| Metric | Value |
|--------|-------|
| Algorithm | K-Nearest Neighbors |
| Test Size | 20% (30 samples) |
| Accuracy | ~100% |

---

## 🛠️ Key Skills Used
- Data handling with `pandas` and `numpy`
- Supervised learning basics
- Model training and evaluation with `scikit-learn`
- Data visualization with `matplotlib` and `seaborn`

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python classification_model.py
```

---

## 📦 Requirements
See `requirements.txt`
