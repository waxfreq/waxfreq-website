# waxfreq* Website – Anleitung zum Hochladen und Pflegen

Diese Anleitung ist für Simon (oder wer auch immer die Seite online bringt).
Kein Terminal nötig, alles läuft über die GitHub-Webseite und die App GitHub Desktop.
Dauer: etwa 20 Minuten.

---

## 1. Was in diesem Ordner liegt

| Datei / Ordner | Zweck |
|---|---|
| `index.html` | Die ganze Seite: Layout, Texte, Animationen |
| `releases.json` | Die Releases für die Latest-Sektion (neuestes oben) |
| `assets/logo-teal.webp`, `assets/logo-teal.png` | Logo in Teal (Original silber: `assets/logo.webp`) |
| `assets/press/` | Pressefoto: `artist.webp` / `artist.jpg` für die Seite, `waxfreq-press.jpg` in voller Grösse zum Download |
| `assets/cursor/` | Die Mauszeiger (Camo und Leopard) |
| `scripts/update-releases.py` | Holt die Releases von elasticStage und schreibt `releases.json` |
| `.github/workflows/update-releases.yml` | Lässt dieses Script auf GitHub jeden Tag automatisch laufen |
| `ANLEITUNG.md` | Diese Datei |
| `_old/`, `.claude/`, `*.zip` | Backups und Arbeitsdateien, müssen **nicht** online (stehen in `.gitignore`) |

Die Seite braucht keinen Server und kein Framework. `index.html` doppelklicken zeigt sie lokal.

---

## 2. Einmalig: GitHub-Account

1. Auf <https://github.com> ein kostenloses Konto anlegen (am besten ein gemeinsames für waxfreq*, zum Beispiel Benutzername `waxfreq`).
   Der Benutzername wird Teil der Adresse: `https://BENUTZERNAME.github.io/waxfreq-website/`
2. E-Mail bestätigen.

---

## 3. Repository anlegen

1. Oben rechts auf **+** → **New repository**.
2. Repository name: `waxfreq-website`
3. **Public** auswählen (GitHub Pages ist nur bei öffentlichen Repos kostenlos).
4. Nichts weiter ankreuzen (kein README, kein .gitignore). **Create repository**.

---

## 4. Dateien hochladen mit GitHub Desktop

1. <https://desktop.github.com> herunterladen, installieren, mit dem GitHub-Konto anmelden.
2. In GitHub Desktop: **File → Clone repository**, das Repo `waxfreq-website` wählen, einen Ordner aussuchen, **Clone**.
   Es entsteht ein leerer Ordner `waxfreq-website` auf dem Rechner.
3. Den **gesamten Inhalt** dieses Projektordners (alles, inklusive dem versteckten Ordner `.github`) in diesen neuen Ordner kopieren.
   Tipp im Finder: `Cmd + Shift + .` zeigt versteckte Ordner an. Der Ordner `_old` darf weggelassen werden.
4. Zurück in GitHub Desktop: links erscheinen alle Dateien. Unten links bei "Summary" zum Beispiel `Website` eintragen, dann **Commit to main**.
5. Oben auf **Push origin**. Fertig, die Dateien sind auf GitHub.

Alternative ohne GitHub Desktop: Im Repo auf GitHub **Add file → Upload files**, alle Dateien hineinziehen, **Commit changes**.
Der Ordner `.github` lässt sich so aber nicht hochladen, dafür siehe Schritt 6b.

---

## 5. GitHub Pages einschalten

1. Im Repo auf **Settings** → links **Pages**.
2. Bei "Build and deployment" → Source: **Deploy from a branch**.
3. Branch: **main**, Ordner: **/ (root)**. **Save**.
4. Ein bis zwei Minuten warten, Seite neu laden. Oben steht dann die Adresse, zum Beispiel
   `https://waxfreq.github.io/waxfreq-website/`
   Das ist die fertige Website.

---

## 6. Automatisches Release-Update einschalten

Damit die Latest-Sektion sich selbst von elasticStage aktualisiert:

