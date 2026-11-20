# Hälsostudie – Individuell uppgift

## Om projektet

I detta projekt analyserar jag hälsodata från 800 personer. Syftet är att undersöka samband mellan bland annat ålder, vikt, rökning och blodtryck.

## Del 1 – Statistik

I första delen har jag arbetat med:

- Beräknat beskrivande statistik som medelvärde, median, min och max.
- Skapat tre grafer för att visa olika samband i datan.
- Simulerat hälsodata med NumPy.
- Beräknat 95 % konfidensintervall med normalapproximation och bootstrap.
- Gjort ett t-test för att undersöka om rökare har högre blodtryck än icke-rökare.
- Genomfört en power-simulering för att undersöka hur ofta testet hittar en skillnad.

## Del 2 – Fördjupning

I andra delen har jag:

- Delat upp koden i funktioner och moduler
- Skapat klassen `HealthAnalyzer` för statistiska beräkningar
- Skapat klassen `HealthFig` för grafer
- Använt multipel linjär regression med ålder och vikt för att undersöka blodtrycket
- Skapat ett residualdiagram och en graf som jämför verkligt och beräknat blodtryck

## Projektstruktur

- `Data/` – Hälsodatasetet
- `Notebook/Report.ipynb` – Rapport med kod, grafer och förklaringar
- `src/Health_Analyzer.py` – Funktioner för statistik och analyser
- `src/Health_Fig.py` – Funktioner för visualiseringar
- `Figures/` – Sparade grafer
- `requirements.txt` – Bibliotek som används i projektet

## Installation och körning

1. Ladda ner projektet från GitHub.
2. Installera biblioteken med `pip install -r requirements.txt`.
3. Öppna `Notebook/Report.ipynb` i VS Code.
4. Välj rätt Python-miljö.
5. Kör notebooken från början till slut med **Restart & Run All**.

## Python-version

Python-version: **Fyll i din Python-version här.**