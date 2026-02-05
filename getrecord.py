import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='pyapp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_by_id(record_id):
    """IDを基にrecordsテーブルから1件取得する"""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM records WHERE id = %s"
            cursor.execute(sql, (record_id,))
            return cursor.fetchone()
