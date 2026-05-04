from sklearn.model_selection import GridSearchCV, train_test_split

# First, split data (assuming X, y from previous chapter's churn dataset)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )

# Define the grid
# Note: Use double underscore 'rf__n_estimators' to target the pipeline step
param_grid = {
    'rf__n_estimators': [100, 200, 300],
    'rf__max_depth': [None, 10, 20],
    'rf__min_samples_split': [2, 5]
}

# Setup Grid Search with 5-fold Cross-Validation
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,      # Use all CPU cores
    verbose=1       # Show progress
)

# Fit on Training Data
# grid_search.fit(X_train, y_train)

# print("Best Parameters:", grid_search.best_params_)
# print("Best CV F1 Score:", grid_search.best_score_)
# print("Test F1 Score:", grid_search.score(X_test, y_test))