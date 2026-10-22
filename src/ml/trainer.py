class ModelTrainer:

    def train(self, models, X_train, y_train):
        trained = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            trained[name] = model
        return trained
