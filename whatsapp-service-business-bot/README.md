# WhatsApp Service Business Customer Support Bot

A complete, market-ready Flask project for a **Service Business Customer Support Bot** using a restaurant ordering demo. It is built for the project requirement: WhatsApp chatbot template + demo bot + database integration + analytics dashboard + deployment guide.

The bot can run in three ways:

1. **Browser demo chat** for instant project demonstration without WhatsApp credentials.
2. **Twilio WhatsApp Sandbox webhook** for fast WhatsApp testing.
3. **Meta WhatsApp Cloud API webhook** as an optional production-style adapter.

> Important: This project is a business-specific customer support bot, not a general-purpose AI assistant. It answers restaurant/service questions, manages orders/bookings/leads, and stores business records.

---

## Features

### WhatsApp/customer features

- Greeting and help flow
- Restaurant menu browsing
- Food order cart flow
- Delivery / pickup handling
- Payment method capture
- Order confirmation and order tracking
- Table reservation / appointment booking
- FAQ automation from business data
- Human staff callback / lead capture
- Feedback capture
- Browser demo simulator for viva/demo day

### Admin/business features

- Secure admin login with hashed password
- Analytics dashboard for revenue, orders, leads, conversations, messages, customers and bookings
- Conversation viewer with full message history
- Order status management
- Booking status management
- Lead pipeline status management
- Menu item management
- FAQ management
- CSV export for orders, leads and customers

### Engineering features

- Flask application factory structure
- SQLAlchemy data models
- SQLite default, PostgreSQL-ready through `DATABASE_URL`
- Twilio webhook XML/TwiML response
- Optional Twilio request signature validation
- Meta Cloud API webhook verification and message sending adapter
- Seed CSV data for menu and FAQs
- Tests for core bot flows and webhooks
- Dockerfile, docker-compose, Procfile, Makefile
- Deployment and architecture docs

---

## Project structure

```text
whatsapp-service-business-bot/
├── app/
│   ├── channels/              # Twilio and Meta channel adapters
│   ├── routes/                # Public, webhook, admin routes
│   ├── services/              # Bot engine, menu, FAQ, orders, analytics, seed
│   ├── static/                # CSS and JS
│   ├── templates/             # Public and admin HTML
│   ├── __init__.py            # Flask app factory
│   ├── extensions.py
│   └── models.py
├── data/                      # Menu, FAQ, sample data CSVs
├── docs/                      # Full guides and project documentation
├── scripts/                   # CSV import and backup utilities
├── tests/                     # pytest tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── wsgi.py
```

---

## Quick start: run locally

### 1. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create environment file

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and update:

```env
SECRET_KEY=make-this-long-and-random
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=ChangeMe@12345
BUSINESS_NAME=Spice Garden Restaurant
```

### 4. Initialize and seed database

The app auto-creates tables and seed records on first run. You can also run:

```bash
flask --app run.py init-db
flask --app run.py seed
```

### 5. Start server

```bash
flask --app run.py run --debug
```

Open:

- Website: `http://127.0.0.1:5000/`
- Browser demo: `http://127.0.0.1:5000/demo`
- Admin dashboard: `http://127.0.0.1:5000/admin`

Default admin credentials come from `.env`:

```text
admin@example.com / ChangeMe@12345
```

---

## Demo script for presentation

Use the browser demo first:

1. Send `hi`
2. Send `menu`
3. Send `order`
4. Send `PZ01 x2, BR01 x1`
5. Send `done`
6. Send `MG Road, Pune`
7. Send `cash`
8. Copy the generated order number
9. Send `status ORD-XXXXXX`
10. Send `book`
11. Send `Rohit Kumar`
12. Send `tomorrow 7pm`
13. Send `4`
14. Send `human`
15. Send `Rohit, corporate lunch for 30 people, rohit@example.com`
16. Open `/admin` to show records and analytics

---

## Twilio WhatsApp Sandbox setup

1. Create/login to Twilio.
2. Open WhatsApp Sandbox.
3. Join sandbox from your WhatsApp using the code shown by Twilio.
4. Expose local Flask using ngrok:

```bash
ngrok http 5000
```

5. In Twilio Sandbox settings, set **When a message comes in** to:

```text
https://YOUR-NGROK-DOMAIN.ngrok-free.app/webhook/twilio
```

6. Keep method as `POST`.
7. Send `hi` or `menu` from WhatsApp.

For production signature validation:

```env
PUBLIC_BASE_URL=https://your-real-domain.com
TWILIO_AUTH_TOKEN=your_token
VALIDATE_TWILIO_SIGNATURE=true
```

During local ngrok testing, set `PUBLIC_BASE_URL` to the exact ngrok URL.

---

## Meta WhatsApp Cloud API setup

This is optional. Twilio Sandbox is faster for student demos.

1. Create a Meta app with WhatsApp product.
2. Configure webhook callback URL:

```text
https://your-domain.com/webhook/meta
```

3. Use your `.env` value as verify token:

```env
META_VERIFY_TOKEN=change-this-verify-token
```

4. Subscribe to WhatsApp `messages` webhook field.
5. Configure production credentials:

```env
META_ACCESS_TOKEN=your_meta_token
META_PHONE_NUMBER_ID=your_phone_number_id
META_GRAPH_API_VERSION=v25.0
```

---

## Data management

The bot uses these included seed files:

- `data/menu.csv` — menu items, SKUs, category, price, tags
- `data/faqs.csv` — question, answer, category, keywords
- `data/service_catalog.csv` — service/appointment catalog
- `data/sample_orders.csv` — sample external analytics data format

To add a new client:

1. Replace menu and FAQ CSV data.
2. Run `flask --app run.py reset-db` for a clean local rebuild.
3. Or import CSV through `scripts/import_csv.py` from Flask shell.
4. Update `.env` business settings.
5. Test browser demo.
6. Connect Twilio/Meta webhook.

---

## Run tests

```bash
pytest -q
```

Expected: all tests pass.

---

## Docker run

```bash
cp .env.example .env
docker compose up --build
```

Open `http://localhost:5000`.

---

## Deployment summary

Use any platform that supports Python web apps:

- Render
- Railway
- Fly.io
- VPS with Nginx + Gunicorn
- Docker host

Production checklist:

- Set strong `SECRET_KEY`
- Set strong `ADMIN_PASSWORD`
- Use PostgreSQL for production
- Set `PUBLIC_BASE_URL` to HTTPS domain
- Enable Twilio signature validation if using Twilio
- Configure HTTPS webhook URL
- Back up database regularly
- Confirm WhatsApp opt-in/compliance policy for customers
- Do not use it as a general-purpose AI assistant; keep it business-support focused

See `docs/DEPLOYMENT.md` for full instructions.

---

## What to submit for college/project review

- GitHub repo with this code
- Screenshots of browser demo
- Screenshot of Twilio Sandbox webhook configuration
- Screenshot of WhatsApp message handling
- Screenshot of admin dashboard
- Architecture diagram from `docs/ARCHITECTURE.md`
- Test output screenshot from `pytest -q`
- Dataset references from `docs/DATASETS.md`
- Case study from `docs/CASE_STUDY_TEMPLATE.md`

---

## License

MIT License. You can use and customize this for student, portfolio, and client demo projects.
