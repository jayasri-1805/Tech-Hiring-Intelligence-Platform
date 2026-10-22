from .classification_metrics import classification_metrics

class ClassificationEvaluator:

    def evaluate(self, models, X_test, y_test):
        results = {}
        for name, model in models.items():
            preds = model.predict(X_test)
            results[name] = classification_metrics(y_test, preds)
        return results
