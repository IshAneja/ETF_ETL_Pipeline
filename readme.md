# 💹 ETF Price ETL Pipeline

This project is an ETL (Extract, Transform, Load) pipeline built in Python that collects daily ETF price data using the [Alpha Vantage API](https://www.alphavantage.co/), processes and cleans the data, and stores it in a local SQLite database. It’s designed to be modular, extensible, and easily integrated into more complex data workflows or dashboards.

---

## 🚀 Features

- Pulls **daily adjusted price data** for selected ETFs (e.g., SPY, QQQ, VTI)
- Transforms and cleans raw API responses using `pandas`
- Stores the data into a **local SQLite database**
- Built-in logging and error handling
- Modular ETL functions for easy scaling
- Secure API key management using environment variables (`.env`)

---

## 📦 Project Structure
```yaml
etf_etl_pipeline/
│
├── ETF_ETL_Pipeline.py # Main script with ETL logic
├── .env # API key stored securely (excluded from Git)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/IshAneja/ETF_ETL_Pipeline.git
cd ETF_ETL_Pipeline
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API Key 
```ini
ALPHA_VANTAGE_API_KEY=your_real_api_key_here
```

### 4. Run ETL Pipeline
```bash
python ETF_ETL_Pipeline.py 
```

## 🗃️ Output
- A local SQLite database named etf_prices.db
- Table: etf_prices
- Columns: date, symbol, open, high, low, close, adjusted_close, volume

## 🔒 Security Note
#### Make sure your .env file is excluded from version control:
```bash 
# .gitignore
.env
```

## 🔄 Future Improvements
- Add support for PostgreSQL, MySQL, or cloud-based data warehouses
- Schedule daily updates with Airflow or Prefect
- Add feature engineering (e.g., moving averages, indicators)
- Build a dashboard using Streamlit, Dash, or Power BI

## 📚 Resources
- [Alpha Vantage API Docs](https://www.alphavantage.co/documentation/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [dotenv Documentation](https://pypi.org/project/python-dotenv/)


## 👤 Author 
### Ish Aneja

📫 [Ish.Aneja@outlook.com](mailto:Ish.Aneja@outlook.com)
🔗 [LinkedIn](https://https://www.linkedin.com/in/ish-aneja/)
📘 [Portfolio](https://ishaneja.github.io/)

## 📄 License
This project is open-source under the MIT License.
