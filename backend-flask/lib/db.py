from psycopg_pool import ConnectionPool
import os


def query_wrap_object(template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
        {template}
    ) object_row);
    """
    return sql

def query_wrap_array(template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
        {template}
    ) array_row);
    """
    return sql

def get_connection():
    connection_url = os.getenv("CONNECTION_URL")
    pool = ConnectionPool(connection_url)
    

# Usage example:
# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute(query_wrap_objects('SELECT * FROM my_table'))
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# cursor.close()
# pool.putconn(conn)
