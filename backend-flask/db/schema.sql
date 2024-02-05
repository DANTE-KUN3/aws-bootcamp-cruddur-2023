CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.activites;

CREATE TABLE public.users(
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    display_name text,
    handle text,
    cognito_user_id text,
    created_at TIMESTAMP DEFAULT current_timestamp NOT NULL
);


CREATE TABLE public.activities (
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    message text NOT NULL,
    replies_count integer DEFAULT 0,
    reposts_count integer DEFAULT 0,
    likes_count integer DEFAULT 0,
    reply_to_activity_uuid UUID,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT current_timestamp NOT NULL
);
