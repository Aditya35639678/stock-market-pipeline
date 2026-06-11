# 📈 Stock Market Data Pipeline Dashboard

## Overview

This project is an end-to-end Data Engineering pipeline that extracts stock market data from Yahoo Finance, stores it in PostgreSQL using Docker, and visualizes key metrics in Grafana.

The dashboard allows users to dynamically select stocks and analyze their performance using various financial metrics.

---

## Project Architecture

```text
Yahoo Finance API
        │
        ▼
   Python ETL
        │
        ▼
 PostgreSQL
   (Docker)
        │
        ▼
    Grafana
 Dashboard
```

---

## Technologies Used

- Python
- yfinance
- PostgreSQL
- Docker
- Grafana
- SQL
- Git & GitHub

---

## Features

### Data Extraction

- Downloads historical stock data from Yahoo Finance.
- Supports:
  - AAPL
  - MSFT
  - GOOGL
  - NVDA

### Database Storage

- Stores stock data in PostgreSQL.
- Uses a composite primary key:
  - ticker
  - date

### Grafana Dashboard

#### Price Analysis

- Closing Price Trend
- Latest Closing Price
- Average Closing Price
- Highest Closing Price
- Lowest Closing Price
- Price Change %

#### Volume Analysis

- Trading Volume Trend
- Highest Trading Volume
- Total Trading Volume

### Dynamic Filters

- Stock Selector Dropdown
- Date Range Filter

---

## Database Schema

### Table: stocks

| Column | Data Type |
|----------|----------|
| ticker | VARCHAR |
| date | TIMESTAMP |
| open | FLOAT |
| high | FLOAT |
| low | FLOAT |
| close | FLOAT |
| volume | BIGINT |

Primary Key:

```sql
(ticker, date)
```

---

## Project Structure

```text
stock-market-pipeline/
│
├── Scripts/
│   ├── create_table.py
│   ├── Extract_script.py
│   └── test_connection.py
│
├── data/
├── docker-compose.yml
├── Requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/stock-market-pipeline.git
cd stock-market-pipeline
```

### Install Dependencies

```bash
pip install -r Requirements.txt
```

### Start PostgreSQL

```bash
docker-compose up -d
```

### Create Database Table

```bash
python Scripts/create_table.py
```

### Load Stock Data

```bash
python Scripts/Extract_script.py
```

---

## Grafana Setup

1. Open Grafana:

```text
http://localhost:3000
```

2. Add PostgreSQL Data Source

3. Connect Grafana to PostgreSQL

4. Import/Create Dashboard

5. Select Stock from Dropdown

6. Analyze Metrics

---

## Sample Dashboard Metrics

### AAPL

| Metric | Value |
|----------|----------|
| Latest Price | 291 |
| Average Price | 307 |
| Highest Price | 317 |
| Lowest Price | 307 |
| Price Change % | -2.49% |

---

## Learning Outcomes

This project helped me gain hands-on experience with:

- Data Extraction using APIs
- ETL Pipeline Development
- PostgreSQL Database Management
- Docker Containerization
- SQL Query Development
- Grafana Dashboard Creation
- Dynamic Dashboard Variables
- Time-Series Data Analysis

---

## Future Improvements

- Apache Airflow Scheduling
- AWS Deployment
- Real-Time Stock Streaming
- Kafka Integration
- CI/CD Pipeline
- Data Quality Monitoring
- Machine Learning Forecasting

---

## Author

**Aditya Mathew**

Aspiring Data Engineer focused on building scalable data pipelines, analytics solutions, and cloud-based data platforms.