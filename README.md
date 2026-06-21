# Company Simulation Game - Deployment Guide

This project is a multi-player corporate simulation game featuring real-time WebSockets communication, a live support dashboard, customizable visual themes, and 11 global languages.

## Deployment Options

We recommend deploying this application directly to **Render** or similar Python hosting services, as they natively support persistent databases and WebSockets (Socket.IO).

---

### Deploying to Render (Recommended)

Render is the easiest way to deploy this full Python application with real-time WebSockets and database persistence.

#### Option A: Quick Deploy (SQLite Mode)
1. Push this repository to your GitHub account.
2. Sign in to [Render](https://render.com/).
3. Click **New** -> **Web Service** and connect your GitHub repository.
4. Set the following configurations:
   - **Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 app:app`
5. Click **Deploy Web Service**. Render will automatically detect your WebSocket setup and deploy the app!

*Note: In SQLite mode, the local database will reset whenever the web service restarts or redeploys unless a persistent disk is attached to the Render service.*

#### Option B: Production Deploy (PostgreSQL Mode)
To keep player data persistent without resets:
1. Create a **PostgreSQL Database** on Render (it is free/low-cost).
2. Create a **Web Service** for this repository.
3. In the Web Service settings, go to the **Environment** tab.
4. Add a new Environment Variable:
   - **Key**: `DATABASE_URL`
   - **Value**: *(Connect your Render PostgreSQL Database: Render will automatically bind the connection string when you link them, or you can paste the Internal Database URL here)*
5. Use the same start command:
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 app:app`
6. Deploy the service. The application will automatically detect the database environment, skip SQLite migrations, and create the schema on PostgreSQL!

---

### Local Installation & Testing

If you want to run the server locally:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   python app.py
   ```
4. Access the portals:
   - **Player Terminal**: `http://127.0.0.1:5000/`
   - **Admin Control Room**: `http://127.0.0.1:5000/admin`
