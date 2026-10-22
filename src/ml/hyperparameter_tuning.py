from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

class HyperparameterTuner:

    def grid_search(self, model, params, X_train, y_train, cv=5, scoring=None):
        search = GridSearchCV(model, params, cv=cv, scoring=scoring, n_jobs=-1)
        search.fit(X_train, y_train)
        return search

    def randomized_search(self, model, params, X_train, y_train, cv=5, scoring=None, n_iter=20):
        search = RandomizedSearchCV(
            model,
            params,
            cv=cv,
            scoring=scoring,
            n_iter=n_iter,
            random_state=42,
            n_jobs=-1
        )
        search.fit(X_train, y_train)
        return search
