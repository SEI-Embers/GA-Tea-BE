CREATE USER nine_admin WITH PASSWORD '9259';

CREATE DATABASE GATea;

ALTER DATABASE GATea OWNER TO nine_admin;

GRANT ALL PRIVILEGES ON DATABASE GATea TO nine_admin;