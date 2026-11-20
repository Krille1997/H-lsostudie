import matplotlib.pyplot as plt
from IPython.display import display

class HealthFig:
    def __init__(self, df):
        self.df = df

    def fig_weight_age(self):
        medelvikt = self.df["weight"].mean()

        fig, scatter = plt.subplots()

        scatter.scatter(self.df["age"], self.df["weight"], alpha=0.6)
        scatter.set_title("Ålder och vikt")
        scatter.set_xlabel("Ålder")
        scatter.set_ylabel("Vikt - KG")
        scatter.axhline(y=medelvikt, color="red", label="Medelvikt")
        plt.tight_layout()
        scatter.legend()
        fig.savefig("../Figures/age_weight.png", dpi=150)
        plt.show()

    def fig_smoker_disease(self):
        smoker_disease = self.df.groupby("smoker")["disease"].mean() * 100
        
        fig, bar = plt.subplots()
        
        bar.bar(smoker_disease.index, smoker_disease.values)
        bar.set_title("Rökning och sjukdom")
        bar.set_xlabel("Rökare")
        bar.set_ylabel("Procentandel med sjukdom (%)")
        bar.grid(axis="y")
        plt.tight_layout()
        fig.savefig("../Figures/smoker_disease.png", dpi=150)
        plt.show()

    def fig_smoker_bp(self):
        smoker_bp = self.df.groupby("smoker")["systolic_bp"].mean()

        display(smoker_bp.round(2))

        fig, bar = plt.subplots()
        
        bar.bar(smoker_bp.index, smoker_bp.values)
        bar.set_title("Genomsnittliga systoliska blodtrycket hos rökare och icke-rökare")
        bar.set_xlabel("Rökare")
        bar.set_ylabel("Medelblodtryck")
        bar.grid(axis="y")
        plt.tight_layout()
        fig.savefig("../Figures/blodtryck hos rökare.png", dpi=150)
        plt.show()

    def fig_regression(self, blodtryck, prediktion, residualer):
          fig, scatter = plt.subplots()

          scatter.scatter(prediktion, residualer, alpha=0.5)
          scatter.axhline(y=0, color="red", linestyle="--")
          scatter.set_title("Residualdiagram")
          scatter.set_xlabel("Förväntat blodtryck")
          scatter.set_ylabel("Residualer")
          fig.savefig("../Figures/regression.png", dpi=150)
          plt.show()

    def fig_regression_2(self, blodtryck, prediktion):
        fig, scatter = plt.subplots()
        
        scatter.scatter(prediktion, blodtryck, alpha=0.5)
        
        scatter.plot(
            [blodtryck.min(), blodtryck.max()],
            [blodtryck.min(), blodtryck.max()],
            color="red",
            linestyle="--"
            )

        scatter.set_title("Verkligt och beräknat blodtryck")
        scatter.set_xlabel("Beräknat blodtryck")
        scatter.set_ylabel("Verkligt blodtryck")
        fig.savefig("../Figures/regression_2.png", dpi=150)
        plt.show()