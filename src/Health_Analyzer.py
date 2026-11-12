def berakna_statistik(df, kolumner):
    return df[kolumner].agg(["mean", "median", "min", "max"])

def bootstrap_mean(bp_boot, rng):
    pop = rng.choice(bp_boot, size=len(bp_boot), replace=True)
    return pop.mean()