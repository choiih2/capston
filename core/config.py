# core/config.py
DIR_WORDLIST = "wordlists/directories.txt"
SQLI_ERROR_FILE = "payloads/sqli_error.txt"
SQLI_UNION_FILE = "payloads/sqli_union.txt"
SQLI_TIME_FILE = "payloads/sqli_time.txt"
XSS_PAYLOADS = "payloads/xss.txt"

# DB config (기본값; 필요하면 수정)
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "rootpassword",
    "db": "mydb",
    "charset": "utf8",
    "autocommit": True
}
