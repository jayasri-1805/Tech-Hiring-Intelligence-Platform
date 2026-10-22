from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


class ModelFactory:

    def get_models(self):

        return {

            "Linear Regression":

                LinearRegression(),

            "Decision Tree":

                DecisionTreeRegressor(
                    random_state=42,
                    max_depth=15,
                ),

            "Random Forest":

                RandomForestRegressor(
                    n_estimators=50,
                    max_depth=12,
                    random_state=42,
                    n_jobs=-1,
                ),
        }