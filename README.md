# Project Overview

This project explores a machine learning workflow to build, train, and evaluate a classification model, focusing on Support Vector Machines (SVM). The project includes data preprocessing, model training, hyperparameter tuning, evaluation, and inference. It is divided into two Jupyter Notebooks:

- **P1M2_Joni.ipynb**: Main notebook covering model training, evaluation, and analysis.
- **P1M2_Joni_inf.ipynb**: Inference notebook for deploying the model on new data.

## Key Features

1. **Data Preprocessing**:
   - Handling missing values and encoding categorical variables.
   - Splitting the dataset into training and testing subsets.

2. **Model Development**:
   - Training an SVM classifier.
   - Performing hyperparameter tuning to optimize model performance.

3. **Evaluation Metrics**:
   - Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
   - Detailed ROC curve analysis for both training and testing datasets.

4. **Model Insights**:
   - AUC scores of 0.87 (train) and 0.85 (test) indicate strong generalization and no significant overfitting.
   - The model reliably distinguishes between classes.

5. **Model Deployment**:
   - Saving the trained SVM model using Python's `pickle` library.
   - Deployment-ready inference through the `P1M2_Joni_inf.ipynb` notebook.

6. **Conceptual Discussions**:
   - Explanation of key concepts such as Bagging, Boosting, Random Forest, and Cross-Validation.
   - Detailed comparisons and practical implications of these concepts.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher.
- Libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `pickle`.

### Installation
1. Clone this repository.
2. Install the required packages using:
   ```bash
   pip install -r requirements.txt

---
## Hugging Face Visualization
   
      https://huggingface.co/spaces/radityaruan/M2




