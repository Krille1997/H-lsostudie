def berakna_statistik(df, kolumner):
    return df[kolumner].agg(["mean", "median", "min", "max"])