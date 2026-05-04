from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_dist = {
    'rf__n_estimators': randint(100, 500),
    'rf__max_depth': [None, 10, 20, 30, 40, 50],
    'rf__min_samples_split': randint(2, 20),
    'rf__min_samples_leaf': randint(1, 10),
    'rf__max_features': ['sqrt', 'log2', None]
}

random_search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_dist,
    n_iter=50,          # Try 50 random combinations
    cv=5,
    scoring='f1',
    n_jobs=-1,
    random_state=42,
    verbose=1
)

# random_search.fit(X_train, y_train)
# print("Best Random Parameters:", random_search.best_params_)