# Market Tracker Architecture

## Overview
Market Tracker is a Python application that retrieves real-time cryptocurrency and forex market data using public APIs and displays it in both terminal and web dashboard interfaces.

---

## Components

### 1. API Layer
Responsible for fetching market data.

Crypto data source:
- CoinGecko API

Forex data source:
- ExchangeRate API

Files:
- api.py

---

### 2. Backend Server

Flask web application responsible for:

- Handling HTTP requests
- Fetching market data
- Passing data to templates
- Serving charts and dashboard

File:
- app.py

---

### 3. Terminal Interface

Allows users to query markets directly from the terminal.

Displays:
- crypto prices
- forex rates

File:
- terminal.py

---

### 4. Chart Module

Handles price history and chart generation.

File:
- charts.py

---

### 5. Frontend

Web dashboard built with:

- HTML
- CSS
- Jinja2 templates

Files:

templates/dashboard.html  
static/style.css

---

## Data Flow

User Request  
↓  
Flask App  
↓  
API Requests (CoinGecko / ExchangeRate)  
↓  
Data Processing 
STRUCTURE

market_tracker
│
├── app.py
├── api.py
├── charts.py
├── terminal.py
│
├── templates/
│ └── dashboard.html
│
├── static/
│ └── style.css
│
├── images/
│
├── README.md
├── ARCHITECTURE.md
└── requirements.txt
↓  
Render Dashboard or Terminal Output

---


