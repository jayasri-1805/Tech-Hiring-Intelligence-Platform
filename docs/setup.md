# Sprint 3B

1. Install:
   pip install pymysql

2. Update config/db_config.py

3. Test MySQL connection using sql/test_connection.sql

4. Use:

from src.database.mysql_loader import MySQLLoader

MySQLLoader().load("data/analytics/analytics_dataset.csv")
