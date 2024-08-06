
CREATE DATABASE azuredb;

-- Connect to the database
\c azuredb;



CREATE TABLE public.pipeline_runs (
    pipeline_name character varying(255),
    run_id integer,
    env character varying(255),
    start_time character varying(255),
    end_time character varying(255),
    status character varying(255),
    result character varying(255),
    branch character varying(255),
    requestor character varying(255),
    ci_mode character varying(255)
);