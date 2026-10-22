from .metrics import regression_metrics

class ModelEvaluator:

    def evaluate(self, models, X_test, y_test):
        results = {}
        for name, model in models.items():
            preds = model.predict(X_test)
            results[name] = regression_metrics(y_test, preds)
        return results
