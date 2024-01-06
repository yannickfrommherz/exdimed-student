# How to: Live Coding mit VS Code

Die [*Live Share*](https://code.visualstudio.com/learn/collaboration/live-share) Erweiterung in [VS Code](https://code.visualstudio.com) ermöglicht 

- als *Host* die *eigene, lokale Programmierumgebung* mit anderen Personen übers Internet zu teilen bzw. 
- als *Gast* der Programmierumgebung eines Hosts beizutreten.

## Anwendungsfälle

Live Share lohnt sich insbesondere in diesen zwei Szenarien:

- Ein Host schreibt, erklärt und führt Code aus, während Gäste ihm dabei folgen, ohne selbst zu coden.
- Host und Gäste coden gemeinsam in derselben Programmierumgebung.

## Good to know

**Start einer Live Coding Session**

- Der Host wird beim Teilen seiner Programmierumgebung über `Share` in der Live-Share Erweiterung in VS Code zum Einloggen mit einem GitHub- oder Microsoft-Account aufgefordert.
- Gäste können uneingeloggt der geteilten Programmierumgebung über einen Link im Browser oder, besser, über `Join` sowie den Link in der Live-Share Erweiterung im eigenen VS Code-Programm beitreten.
- Gäste sollten sich einen sinnvollen Namen geben, damit der Host Gäste bei Bedarf identifizieren kann, etwa um ihnen Schreibrechte zu erteilen.
- Der Host muss die Gäste standardmäßig einzeln eintreten lassen.

**Folgemodus**

- Gäste folgen zu Beginn automatisch den Mausbewegungen des Hosts.
- Um einer Person zu folgen bzw. nicht mehr zu folgen, einfach auf den Namen der Person unter `Participants` klicken. 
- Zwei Personen sollten sich nicht gegenseitig folgen, denn so entstehen hektische Rückkopplungen.
- Über einen Rechtsklick auf eine Person unter `Participants` kann diese auf die Stelle im Code, an der man sich selbst gerade befindet, *fokussiert* werden. Fokussierung aktiviert auch den Folgemodus.  

**Berechtigungen**

- Gäste haben zu Beginn nur Leserechte, können aber Schreibrechte anfordern. Der Host kann Gästen auch unaufgefordert Schreibrechte erteilen (über einen Rechtsklick auf die jeweilige Person unter `Participants`).
- Gäste müssen außerdem die Berechtigung zum Ausführen von Code anfragen.

**Weiteres**

- Über einen *Session Chat* können Teilnehmende miteinander kommunizieren. 
- Nur der Host kann bei Bedarf den Kernel neustarten. Da die Live Share Session auf der lokalen Programmierumgebung des Hosts basiert, betrifft ein Kernelneustart auch die virtuellen Programmierumgebungen der Gäste.
- Neue Dateien und Ordner können während einer Live Share Session erstellt werden. Diese werden effektiv auf dem Rechner des Hosts geschaffen.
