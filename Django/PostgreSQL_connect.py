import psycopg2


conn = psycopg2.connect(database="db2", user="postgres", password="12345678", host="10.10.31.6", port="5432")
cur = conn.cursor()

