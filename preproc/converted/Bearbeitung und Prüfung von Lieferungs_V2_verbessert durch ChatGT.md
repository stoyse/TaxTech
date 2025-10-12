**Arbeitsanweisung**

**Bearbeitung und Prüfung von Lieferungs- und Leistungseingangsrechnungen**

**Unternehmen:** Heiß &amp; Laut Maschinenbau GmbH **Fachbereich:** Rechnungswesen / Buchhaltung **Gültig ab:** [TT.MM.JJJJ] **Version:** 1.0 **Erstellt durch:** [Name] **Geprüft / Freigegeben durch:** [Name]

**1. Zweck und Ziel der Arbeitsanweisung**

Diese Arbeitsanweisung beschreibt die Vorgehensweise bei der Bearbeitung, Prüfung, Freigabe und Archivierung von Lieferungs- und Leistungseingangsrechnungen bei der Heiß &amp; Laut Maschinenbau GmbH.
Ziel ist, dass alle eingehenden Rechnungen vollständig, korrekt, nachvollziehbar und in Übereinstimmung mit den steuerlichen Anforderungen (insbesondere GoBD, § 14 UStG, HGB) verarbeitet werden.

Der Prozess soll sicherstellen, dass keine unberechtigten Zahlungen erfolgen, alle steuerlich relevanten Daten ordnungsgemäß erfasst werden und die interne Kontrolle über Rechnungsprüfung und Zahlungsfreigabe gewährleistet ist.

**2. Geltungsbereich**

Diese Arbeitsanweisung gilt für sämtliche Eingangsrechnungen über Lieferungen und Leistungen, die von Lieferanten, Dienstleistern oder sonstigen Geschäftspartnern an die Heiß &amp; Laut Maschinenbau GmbH übermittelt werden.
Dabei spielt es keine Rolle, ob die Rechnung per Post, per E-Mail oder über elektronische Schnittstellen (z. B. automatisierte Lieferantenportale) eingeht.

Sie betrifft insbesondere die Mitarbeitenden der Poststelle bzw. des Rechnungseingangs, der Buchhaltung, der Fachabteilungen sowie die freigabeberechtigten Personen.

**3. Beschreibung des Prozesses**

**3.1 Rechnungseingang und Erfassung**

Rechnungen treffen bei Heiß &amp; Laut entweder per Post oder per E-Mail ein.
Papierrechnungen werden in der Poststelle entgegengenommen, auf Vollständigkeit (Seiten, Anhänge, Anlagen) und Lesbarkeit geprüft und anschließend über den zentralen Scanner digitalisiert. Die gescannte Datei wird im elektronischen Rechnungseingangssystem gespeichert und erhält eine eindeutige Dokumenten-ID.

Eingehende E-Mails mit Rechnungsanhang werden automatisch von der zentralen Rechnungseingangsadresse (z. B. rechnungen@heissundlaut.de) in das Dokumentenmanagementsystem (DMS) übertragen. Das System extrahiert die Metadaten (z. B. Absender, Datum, Rechnungsnummer, Betrag) und übergibt diese an das SAP-System.

Nach der Erfassung werden die Belege an die Buchhaltung weitergeleitet, wo die formelle Prüfung erfolgt.

**3.2 Formelle Prüfung durch die Buchhaltung**

Die Buchhaltung öffnet die übermittelte Rechnung im SAP-System – abhängig von der Art der Rechnung entweder im Modul **MIRO (Eingangsrechnung mit Bestellbezug)** oder **FB60 (sonstige Rechnung)** .

Dort werden die Pflichtangaben gemäß § 14 UStG überprüft, also insbesondere:

- vollständiger Name und Anschrift von Lieferant und Heiß &amp; Laut Maschinenbau GmbH,
- Steuernummer oder Umsatzsteuer-Identifikationsnummer,
- fortlaufende Rechnungsnummer,
- Rechnungsdatum,
- Leistungsbeschreibung, Menge, Preis,
- Umsatzsteuerbetrag und -satz.

Das System prüft automatisch, ob die Rechnung bereits im System vorhanden ist (Duplikatsprüfung). Falls eine Dublette erkannt wird, stoppt die Verarbeitung und die Buchhaltung prüft manuell.
Wenn formale Angaben fehlen oder unplausibel sind (z. B. fehlerhafte Steuernummer, unvollständige Adressdaten), informiert die Buchhaltung den Lieferanten per E-Mail und bittet um Korrektur.

Fehlerhafte oder unvollständige Rechnungen werden nicht weiterbearbeitet, bis eine korrigierte Version eingeht. Sobald die formelle Prüfung ohne Beanstandung abgeschlossen ist, wird die Rechnung zur weiteren Bearbeitung (Prüfung auf Bestellbezug) freigegeben.

**3.3 Prüfung auf Bestellbezug oder Vertragszuordnung**

Das SAP-System prüft automatisiert, ob im Rechnungssatz eine Bestellnummer hinterlegt ist.
Liegt ein Bestellbezug vor, wird der Vorgang dem jeweiligen Einkaufsvorgang (im Modul MM) zugeordnet.
Fehlt ein Bestellbezug, prüft die Buchhaltung, ob ein Rahmenvertrag existiert, auf den sich die Rechnung beziehen kann.

Wenn weder ein Bestellbezug noch ein Rahmenvertrag gefunden wird, wird die Rechnung der zuständigen Fachabteilung zur Klärung zugewiesen. Die Fachabteilung prüft, ob es sich ggf. um eine einmalige Leistung, einen Werkvertrag oder eine Sondervereinbarung handelt.

**3.4 Sachliche Prüfung in der Fachabteilung**

