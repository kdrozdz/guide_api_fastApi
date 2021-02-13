
CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE ,
    location CHAR NOT NULL,
    hashed_password VARCHAR NOT NULL,
    disabled boolean DEFAULT false);"""

CREATE_ANNOUNCEMENT_TABLE = """CREATE TABLE IF NOT EXISTS announcement (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_time VARCHAR NOT NULL,
    location CHAR NOT NULL,
    language VARCHAR NOT NULL,
    owner INTEGER NOT NULL REFERENCES  users ON DELETE CASCADE
    );"""

CREATE_ADVICE_TABLE = """CREATE TABLE IF NOT EXISTS advice (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_time VARCHAR NOT NULL,
    owner INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    announcement INTEGER NOT NULL REFERENCES announcement ON DELETE CASCADE
    );"""

CREATE_REPUTATION_TABLE = """CREATE TABLE IF NOT EXISTS reputation (
    id SERIAL PRIMARY KEY,
    rating INTEGER NOT NULL,
    text VARCHAR,
    from_user INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    to_user INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    created_time VARCHAR NOT NULL,
    UNIQUE (from_user, to_user)
    );"""
