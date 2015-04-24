-- Make the schema
CREATE SCHEMA IF NOT EXISTS base_api;

-- Make the version table
CREATE TABLE IF NOT EXISTS base_api.version_history (
  version INT PRIMARY KEY,
  upgrade_start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  upgrade_end TIMESTAMP
);

INSERT INTO base_api.version_history (version) VALUES (0);

-- Make the user, give it full access
CREATE USER base_api PASSWORD 'pwgen_-sny_40';
GRANT ALL ON SCHEMA base_api TO base_api;
GRANT ALL ON ALL TABLES IN SCHEMA base_api TO base_api;

-- Readonly user
CREATE USER base_api_readonly PASSWORD 'pwgen_-sny_40';
GRANT USAGE ON SCHEMA base_api TO base_api_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA base_api TO base_api_readonly;

UPDATE base_api.version_history SET upgrade_end=clock_timestamp() WHERE version=0;
