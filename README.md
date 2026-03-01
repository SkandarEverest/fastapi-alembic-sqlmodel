# Expense Tracker API

A simple REST API built with FastAPI, SQLModel, and Alembic.

This project was developed for Assignment 1 (API + Database + Migration) and deployed to a VPS for Assignment 2.

---

## Tech Stack

Backend:
- FastAPI
- SQLModel
- Alembic
- SQLite
- Uvicorn

Deployment:
- DigitalOcean VPS (Singapore)
- Nginx (reverse proxy)
- Cloudflare (DNS)
- Let’s Encrypt (SSL)

---

## Features

- Create expense categories
- Create expenses
- Retrieve expense list
- Database migration using Alembic
- Production deployment with HTTPS

---

## Local Development

### Install dependencies

```bash
uv sync
```

### Run migration

```bash
uv run alembic upgrade head
```

### Start development server

```bash
uv run uvicorn app.main:app --reload
```

---

## Database Migration

Create new migration:

```bash
uv run alembic revision --autogenerate -m "message"
```

Apply migration:

```bash
uv run alembic upgrade head
```

---

## Production Deployment Summary

1. Create DigitalOcean Droplet (Ubuntu 22.04, Singapore region)
2. Setup SSH key authentication
3. Enable firewall (OpenSSH, HTTP, HTTPS)
4. Clone repository on VPS
5. Run:

```bash
uv sync
uv run alembic upgrade head
```

6. Create systemd service to run Uvicorn
7. Configure Nginx reverse proxy
8. Configure Cloudflare DNS
9. Install SSL using Let’s Encrypt (Certbot)

---

## Live API

Base URL:

```
https://expense-tracker-api.skandareverest.tech
```

API Documentation:

```
https://expense-tracker-api.skandareverest.tech/scalar
```

---

## Notes

- SQLite database file is not committed to the repository.
- Alembic manages database schema.
- Application runs via systemd on VPS.
- HTTPS secured with Let’s Encrypt.