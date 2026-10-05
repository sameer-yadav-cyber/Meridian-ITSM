# MeridianDesk — Postgres on Render + local API

This folder is the custom ITSM microservice from the FRS (replaces ServiceNow). The AEX agent calls these REST endpoints. The approved troubleshooting text lives in `../kb_docs/Meridian_KB.md` (export that file to PDF and index it in AEX).

## 1. Create Postgres on Render

1. Sign in at [https://dashboard.render.com](https://dashboard.render.com).
2. **New + → PostgreSQL**.
3. Settings:
   - Name: `meridiandesk`
   - Database: `meridiandesk`
   - User: leave generated, or set `meridian`
   - Region: closest to you
   - Plan: Free is enough for the assessment
4. Create the database and wait until status is **Available**.
5. Open the database page and copy **External Database URL**.  
   It looks like:  
   `postgresql://USER:PASSWORD@dpg-xxxx.oregon-postgres.render.com/meridiandesk`
6. Also copy **Internal Database URL** if you later host the API on Render in the same region (faster, no SSL from inside Render).

Render **pauses** free databases after inactivity. Resume it from the dashboard if connections fail.

### Connect from your laptop (localhost API → Render Postgres)

On the Render database page:

- **External Database URL** is the one your PC uses.
- Add `?sslmode=require` if it is not already in the URL.

In `backend/.env`:

```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/meridiandesk?sslmode=require
SEED_ON_START=true
```

Allow your IP if Render shows an access-control list. For the free/starter Postgres used in this assessment, external connections with the password URL are enough.

Do not commit `.env`. `.env.example` is the template.

### Optional: Postgres also on localhost

If you want a fully local database (Docker):

```
docker run --name meridian-pg -e POSTGRES_USER=meridian -e POSTGRES_PASSWORD=meridian -e POSTGRES_DB=meridiandesk -p 5432:5432 -d postgres:16
```

Then:

```
DATABASE_URL=postgresql://meridian:meridian@localhost:5432/meridiandesk
```

You can keep two `.env` files and switch: Render for shared demo data, Docker for offline work.

## 2. Run the API on localhost (talks to Render or local Postgres)

From this `backend` folder:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and paste the Render **External Database URL**.

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs` for Swagger. Seed users and catalogue load on first start.

Health check: `GET http://127.0.0.1:8000/health`

AEX on another machine cannot call `127.0.0.1`. Use ngrok, Cloudflare Tunnel, or deploy the API on Render (section 3) and put that public HTTPS base URL in the AEX tool configs.

## 3. Host the API on Render (optional)

1. Push this project to Git (GitHub/GitLab).
2. Render → **New + → Web Service**.
3. Root directory: `backend`
4. Runtime: Python
5. Build: `pip install -r requirements.txt`
6. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Environment:
   - `DATABASE_URL` = Render Postgres **Internal** URL if the web service is in the same region, otherwise External URL with `sslmode=require`
   - `SEED_ON_START=true`
8. After deploy, the public base is `https://YOUR-SERVICE.onrender.com`

In AEX, set tool URLs to that base, for example `https://YOUR-SERVICE.onrender.com/incidents`.

## 4. Agent vs admin endpoints

The chat agent may call:

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/users/{user_id}` | Profile (name, email, phone, role) |
| GET | `/motd` | Up to two active announcements |
| GET | `/catalog/search?q=` | Catalogue search |
| POST | `/incidents` | Create incident |
| POST | `/requests` | Create RITM |
| GET | `/tickets?user_id=` | Latest 10 of that user |
| GET | `/tickets/{number}?user_id=` | One ticket, ownership checked |
| POST | `/tickets/{number}/comments?user_id=` | Add comment |
| POST | `/tickets/{number}/attachments?user_id=` | Attach file (base64) |

Admin / data management (AEX agent must **not** expose these to the end user):

| Method | Path | Purpose |
| --- | --- | --- |
| GET/POST/PUT/DELETE | `/users` | User CRUD |
| GET/POST/PUT/DELETE | `/catalog` | Catalogue CRUD |
| GET/POST/PUT/DELETE | `/motd` | MOTD CRUD |
| GET | `/admin/tickets` | All tickets |
| PATCH | `/admin/tickets/{number}` | Fulfilment update (status, assignee, priority) |
| PUT | `/admin/tickets/{number}` | Same fields |
| DELETE | `/admin/tickets/{number}` | Delete ticket |
| GET | `/admin/events` | Event log for mailer testing |

`GET /kb/search` is a stub. Full article text is retrieved from the **AEX Knowledge Base** after you upload the PDF of `Meridian_KB.md`.

## 5. Seed users (chat start IDs)

`jsmith` `apatel` `mchen` `rgarcia` `nwilliams` `dkim`

Email on each profile is the DNR Mailer recipient.
