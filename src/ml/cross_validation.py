from sklearn.model_selection import cross_val_score

class CrossValidator:

    def evaluate(self, model, X, y, cv=5, scoring=None):
        scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
        return {
            "scores": scores.tolist(),
            "mean": float(scores.mean()),
            "std": float(scores.std())
        }
