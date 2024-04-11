import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from sklearn.preprocessing import KBinsDiscretizer, PolynomialFeatures
from sklearn.pipeline import Pipeline
from scipy.stats import randint

# Load the necessary columns from the train.csv
df = pd.read_csv('data/train.csv', usecols=['ID', 'LABEL'])

# Ensure stratified split to maintain class distribution
X_train, X_test, y_train, y_test = train_test_split(df[['ID']], df['LABEL'], test_size=0.2, stratify=df['LABEL'], random_state=42)

# Define a pipeline with KBinsDiscretizer, PolynomialFeatures, and a placeholder for RandomForestClassifier
pipeline = Pipeline([
    ('binning', KBinsDiscretizer(n_bins=10, encode='onehot', strategy='uniform')),
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('clf', RandomForestClassifier(class_weight='balanced', random_state=42))
])

# Parameter distribution for RandomizedSearchCV
param_dist = {
    'clf__n_estimators': randint(100, 500),
    'clf__max_depth': randint(3, 20),
    'clf__min_samples_split': randint(2, 11),
    'clf__min_samples_leaf': randint(1, 11),
    'clf__max_features': ['auto', 'sqrt', 'log2', None]
}

# Perform random search
random_search = RandomizedSearchCV(pipeline, param_distributions=param_dist, n_iter=10, cv=3, scoring='f1_macro', verbose=2, random_state=42)
random_search.fit(X_train, y_train)

# Best parameters and score
print("Best parameters found: ", random_search.best_params_)
print("Best F1 score found: ", random_search.best_score_)

# Evaluate the best model on the test set
best_model = random_search.best_estimator_
predictions = best_model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='macro')
precision = precision_score(y_test, predictions, average='macro')
recall = recall_score(y_test, predictions, average='macro')
conf_matrix = confusion_matrix(y_test, predictions)

# Print metrics
print(f"Test Accuracy: {accuracy}")
print(f"Test F1 Score (Macro): {f1}")
print(f"Test Precision (Macro): {precision}")
print(f"Test Recall (Macro): {recall}")
print("Test Confusion Matrix:")
print(conf_matrix)


# Calculate metrics
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='macro')
precision = precision_score(y_test, predictions, average='macro')
recall = recall_score(y_test, predictions, average='macro')
conf_matrix = confusion_matrix(y_test, predictions)

# Print metrics
print(f"Accuracy: {accuracy}")
print(f"F1 Score (Macro): {f1}")
print(f"Precision (Macro): {precision}")
print(f"Recall (Macro): {recall}")
print("Confusion Matrix:")
print(conf_matrix)