Die sachliche Prüfung erfolgt in der Fachabteilung, die die Leistung oder Lieferung beauftragt hat.
Dort wird überprüft:

- ob die Leistung tatsächlich erbracht oder die Ware vollständig geliefert wurde,
- ob Menge, Preis und Leistungszeitraum mit der Bestellung bzw. dem Vertrag übereinstimmen,
- ob der Rechnungsbetrag korrekt ist und ggf. Rabatte oder Skonti berücksichtigt wurden,
- ob die Kontierung (Kostenstelle, Innenauftrag, Projekt, Steuerschlüssel) sachgerecht ist.

Falls Unstimmigkeiten vorliegen, nimmt die Fachabteilung Kontakt mit dem Lieferanten auf oder stimmt sich mit der Buchhaltung ab.
Erst wenn die inhaltliche Prüfung abgeschlossen ist, bestätigt die Fachabteilung die sachliche Richtigkeit der Rechnung im System.

Diese Bestätigung erfolgt durch elektronische Kennzeichnung im SAP-System (z. B. durch Häkchen „sachlich geprüft“ oder Unterschrift im Workflow).

**3.5 Freigabe der Rechnung**

Nach der sachlichen Prüfung wird die Rechnung im elektronischen Freigabe-Workflow an die zuständige freigabeberechtigte Person weitergeleitet.
Die Freigabeberechtigten sind gemäß der internen Zeichnungsrichtlinie der Heiß &amp; Laut Maschinenbau GmbH im System hinterlegt.

Im Rahmen der Freigabe wird überprüft:

- ob die Rechnung sachlich korrekt ist,
- ob die Leistung im Budgetrahmen liegt,
- ob eine Berechtigung zur Freigabe besteht,
- ob alle vorherigen Prüfschritte abgeschlossen wurden.

Die Freigabe erfolgt durch elektronische Bestätigung (z. B. Schaltfläche „freigeben“ im SAP-System).
Wenn Unklarheiten bestehen oder die Freigabe abgelehnt wird, wird die Rechnung an die Buchhaltung zurückgesendet. Diese veranlasst eine Rückfrage bei der Fachabteilung oder beim Lieferanten.

**3.6 Buchung und Zahlung**

Sobald die Freigabe erteilt wurde, bucht das SAP-System die Rechnung automatisch.
Sie wird in den nächsten Zahlungsvorschlag aufgenommen und nach den im System hinterlegten Zahlungsbedingungen (z. B. Skonto, Fälligkeit) ausgeführt.
Der Zahlungslauf wird von der Finanzbuchhaltung überwacht.

Bei größeren Beträgen oder Sonderzahlungen erfolgt eine zusätzliche manuelle Kontrolle durch eine zweite Person (Vier-Augen-Prinzip).
Nach erfolgreicher Ausführung der Zahlung wird der Belegstatus im System auf „bezahlt“ gesetzt.

**3.7 Archivierung und Nachvollziehbarkeit**

Nach Abschluss des gesamten Bearbeitungsprozesses wird der vollständige Rechnungsbeleg einschließlich aller zugehörigen Prüf- und Freigabeinformationen revisionssicher im DMS abgelegt.
Die Archivierung erfolgt nach den GoBD und der internen Aufbewahrungsrichtlinie, d. h. in der Regel für mindestens zehn Jahre.

Über die Dokumenten-ID oder SAP-Belegnummer kann der Vorgang jederzeit nachvollzogen werden.
Die Historie der Bearbeitungsschritte (Wer hat wann geprüft, freigegeben, bezahlt?) ist im System protokolliert und unveränderbar gespeichert.

**4. Sonderfälle**

- **Rahmenverträge ohne SAP-Abruf:** Rechnungen müssen manuell geprüft werden, ob sie sich auf einen gültigen Vertrag beziehen.
- **Rechnungen ohne Bestellbezug:** Nur nach Freigabe durch die zuständige Führungskraft und Rücksprache mit der Buchhaltung zulässig.
- **Papierrechnungen:** Nur in Ausnahmefällen, z. B. wenn der Lieferant keine elektronische Übermittlung ermöglicht. Diese werden sofort nach dem Scanvorgang elektronisch weiterverarbeitet.
- **Korrekturrechnungen oder Gutschriften:** Werden wie eigenständige Rechnungen behandelt und erhalten eine separate Dokumenten-ID.
- **Stornierungen:** Dürfen ausschließlich von der Buchhaltung durchgeführt werden, mit Dokumentation des Stornogrunds.

**5. Risiken und Kontrollen**

Im Rahmen des Prozesses bestehen insbesondere folgende Risiken:

- fehlerhafte oder doppelte Rechnungen,
- Zahlungen ohne ordnungsgemäße Freigabe,
- falsche Kontierung oder fehlerhafte Steuerschlüssel,
- Verstöße gegen Aufbewahrungsfristen.

Zur Vermeidung dieser Risiken bestehen folgende Kontrollen:

- systemische Duplikatsprüfung in SAP,
- automatisierte Pflichtfeldprüfung für Bestellnummern,
- elektronischer Freigabeprozess mit Berechtigungsprüfung,
- revisionssichere Archivierung aller Belege,
- regelmäßige Stichprobenprüfung durch die Steuerabteilung.

**6. Prozessende**

Der Prozess gilt als abgeschlossen, wenn:

1. die Rechnung formell und sachlich geprüft,
2. die Freigabe erteilt,
3. die Zahlung ausgeführt und
4. der vollständige Beleg elektronisch archiviert wurde.

Damit ist der gesamte Bearbeitungsweg von der Erfassung bis zur Archivierung lückenlos dokumentiert und jederzeit nachvollziehbar.