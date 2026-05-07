# SVM Assignment – Iris Dataset

A Support Vector Machine classifier built on the classic Iris dataset.

## Requirements

```
pandas, numpy, matplotlib, seaborn, scikit-learn
```

## What It Does

1. Load Data – Iris dataset via `sns.load_dataset('iris')`
2. EDA – Pairplot and KDE plot (Setosa sepal length vs width)
3. Train/Test Split – 70/30 split
4. Train SVC – Default `SVC()` from scikit-learn
5. Evaluate – Confusion matrix and classification report (~98% accuracy)
6. GridSearchCV – Tunes `C` and `gamma` parameters; results match baseline

bash
jupyter notebook 02-SVM_Assignment.ipynb

Both the baseline SVC and the tuned GridSearch model achieve **~98% accuracy**. The Iris dataset is small and clean, so default parameters are already near-optimal.
