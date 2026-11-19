# Hälsostudie – Individuell uppgift

Python 3.14.7 för att analysera datan och skapat tabeller och diagram för att visa resultaten.

## Projekt/mappstruktur

* Data/ – Innehåller CSV-filen

* Notebooks/Report.ipynb – Här finns vår rapport med analyser och diagram.

* src/ – Innehåller funktioner som används i rapporten.

* requirements.txt – Bibliotek som behövs för att köra projektet.

## Så kör du projektet

* Ladda ner projektet från GitHub.

* Öppna projektet i Visual Studio Code.

* Installera biblioteken med pip install -r requirements.txt.

* Öppna notebooks/report.ipynb och kör cellerna uppifrån och ned.

## Del 1 – Grundläggande analys och statistik

### G-krav

1. Beskrivande analys
- Beräkna medelvärde, median, min och max för age, weight, height, systolic_bp och cholesterol.
- Skapa minst 3 olika grafer.

2. Simulering
- Beräkna andelen personer med sjukdom.
- Simulera 1000 personer med NumPy (random + seed).
- Jämför simulerad andel med verklig andel.

3. Konfidensintervall
- Beräkna konfidensintervall för medelvärdet av systolic_bp.

4. Hypotesprövning
- Testa om rökare har högre medelblodtryck än icke-rökare.
- Använd exempelvis bootstrap eller t-test.
- Förklara resultatet i Markdown.

### VG-krav

1. Beräkna konfidensintervall med två olika metoder och jämför resultaten.
2. Gör en power-simulering för att undersöka hur säkert hypotesprövningen upptäcker en verklig skillnad.
3. Motivera metodval i Markdown och hänvisa till dokumentation eller annan källa.

## Inlämning

- All kod, grafer och förklaringar ska finnas i Jupyter Notebook.
- Del 1 lämnas in via GitHub på branch del1.
- Del 2 lämnas in via GitHub på branch del2.

Del 2 – Fördjupning och pipeline

För G ska du göra:

Strukturera koden
- Flytta delar av din kod från del 1 till funktioner och moduler.
- Skapa minst en klass (t.ex. HealthAnalyzer) som kan utföra någon del av analysen (t.ex. beräkna statistik eller rita grafer).

Linjär algebra i praktiken
- Använd numpy eller scikit-learn för en analys som bygger på matriser/vektorer.
- Exempel:
- En enkel linjär regression för att förutsäga blodtryck från ålder eller vikt.
- PCA för att hitta mönster i datan.

Utökad analys och visualisering
- Lägg till minst en ny analys eller graf som ger en djupare förståelse (t.ex. relationen mellan blodtryck och ålder, eller sjukdomsförekomst per kön).

Dokumentation
- Skriv docstrings till dina funktioner/klasser.
- Använd markdown-rutor för att förklara vad du gör och varför.

För VG ska du även göra:
- Bygg en mer utvecklad klass som kan hantera flera olika analyser eller visualiseringar.
- Använd en mer avancerad metod (t.ex. multipel regression) eller en extra visualisering som tydligt förklarar resultaten.
- Motivera dina metodval i markdown och hänvisa till dokumentation eller annan källa.