# 🇮🇳 Scheme Dekho — Government Scheme Portal

A beautiful, professional local website for discovering and checking eligibility for 138+ Indian government schemes.

## 🚀 Quick Start

### 1. Install Python dependencies
```bash
pip install flask
```

### 2. Set up the database (run once)
```bash
python seed_db.py
```

### 3. Start the website
```bash
python app.py
```

### 4. Open in your browser
```
http://localhost:5000
```

---

## 📂 Project Structure
```
scheme_dekho/
├── app.py              ← Flask application (main server)
├── seed_db.py          ← Database seeder (run once)
├── requirements.txt
├── database/
│   └── schemes.db      ← SQLite database (auto-created)
├── templates/
│   ├── base.html       ← Shared layout & navbar
│   ├── index.html      ← Home page
│   ├── dashboard.html  ← Dashboard
│   ├── schemes.html    ← Browse all schemes
│   ├── scheme_detail.html ← Single scheme page
│   ├── eligibility.html   ← Eligibility checker
│   └── verifier.html      ← Scheme verifier
└── static/
    ├── css/style.css   ← All styles
    └── js/main.js      ← Animations & interactions
```

## ✨ Features
- 🏠 **Stunning Home Page** — Animated hero, scheme ticker, category grid
- 📊 **Dashboard** — KPIs, quick access, tools overview
- 📋 **138+ Schemes** — Searchable, filterable by category
- 🎯 **Eligibility Checker** — Enter age, income, caste, gender, BPL → instant matches
- 🛡️ **Scheme Verifier** — Check if a scheme is real or fake
- 🔗 **Official Links** — Direct link to gov.in for every scheme
- 🌙 **Dark Theme** — India-inspired saffron + navy + gold

## 🛠️ Tech Stack
- **Backend**: Python + Flask
- **Database**: SQLite (SQL)
- **Frontend**: HTML5 + CSS3 + Vanilla JS
- **Fonts**: Syne (display) + Plus Jakarta Sans
- **Icons**: Font Awesome 6
