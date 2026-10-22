import json

class EvaluationReport:
    def save(self, results, path="reports/model_results.json"):
        with open(path,"w") as f:
            json.dump(results,f,indent=4)
