START TRANSACTION;

INSERT INTO dim_company
(company_type, company_size, company_category, industry)
VALUES
('Private','Large','Technology','AI');

COMMIT;

-- Use ROLLBACK; if needed before COMMIT.