**6a. Erlaubnis für den Workflow**
1. **Settings** → **Actions** → **General**.
2. Unten bei "Workflow permissions": **Read and write permissions** wählen. **Save**.

**6b. Falls der Ordner `.github` nicht mit hochgeladen wurde**
1. Im Repo **Add file → Create new file**.
2. Als Dateiname eintippen: `.github/workflows/update-releases.yml` (GitHub legt die Ordner selbst an).
3. Den Inhalt der Datei `.github/workflows/update-releases.yml` aus diesem Projekt hineinkopieren. **Commit changes**.

**6c. Testen**
1. Oben im Repo auf **Actions** → links **Update releases from elasticStage** → rechts **Run workflow** → **Run workflow**.
2. Grüner Haken: läuft, ab jetzt jeden Morgen automatisch.
3. Roter Haken: elasticStage lässt den automatischen Abruf nicht durch. Dann gilt Abschnitt 8 (von Hand pflegen). Die Seite funktioniert trotzdem ganz normal.

---

## 7. Eigene Domain (optional)

Falls ihr zum Beispiel `waxfreq.ch` habt:
1. **Settings → Pages → Custom domain**: Domain eintragen, **Save**, **Enforce HTTPS** anhaken.
2. Beim Domain-Anbieter einen **CNAME**-Eintrag anlegen: `www` → `BENUTZERNAME.github.io`
   Für die nackte Domain vier **A**-Einträge auf `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
3. Bis zu einem Tag warten, bis es überall greift.

---

## 8. Die Seite pflegen

Alle Änderungen gehen gleich: Datei ändern, in GitHub Desktop **Commit** und **Push**. Nach ein bis zwei Minuten ist es online.
Ohne GitHub Desktop: Datei im Repo anklicken → Stift-Symbol → bearbeiten → **Commit changes**.

**Neues Release von Hand eintragen** (`releases.json`), falls der Workflow blockiert wird:
Oben in der Liste einen neuen Block einfügen, der neueste steht zuoberst:

```json
{
  "title": "Name der Platte",
  "format": "Single/EP",
  "media": ["Vinyl"],
  "year": "2027",
  "date": "2027-03-01",
  "genre": "Techno",
  "subgenre": "Detroit Techno",
  "url": "https://elasticstage.com/waxfreq/releases/...",
  "image": "https://... (Cover-Bild, Link von der elasticStage-Seite)"
},
```

Komma zwischen den Blöcken nicht vergessen. Ab zwei Releases erscheint automatisch "Also on wax" darunter.

**Texte ändern**: in `index.html` nach dem Text suchen (Bio im Abschnitt `id="about"`, Links im Abschnitt `id="links"`).

**Pressefoto tauschen**: neues Foto als `assets/press/artist.jpg` ablegen (ideal 1200 px breit, Hochformat 2:3) und `assets/press/artist.webp` löschen oder ebenfalls ersetzen. Die Vollgrösse für den Download ist `assets/press/waxfreq-press.jpg`.

**Links**: Soundcloud, elasticStage und Instagram stehen je dreimal in `index.html` (Kopfzeile, Linkliste, Footer). Suchen und ersetzen.

---

## 9. Zweite Person berechtigen

Statt Passwörter zu teilen: **Settings → Collaborators → Add people**, GitHub-Benutzername der Person eingeben. Sie bekommt eine Einladung per E-Mail und kann danach alles bearbeiten.

---

## 10. Wenn etwas nicht geht

- **Seite zeigt 404**: Pages noch nicht fertig (zwei Minuten warten) oder Branch/Ordner in Schritt 5 falsch.
- **Seite lädt, aber ohne Logo oder Foto**: Dateinamen prüfen, auf dem Server zählt Gross-/Kleinschreibung (`artist.jpg`, nicht `artist.JPG`).
- **Latest zeigt alte Platte**: `releases.json` prüfen, neuestes Datum muss oben stehen; Workflow in Actions anschauen.
- **Intro erscheint nicht mehr**: Es läuft einmal pro Browser-Sitzung. Tab schliessen und neu öffnen.
