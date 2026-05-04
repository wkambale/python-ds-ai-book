from sklearn.tree import DecisionTreeClassifier, plot_tree

def train_decision_tree(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    max_depth: int = 5
) -> Tuple[DecisionTreeClassifier, Dict[str, float]]:
    """
    Trains a decision tree classifier.

    Args:
        X_train: Training features (unscaled is fine for trees).
        X_test: Test features.
        y_train: Training labels.
        y_test: Test labels.
        max_depth: Maximum depth of the tree.
    """
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, zero_division=0),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred)
    }
    return model, metrics

# Train decision trees with different depths
print("Decision Tree Performance by Max Depth:")
for depth in [3, 5, 7, 10, None]:
    _, metrics = train_decision_tree(
        X_train_unscaled, X_test_unscaled, y_train, y_test, max_depth=depth
    )
    depth_str = str(depth) if depth else "Unlimited"
    print(f"  Depth {depth_str}: F1={metrics['F1-Score']:.3f}, AUC={metrics['AUC']:.3f}")