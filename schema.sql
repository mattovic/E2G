DROP TABLE main;

CREATE TABLE main (
record_id varchar(32),
exercise_id varchar(32),
catalog_id varchar(32),
resistance decimal(4,3),
repetition integer,
date varchar(10),
created_at varchar(50)
);

DROP TABLE exercise;

CREATE TABLE exercise (
exercise_id varchar(32),
name varchar(50),
catalog_id varchar(32)
);

DROP TABLE catalog;

CREATE TABLE catalog (
catalog_id varchar(32),
name varchar(50)
);

DROP TABLE user;

CREATE TABLE user (
user_id varchar(32),
name varchar(50),
token varchar(32),
password varchar(50)
);
