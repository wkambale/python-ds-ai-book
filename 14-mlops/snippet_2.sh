# Run experiments with different hyperparameters
python train_churn.py --n_estimators 50 --max_depth 5
python train_churn.py --n_estimators 100 --max_depth 10
python train_churn.py --n_estimators 200 --max_depth 20
python train_churn.py --n_estimators 200 --max_depth 10