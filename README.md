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
- Skapat klassen "HealthAnalyzer" för statistiska beräkningar
- Skapat klassen "HealthFig" för grafer
- Använt multipel linjär regression för att undersöka sambandet mellan ålder, vikt och blodtryck.
- Skapat två nya grafer som visar hur bra modellen räknar ut blodtrycket.
- Använt residualer för att se hur mycket modellen räknar fel.

## Projektstruktur

Projektet är uppdelat i följande mappar:

- Data innehåller datasetet.
- Figures innehåller sparade grafer.
- Notebook innehåller rapporten Report.ipynb.
- src innehåller två Python-filer:
  - Health_Analyzer.py används för beräkningar och analyser.
  - Health_Fig.py används för att skapa grafer.
- README.md beskriver projektet.
- requirements.txt innehåller biblioteken som behövs.

## Köra projektet

1. Ladda ner projektet från GitHub.
2. Installera biblioteken med pip install -r requirements.txt.
3. Öppna Notebook/Report.ipynb i VS Code.
4. Välj rätt Python-miljö.
5. Kör alla celler med Restart & Run All.

## Python-version

Projektet är gjort med Python 3.14.7.