import numpy as np
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    def __init__(self, df):
        self.df = df

    def berakna_statistik(self, kolumner):
        return self.df[kolumner].agg(["mean", "median", "min", "max"])

    def normalapproximation(self):
         bp = self.df["systolic_bp"]
         
         n = len(bp)
         medelvärde = bp.mean()
         std = bp.std()
         se = std / np.sqrt(n)

         under = medelvärde - 1.96 * se
         upper = medelvärde + 1.96 * se
         
         return medelvärde, under, upper

    def bootstrap_mean(self, bp_boot, rng):
        pop = rng.choice(bp_boot, size=len(bp_boot), replace=True)
        return pop.mean()
    def bootstrap_intervall(self):
         bp_boot = self.df["systolic_bp"].to_numpy()
         rng = np.random.default_rng(42)
         
         R = 1000
         
         means_n1000 = np.array([self.bootstrap_mean(bp_boot, rng) for _ in range(R)])
         
         under_boot = np.percentile(means_n1000, 2.5)
         upper_boot = np.percentile(means_n1000, 97.5)

         return under_boot, upper_boot
    
    def hypotes_test(self):
            smoker = self.df.loc[self.df["smoker"] == "Yes", "systolic_bp"]
            non_smoker = self.df.loc[self.df["smoker"] == "No", "systolic_bp"]

            t_stat, p_value = ttest_ind(
                smoker,
                non_smoker,
                equal_var=False,
                alternative="greater"
            )

            return smoker, non_smoker, t_stat, p_value

    def power_sim(self):
        smoker = self.df.loc[self.df["smoker"] == "Yes", "systolic_bp"]
        non_smoker = self.df.loc[self.df["smoker"] == "No", "systolic_bp"]

        antal_skillnad = 0
        R = 1000

        for i in range(R):
            sim_smoker = smoker.sample(n=len(smoker), replace=True)
            sim_non_smoker = non_smoker.sample(n=len(non_smoker), replace=True)

            sim_smoker = sim_smoker - smoker.mean() + non_smoker.mean() + 2

            t_stat, p_value = ttest_ind(
                sim_smoker,
                sim_non_smoker,
                equal_var=False,
                alternative="greater"
            )

            if p_value < 0.05:
                antal_skillnad += 1

        power = antal_skillnad / R
        return power, antal_skillnad

    def regression(self):
         age_weight = self.df[["age", "weight"]]
         blodtryck = self.df["systolic_bp"]

         model = LinearRegression()
         model.fit(age_weight, blodtryck)

         return model, age_weight, blodtryck