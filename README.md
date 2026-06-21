# 🏢 Company Sim

A real-time multiplayer corporate simulation game built with **Flask**, **Socket.IO**, and **SQLite**. Players join as employees of competing tech companies, solve coding challenges, manage KPIs, and race to hit victory targets — all in the browser.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Socket.IO-Realtime-010101?logo=socketdotio&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red)

---

## ✨ Features

- **Real-Time Multiplayer** — WebSocket-powered live dashboard updates across all players
- **Multi-Company Competition** — Multiple companies compete simultaneously with shared market events
- **24 Career Roles** — 7 career tracks (Frontend, Backend, QA, DevOps, Data Science, Product, Design) with Junior → Senior → CTO → CEO progression
- **Task Engine** — Category-based MCQ challenges (Logic, Bug Fixes, Refactoring, Marketing, Security, etc.) with 4,000+ questions
- **Live KPI Dashboard** — Revenue, Morale, Product Quality, Server Uptime, Tech Debt — all with real-time Chart.js graphs
- **Victory Conditions** — First company to satisfy all 5 metric thresholds simultaneously wins
- **Gadget Shop** — Spend earned salary on productivity gadgets (Mechanical Keyboard, VR Headset, Dual Monitors, etc.)
- **3D Retro TV News Widget** — Draggable, interactive CSS 3D television broadcasting live market bulletins
- **Team & Global Chat** — Real-time chat with team and cross-company messaging with role-based avatars
- **Admin Control Room** — Create/manage sessions, pause/resume games, monitor all companies from a dedicated admin dashboard
- **Support Tickets** — Players can open real-time support threads with the admin
- **3 Premium Themes** — Light Paper, Midnight Dev, and Cyberpunk Neon with full dynamic switching
- **11 Languages** — English, Spanish, French, German, Chinese, Japanese, Portuguese, Russian, Arabic, Hindi, Gujarati
- **Password Authentication** — Secure player registration with hashed passwords and reconnection support

---

## 📸 Screenshots

| Landing Page | Player Dashboard | Admin Panel |
|:---:|:---:|:---:|
| Split-screen access terminal with live telemetry | Real-time KPI graphs, tasks, chat, and 3D TV widget | Global overview, company nodes, and leaderboard |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+, Flask, Flask-SocketIO |
| **Database** | SQLite (via Flask-SQLAlchemy) |
| **Real-time** | Socket.IO (Eventlet async) |
| **Frontend** | Vanilla HTML/CSS/JS, Chart.js, Lucide Icons |
| **Deployment** | Docker, Gunicorn, Render / Railway / VPS |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+ installed
- Git installed

### Local Development

```bash
# 1. Clone the repository
git clone https://github.com/vedantjoliya/company-sim.git
cd company-sim

# 2. Create a virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
```

The server starts at **http://localhost:5000**

### How to Play

1. Open `http://localhost:5000` in your browser
2. Click **Admin Controls** → **Create Session** to spin up a new company node
3. Share the **6-digit join code** with players
4. Players enter their name, the code, pick a role, and set a password
5. The admin starts the simulation — the race begins!

---

## 🐳 Docker Deployment

### Docker Compose (Recommended)

```bash
# Build and start
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Standalone Docker

```bash
# Build the image
docker build -t company-sim .

# Run the container
docker run -d \
  --name company-sim \
  -p 5000:5000 \
  -v company-data:/app/instance \
  -e SECRET_KEY=your-secret-key-here \
  company-sim
```

Access at **http://localhost:5000**

---

## ☁️ Cloud Deployment

### Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Configure:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 -b 0.0.0.0:$PORT --timeout 120 app:app`
5. Add environment variable: `SECRET_KEY` = `<your-random-secret>`
6. Deploy

### Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**
3. Railway auto-detects Python — add a `Procfile`:

```
web: gunicorn --worker-class eventlet -w 1 -b 0.0.0.0:$PORT --timeout 120 app:app
```

4. Add environment variable: `SECRET_KEY` = `<your-random-secret>`
5. Deploy

### VPS (Ubuntu / Debian)

```bash
# Install dependencies
sudo apt update && sudo apt install python3 python3-venv python3-pip git -y

# Clone and setup
git clone https://github.com/vedantjoliya/company-sim.git
cd company-sim
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run with Gunicorn (production)
gunicorn --worker-class eventlet -w 1 -b 0.0.0.0:5000 --timeout 120 app:app
```

> **Tip**: Use `systemd` or `supervisor` to keep the process alive, and `nginx` as a reverse proxy for SSL termination.

---

## 📁 Project Structure

```
company-sim/
├── app.py                  # Main Flask application (routes, sockets, game logic)
├── models.py               # SQLAlchemy database models
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Multi-container orchestration
├── Procfile                # PaaS deployment command
├── .gitignore              # Git exclusions
├── .dockerignore           # Docker build exclusions
├── LICENSE.md              # Proprietary license
│
├── data/
│   ├── roles.py            # 24 career roles definition
│   ├── questions.json      # 4,000+ categorized MCQ questions
│   └── generate_questions.py  # Question bank generator script
│
├── static/
│   ├── css/
│   │   ├── style.css       # Main stylesheet (3 themes, 1800+ lines)
│   │   └── charts.css      # Chart.js overrides
│   └── img/                # 20 custom clipart assets (roles, gadgets, news TV)
│
├── templates/
│   ├── index.html          # Landing page (split-screen access terminal)
│   ├── game.html           # Player dashboard (KPIs, tasks, chat, 3D TV)
│   ├── admin.html          # Admin control room
│   └── fired.html          # Termination notice page
│
└── instance/               # SQLite database (auto-created, gitignored)
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `super-secret-key-for-company-sim` | Flask session secret. **Change in production!** |
| `PORT` | `5000` | Server port (used by PaaS platforms) |

---

## 🎮 Game Mechanics

### Victory Conditions (all must be met simultaneously)
| Metric | Target |
|---|---|
| Company Revenue | ≥ Goal (default $1,000,000) |
| Employee Morale | ≥ 80% |
| Product Quality | ≥ 80 |
| Server Uptime | ≥ 99% |
| Tech Debt | ≤ 15 |

### Career Progression
```
Junior → Mid → Senior → CTO/CPO → CEO
  (score thresholds trigger automatic promotions with salary raises)
```

### Task Categories
Logic, Bug Fixes, Refactoring, Prompt Engineering, Marketing, Team Bonding, Hotfix Deployment, System Architecture, Security Audit, Keyword Matching, and more.

---

## 🔒 Security Notes

- Player passwords are hashed with `werkzeug.security` (PBKDF2)
- Change the `SECRET_KEY` environment variable before deploying to production
- The SQLite database file is stored in `instance/` and is excluded from version control
- CORS is configured with `cors_allowed_origins="*"` — restrict this in production

---

## 📄 License

Copyright © 2026 **Vedant Joliya**. All rights reserved.

This project is provided publicly for portfolio, demonstration, and educational viewing purposes only. See [LICENSE.md](LICENSE.md) for details.

---

## 👨‍💻 Author

**Vedant Joliya**
- Portfolio: [vedantjoliya.free.nf](https://vedantjoliya.free.nf/)
- Email: [contactsvedant@gmail.com](mailto:contactsvedant@gmail.com)
- GitHub: [@vedantjoliya](https://github.com/vedantjoliya)
