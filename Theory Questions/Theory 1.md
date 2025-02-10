# Theorie Frage 1:

## Nachteile von langem und schlecht dokumentiertem Code
- Schwer verständlich
   - Wenn Methoden hunderte Zeilen lang sind, dauert es lange, bis du verstehst, was passiert.

- Fehler sind schwer zu finden
   - Ohne gute Struktur und Kommentare wird das Debuggen (Fehler finden und beheben) mühsam.

- Änderungen sind riskant
  - Wenn du eine kleine Änderung machst, kann es unerwartete Folgen haben.

- Zusammenarbeit wird schwierig
   - Andere Entwickler brauchen lange, um sich in den Code einzuarbeiten.

- Tests sind kompliziert
   - Große Methoden lassen sich nicht leicht testen, weil zu viele Dinge gleichzeitig passieren.

## Welche Prinzipien werden nicht eingehalten?
- Single Responsibility Principle (SRP)
   - Eine Methode sollte nur eine einzige Aufgabe haben. Lange Methoden machen oft zu viel auf einmal.

- KISS (Keep It Simple, Stupid)
   - Code sollte so einfach wie möglich sein. Lange Methoden sind meist unnötig kompliziert.

- DRY (Don't Repeat Yourself)
   - Gleiche Code-Blöcke sollten nicht mehrfach vorkommen. In langen Methoden gibt es oft Wiederholungen.

- Modularität
   - Der Code sollte in kleine, wiederverwendbare Bausteine unterteilt sein.