CREATE DATABASE SBRP_SCHEMA;
USE SBRP_SCHEMA;

CREATE TABLE STAFF
(STAFF_ID		int				not null,
STAFF_FNAME		varchar(50)		not null,
STAFF_LNAME		varchar(50)		not null,
DEPT			varchar(50)		not null,
COUNTRY			varchar(50)		not null,
EMAIL			varchar(50)		not null,
CONSTRAINT STAFF_PK PRIMARY KEY (STAFF_ID));

CREATE TABLE STAFF_ACCESS
(STAFF_ID		int		not null,
ACCESS_RIGHTS	int		not null,
CONSTRAINT STAFF_ACCESS_PK PRIMARY KEY (STAFF_ID),
CONSTRAINT STAFF_FK1 FOREIGN KEY (STAFF_ID) REFERENCES STAFF_ACCESS(STAFF_ID));

CREATE TABLE STAFF_SKILL
(STAFF_ID		int				not null,
SKILL_NAME		varchar(50) 	not null,
CONSTRAINT STAFF_SKILL_PK PRIMARY KEY (STAFF_ID, SKILL_NAME),
CONSTRAINT STAFF_SKILL_FK1 FOREIGN KEY (STAFF_ID) REFERENCES STAFF(STAFF_ID));

CREATE TABLE ROLE_SKILL
(ROLE_NAME		varchar(20) 	not null,
SKILL_NAME		varchar(50) 	not null,
CONSTRAINT ROLE_SKILL_PK PRIMARY KEY (ROLE_NAME, SKILL_NAME));

CREATE TABLE STAFF_ROLE_SKILL
(STAFF_ID		int				not null,
ROLE_NAME		varchar(20) 	not null,
SKILL_NAME		varchar(50) 	not null,
CONSTRAINT STAFF_ROLE_SKILL_PK PRIMARY KEY (STAFF_ID),
CONSTRAINT STAFF_ROLE_SKILL_FK1 FOREIGN KEY (STAFF_ID, SKILL_NAME) REFERENCES STAFF_SKILL(STAFF_ID, SKILL_NAME),
CONSTRAINT STAFF_ROLE_SKILL_FK2 FOREIGN KEY (ROLE_NAME, SKILL_NAME) REFERENCES ROLE_SKILL(ROLE_NAME, SKILL_NAME));


#DROP SCHEMA SBRP_SCHEMA;

