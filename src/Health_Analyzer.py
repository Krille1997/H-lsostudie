class HealthAnalyzer:
    def __init__(self, df):
        self.df = df

    def berakna_statistik(self, kolumner):
        return self.df[kolumner].agg(["mean", "median", "min", "max"])

    def bootstrap_mean(self, bp_boot, rng):
        pop = rng.choice(bp_boot, size=len(bp_boot), replace=True)
        return pop.mean()