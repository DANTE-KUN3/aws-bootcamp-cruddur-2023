from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import pool,query_wrap_array


tracer = trace.get_tracer("home.activities")

class HomeActivities:
    def run(self):
        #logger.info("HomeActivities")
        #with tracer.start_as_current_span("home-activities-mock-data"):
            #span=trace.get_current_span()
            #now = datetime.now(timezone.utc).astimezone()
            #span.set_attribute("app.now",now.isoformat())
            #span.set_attribute("app.result_length",len(results))

        sql = query_wrap_array('''
            SELECT 
                activities.uuid,
                users.display_name,
                users.handle,
                activities.message,
                activities.replies_count,
                activities.reposts_count,
                activities.likes_count,
                activities.reply_to_activity_uuid,
                activities.expires_at,
                activities.created_at
            FROM public.activities
            LEFT JOIN public.users ON users.uuid=activities.user_uuid
            ORDER BY activities.created_at DESC
        ''')
        print("sql---------")
        print(sql)
        print("sql--------")

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                json = cur.fetchone()

        return json[0]
