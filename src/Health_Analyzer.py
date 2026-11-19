import numpy as np
from scipy.stats import ttest_ind

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