# Theorie Frage 2:

## 1. Singleton Pattern

### Problem  
Es gibt Situationen, in denen es **nur eine einzige Instanz** einer bestimmten Klasse geben soll.  
Beispiele dafür sind:  
- Eine **Datenbankverbindung**, die von allen Teilen des Programms gemeinsam genutzt wird.  
- Ein **Log-System**, das alle Ereignisse zentral speichert.  

Das Problem ist, dass Programme normalerweise mehrere Instanzen einer Klasse erzeugen können.  
Ohne Einschränkungen könnte es passieren, dass mehrere Objekte erstellt werden, was zu unerwarteten Problemen führt.  
Zum Beispiel könnte ein zweites Log-System Nachrichten an eine andere Datei schreiben, sodass Informationen verloren gehen oder falsch sortiert werden.  

### Lösung  
Das **Singleton Pattern** stellt sicher, dass es nur **eine einzige Instanz** einer bestimmten Klasse gibt.  
Das bedeutet, dass alle Teile des Programms auf dieselbe Instanz zugreifen, anstatt eigene neue Objekte zu erstellen.  

Um das zu erreichen:  
- Wird das Erstellen eines neuen Objekts verhindert.  
- Gibt es eine zentrale Möglichkeit, um die einzige vorhandene Instanz abzurufen.  
- Alle, die das Objekt benötigen, erhalten immer dieselbe Instanz.  

Das Singleton-Pattern wird oft verwendet, wenn eine zentrale Steuerung benötigt wird.  
Beispiele aus der Praxis sind Konfigurationsdateien, Protokollierungssysteme oder der Zugriff auf eine gemeinsame Hardware-Ressource.  

---

## 2. Factory Pattern

### Problem  
In einem Programm gibt es oft verschiedene Objekte, die zwar ähnlich sind, aber sich in bestimmten Punkten unterscheiden.  
Das Erstellen dieser Objekte kann schnell unübersichtlich werden, wenn überall im Code genau definiert werden muss, **welches Objekt** wann und wie erzeugt wird.  

Ein Beispiel wäre eine **Software zur Fahrzeugherstellung**:  
Man könnte Autos, Motorräder und LKWs direkt im Code erzeugen.  
Aber dann müsste das Programm genau wissen, wie jedes Fahrzeug hergestellt wird, was den Code kompliziert macht.  

### Lösung  
Das **Factory Pattern** sorgt dafür, dass die Erstellung von Objekten an einer zentralen Stelle geregelt wird.  
Anstatt überall im Code neue Objekte zu erzeugen, kann das Programm eine **Fabrik** (Factory) nutzen.  
Diese Factory entscheidet dann automatisch, **welches Objekt** passend ist und gibt es zurück.  

Das hat mehrere Vorteile:  
- Der Code wird übersichtlicher, weil er sich nicht mehr um die Details der Objekterstellung kümmern muss.  
- Neue Objekttypen können leicht hinzugefügt werden, ohne den bestehenden Code zu ändern.  
- Es gibt eine zentrale Stelle, die für die Erzeugung der Objekte zuständig ist, was die Wartung erleichtert.  

Das Factory-Pattern ist besonders nützlich, wenn ein Programm flexibel bleiben soll.  
Zum Beispiel in einer App, die verschiedene Arten von Benutzern (Admins, normale Nutzer, Gäste) erzeugt, könnte eine Factory automatisch entscheiden, welche Art von Benutzer benötigt wird.  