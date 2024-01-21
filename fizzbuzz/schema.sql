DROP TABLE IF EXISTS requests;

CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    param_int1 INT NOT NULL,
    param_int2 INT NOT NULL,
    param_limit INT NOT NULL,
    param_str1 TEXT NOT NULL,
    param_str2 TEXT NOT NULL,
    created_dt DATE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
