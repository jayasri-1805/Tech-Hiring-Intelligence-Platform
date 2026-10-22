from ..database import Database

class DimensionWriter:

    def insert_dataframe(self, dataframe, table_name):
        conn = Database().connect()
        cursor = conn.cursor()

        columns = list(dataframe.columns)
        placeholders = ", ".join(["%s"] * len(columns))
        column_sql = ", ".join(columns)

        sql = f"INSERT INTO {table_name} ({column_sql}) VALUES ({placeholders})"

        inserted = 0
        for row in dataframe.itertuples(index=False, name=None):
            try:
                cursor.execute(sql, row)
                inserted += 1
            except Exception:
                # Skip duplicates or invalid rows
                pass

        conn.commit()
        cursor.close()
        conn.close()

        print(f"{table_name}: {inserted} rows inserted")
