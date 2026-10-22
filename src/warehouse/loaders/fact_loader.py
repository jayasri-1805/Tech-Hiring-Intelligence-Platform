from ..database import Database

class FactLoader:

    def load(self, dataframe):
        """
        Placeholder Fact Loader.
        Sprint 3C.5 focuses on ETL orchestration.
        Foreign-key lookup logic will be expanded later.
        """
        conn = Database().connect()
        cursor = conn.cursor()

        loaded = 0

        for _, row in dataframe.iterrows():
            try:
                cursor.execute(
                    """
                    INSERT INTO fact_jobs
                    (
                        job_id,
                        company_id,
                        location_id,
                        date_id,
                        experience_id,
                        remote_id,
                        salary_id,
                        salary_range,
                        high_paying_job,
                        employment_type,
                        job_title
                    )
                    VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        str(row.get("job_id")),
                        1, 1, 1, 1, 1, 1,
                        row.get("salary_range",0),
                        row.get("high_paying_job",False),
                        row.get("employment_type",None),
                        row.get("job_title",None),
                    )
                )
                loaded += 1
            except Exception:
                pass

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Fact rows inserted: {loaded}")
