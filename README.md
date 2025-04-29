# JOIN Backend (Django REST Framework)

Ein REST-API-Backend für das **JOIN** Projektmanagement-Tool, implementiert mit Django und Django REST Framework (DRF). Dieses Backend stellt Endpunkte für Benutzerregistrierung, Authentifizierung, Aufgabenverwaltung, Kontakte und Status-Tracking bereit.

---

## 📚 Inhaltsverzeichnis

1. [Funktionen](#funktionen)
2. [Technologien](#technologien)
3. [Voraussetzungen](#voraussetzungen)
4. [Installation](#installation)
5. [Umgebungsvariablen](#umgebungsvariablen)
6. [Datenbank-Migration](#datenbank-migration)
7. [Starten des Servers](#starten-des-servers)
8. [API-Routen](#api-routen)
9. [Serializers & Modelle](#serializers--modelle)
10. [Tests](#tests)
11. [Deployment](#deployment)
12. [Contributing](#contributing)
13. [Lizenz](#lizenz)

---

## 🚀 Funktionen

- **Benutzerverwaltung**: Registrierung, Login per Token-Authentifizierung
- **Aufgaben**: CRUD-Operationen für Tasks und SubTasks, Zuordnung zu Benutzern
- **Kontakte**: CRUD für Kontakte, Verknüpfung mit dem aktuellen Benutzer
- **Aktueller Benutzer**: Upsert-Endpoint für Profildaten des eingeloggten Users
- **Status**: Übersichtliche Status-Objekte mit Create-or-Update-Logik
- **Custom Actions**: z.B. `/tasks/{id}/subtask/` zum Abrufen von SubTasks
- **Permissions**: Public und geschützte Endpunkte mit `IsAuthenticated` und `AllowAny`

---

## 🛠 Technologien

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (Standard), konfigurierbar für andere Datenbanken
- Token Authentication (`rest_framework.authtoken`)

---

## 🔧 Voraussetzungen

- Python 3.10 oder höher
- `pip` installiert
- Optional: Virtualenv

---

## ⚙️ Installation

1. Repo klonen:
   ```bash
   git clone https://github.com/DEIN_USERNAME/join-backend.git
   cd join-backend
   ```
2. Virtuelle Umgebung erstellen & aktivieren:
   ```bash
   python -m venv env
   source env/bin/activate       # Linux/macOS
   env\Scripts\Activate.ps1    # Windows PowerShell
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Umgebungsvariablen

Lege eine `.env`-Datei im Projekt-Root an und definiere:

```ini
# .env
DEBUG=True
SECRET_KEY=DEIN_DJANGO_SECRET_KEY
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3    # oder PostgreSQL-URL
```

Weitere Einstellungen siehe `join_backend/settings.py`.

---

## 🗄 Datenbank-Migration

```bash
python manage.py migrate
```

(Optional) Superuser anlegen:

```bash
python manage.py createsuperuser
```

---

## ▶️ Starten des Servers

```bash
python manage.py runserver
```

Der API-Server läuft dann standardmäßig auf `http://127.0.0.1:8000/api/`.

---

## 📡 API-Routen

| Endpunkt                   | Methode        | Beschreibung                        |
| -------------------------- | -------------- | ----------------------------------- |
| `/api/registration/`       | POST           | Nutzer registrieren                 |
| `/api/login/`              | POST           | Token-Login                         |
| `/api/tasks/`              | GET,POST       | Auflistung/Anlegen von Tasks        |
| `/api/tasks/{id}/`         | GET,PUT,DELETE | Detail-/Update-/Lösch-Operationen   |
| `/api/tasks/{id}/subtask/` | GET            | SubTasks einer Task abrufen         |
| `/api/subtasks/`           | GET,POST       | CRUD für SubTasks                   |
| `/api/contacts/`           | GET,POST       | CRUD für Kontakte (authentifiziert) |
| `/api/contacts/{id}/`      | GET,PUT,DELETE | Detail-/Update-/Lösch-Operationen   |
| `/api/current-user/`       | GET,PUT        | Upsert-Profildaten des Users        |
| `/api/status/`             | GET,POST       | CRUD für Status-Modelle             |
| `/api/status/{id}/`        | PUT            | Create-or-Update-Endpoint           |

---

## 📦 Serializers & Modelle

- **Serializers** befinden sich in `api/serializers.py`:

  - `RegistrationSerializer`
  - `EmailAuthTokenSerializer`
  - `TaskSerializer`, `SubTaskSerializer`
  - `ContactSerializer`, `StatusSerializer`, `CurrentUserSerializer`

- **Modelle** in `join/models.py`:

  - `Task`, `SubTask`, `Contact`, `Status`, `CurrentUser`

---

## 🧪 Tests

(*falls vorhanden – hier beschreiben*)  
Beispiel:

```bash
python manage.py test
```

---

## ☁️ Deployment

Für Produktionsempfehlungen:

1. `DEBUG=False` setzen
2. Produktions-Datenbank (PostgreSQL, MySQL) konfigurieren
3. WSGI-Server (Gunicorn, uWSGI)
4. Reverse Proxy (Nginx)
5. SSL-Zertifikat

---

## 🤝 Contributing

1. Forke das Repo
2. Branch erstellen (`git checkout -b feature/xyz`)
3. Änderungen committen (`git commit -m "feat: ..."`)

---

## 📄 Lizenz

Dieses Projekt steht unter der MIT License.  
Details siehe [LICENSE](./LICENSE).

---

## 📫 Kontakt

Bei Fragen: <deine.email@example.com> oder per GitHub-Issue.
