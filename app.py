from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os
import requests
from dotenv import load_dotenv

# Umgebungsvariablen laden
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecret")

# Kontextprozessor für das aktuelle Jahr
@app.context_processor
def inject_year():
    return {'jahr': datetime.now().year}

# Bilderverzeichnis definieren
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BILDER_ORDNER = os.path.join(BASE_DIR, "static", "fotos")

def lade_bilder():
    try:
        return os.listdir(BILDER_ORDNER)
    except FileNotFoundError:
        return []

# Startseite
@app.route("/")
def index():
    return render_template("index.html")

# Kontaktseite mit Formular
@app.route("/kontakt", methods=["GET", "POST"])
def kontakt():
    bilder = lade_bilder()

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        nachricht = request.form.get("nachricht")

        if not name or not email or not nachricht:
            flash("Bitte alle Felder ausfüllen!", "error")
        else:
            try:
                headers = {
                    "accept": "application/json",
                    "api-key": os.getenv("BREVO_API_KEY"),
                    "content-type": "application/json"
                }

                common_content = f"""
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>E-Mail:</strong> {email}</p>
                    <p><strong>Nachricht:</strong><br>{nachricht}</p>
                """

                # An Admin senden
                data_admin = {
                    "sender": {"name": "Webformular", "email": os.getenv("BREVO_SENDER")},
                    "to": [{"email": os.getenv("BREVO_RECIPIENT"), "name": "Empfänger"}],
                    "subject": f"Neue Kontaktanfrage von {name}",
                    "htmlContent": common_content
                }

                response_admin = requests.post("https://api.brevo.com/v3/smtp/email", headers=headers, json=data_admin)

                # Kopie an Absender senden
                data_user = {
                    "sender": {"name": "Jeannine Schöb", "email": os.getenv("BREVO_SENDER")},
                    "to": [{"email": email, "name": name}],
                    "subject": "Kopie deiner Kontaktanfrage",
                    "htmlContent": f"""
                        <p>Hallo {name},</p>
                        <p>vielen Dank für deine Nachricht. Hier ist eine Kopie deiner Anfrage:</p>
                        {common_content}
                        <p>Wir melden uns so bald wie möglich bei dir.</p>
                        <p>Liebe Grüße,<br>Jeannine Schöb</p>
                    """
                }

                response_user = requests.post("https://api.brevo.com/v3/smtp/email", headers=headers, json=data_user)

                if response_admin.status_code == 201 and response_user.status_code == 201:
                    flash("Nachricht erfolgreich gesendet!", "success")
                else:
                    flash("Fehler beim Senden der E-Mail(s).", "error")

                return redirect(url_for("kontakt"))

            except Exception as e:
                flash(f"Fehler beim Senden der Nachricht: {e}", "error")

    return render_template("kontakt.html", bilder=bilder)

# Statische Inhaltsseiten
@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/veranstaltungen")
def veranstaltungen():
    return render_template("veranstaltungen.html")

@app.route("/anreise")
def anreise():
    return render_template("anreise.html")

@app.route("/verfuegbarkeit")
def verfuegbarkeit():
    return render_template("verfuegbarkeit.html")

@app.route("/ab_hof_produkte")
def ab_hof_produkte():
    return render_template("ab_hof_produkte.html")

@app.route("/kueche")
def kueche():
    return render_template("kueche.html")

@app.route("/gasthaeuser")
def gasthaeuser():
    return render_template("gasthaeuser.html")

@app.route("/gaestebuch")
def gaestebuch():
    return render_template("gaestebuch.html")

@app.route("/bildergalerie")
def bildergalerie():
    return render_template("bildergalerie.html")

@app.route("/wissenswertes")
def wissenswertes():
    return render_template("wissenswertes.html")

if __name__ == "__main__":
    app.run(debug=True)

