#4Gewinnt - Bojan & Adam  

---

- Regelmäßige Commits – Zeitstempel
- Verwendung von Branches, mittels pull request wieder in den MainBranch
- Sinnvolle Commit Nachrichten, welche den BestPractices folgen
- Deutsch/Englisch?
- Nur Projektdateien – keine Dateien der Entwicklungsumgebung
- Projektverzeichnis = Rootverzeichnis

---

- Projektstruktur soll matchen mit der LV vorgestellten Struktur
- Heißt zumindest aus einem Package bzw. einem Modul bestehen
- Package und Modulnamen müssen Standards entsprechen
- README.md
   - In 1-2Sätzen beschreiben worum es geht
   - Kurz erläutern wie man das Spiel startet
   - Welche Packages installiert werden müssen falls notwendig

---

- Aufgabenverteilung -> Task_List.md
   - Überlegen wie wir die Aufgabenstellung in unter-Aufgaben aufteilen
   - Einzelne Aufgaben dann zuweisen zur verantwortlichen Person
   - Muss über Projektverlauf hinweg aktualisiert werden
   - MarkdownListe verwenden oder GitHub Issues
   - Eine einmalig erstellte Liste mit 5 Einträgen zu wenig

---

- Planung -> Specifiactions.md
   - Welche Klassen, Methoden und zentrale Attribute, und wie interagieren sie miteinander (Text oder Klassendiagram)
   - Dokumentation von vorab getroffenen Planungsentscheidungen, werden während der Umsetzung Anpassungen vornehmen müssen, diese Anpassungen auch dazu dokumentieren 

--- 

- 4Gewinnt
   - Spielbrettgröße 6 Reihen und 7 Spalten
   - horizontale, vertikale oder diagonale Steine in einer Farbe führen zu Spielgewinn
   - Auswahl ob 2 Menschen gegeneinander oder gegen Computer
   - Nach jedem Spielzug:
      - Überprüfung ob Sieg, wenn ja Ausgabe Siegerin und Spiel beenden
      - Spielbrett anzeigen
      - Nächster Spieler kann Stein spielen oder Spiel beenden
   - Computer-Spieler muss nicht intelligent sein, muss nur gültige Spiele durchführen
   - Doku immer in Kommentaren bzw. Files festhalten!

--- 

- Unit-Tests
   - Automatische Tests für Spielzug- und Gewinnüberprüfung (gültiger Zug, Gewinn-Szenarios…)
   - 100 Prozent Testabdeckung soll erreicht werden
   - Sonderfälle beachten!
   - Andere Teile wie Computer-Gegner, Spielablauf.. müssen nicht getestet werden

--- 

- Docstrings
   - Für alle Klassen, Methoden und Attribute muss docstring Dokumentation im numpy Standard erzeugt werden

--- 

- Theorie-Teil – eigenes File anlegen am besten, zb. .md:
   1.	Sie beginnen als Entwickler*in in einem neuen Unternehmen und bekommen die Verantwortung für ein Modul. Das Modul ist über eine lange Zeit hinweg gewachsen und besteht nur aus sehr wenigen Version 1.0 SEM – AI WS 2024 Christian Hofer Klassen. Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger, und sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch diesen Code? Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten?

   2.	Wählen Sie 2 Design Patterns Ihrer Wahl und umschreiben Sie diese in eigenen Worten. Die Beschreibung muss nicht besonders detailliert sein, sondern nur ganz allgemein Problem und Umsetzung der Lösung bzw. Idee dahinter beschreiben. Mögliche Quelle: https://refactoring.guru/design-patterns/catalog https://www.philipphauer.de/study/se/design-pattern.php Umfang ungefähr ½ - ¾ A4 Seite pro Pattern – Sie müssen das Pattern nicht genau im Detial verstehen. Direkte 1 zu 1 Übersetzungen oder Übernahmen sind nicht erwünscht – Sie können natürlich auch eigene Grafiken zur Unterstützung einbeziehen.
