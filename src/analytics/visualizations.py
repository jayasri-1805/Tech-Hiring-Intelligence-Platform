import matplotlib.pyplot as plt

class VisualizationPipeline:

    def salary_distribution(self, df):
        plt.figure(figsize=(8,5))
        df["salary_midpoint"].hist(bins=30)
        plt.title("Salary Distribution")
        plt.xlabel("Salary Midpoint")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

    def jobs_by_country(self, df):
        plt.figure(figsize=(10,5))
        df["country"].value_counts().head(10).plot(kind="bar")
        plt.title("Top 10 Countries by Jobs")
        plt.tight_layout()
        plt.show()
