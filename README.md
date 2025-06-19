# 🌐 Flask Kontaktformular mit Brevo (ehemals Sendinblue)

Dieses Projekt ist eine private Flask-Webanwendung für das Ferienhaus Schöb. Über das Kontaktformular können Nachrichten versendet werden – inklusive einer Kopie an die absendende Person.

## 🚀 Funktionen

- Kontaktformular mit Name, E-Mail und Nachricht
- Versand per Brevo (API)
- Automatische Kopie an Absender
- Flash-Nachrichten (Erfolg oder Fehler)
- Responsive Navigation & Layout
- Trennung von Code und sensiblen Daten via `.env`

## 🛠️ Installation

1. Repository klonen:
```bash
git clone https://github.com/dein-benutzername/dein-repo.git
cd dein-repo
```

2. Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate  # oder auf Windows: venv\Scripts\activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. `.env`-Datei erstellen mit folgendem Inhalt:
```env
FLASK_SECRET_KEY=dein_geheimer_schluessel
BREVO_API_KEY=dein_api_key
BREVO_SENDER=deine@absenderadresse.de
BREVO_RECIPIENT=deine@empfaengeradresse.de
```

## ▶️ Anwendung starten

```bash
python app.py
```

Dann im Browser öffnen: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📂 Projektstruktur

```
├── app.py
├── .env               # Nicht im Repo enthalten – selbst anlegen
├── templates/
├── static/
├── .gitignore
├── README.md
```

## 🔒 Lizenz / Nutzung

Dieses Projekt ist **nicht öffentlich lizenziert** und dient ausschließlich privaten Zwecken im Zusammenhang mit dem **Ferienhaus Schöb**.

- Eine Weitergabe, Vervielfältigung oder kommerzielle Nutzung ist **nicht gestattet**.
- Der Quellcode ist nur für den persönlichen Einsatz im Familien- und Freundeskreis gedacht.

📬 Kontakt bei Fragen: [j.schoeb@outlook.com](mailto:j.schoeb@outlook.com)