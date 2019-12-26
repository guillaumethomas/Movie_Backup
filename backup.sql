/* create first table */

create table film_locations(
filename varchar(255) not null primary key,
filelocation json not null,
backup boolean not null);

http://www.postgresqltutorial.com/postgresql-insert/
http://www.postgresqltutorial.com/postgresql-json/
http://www.postgresqltutorial.com/postgresql-boolean/

insert into film_locations(filename, filelocation, backup) values ('test2', '{ "customer": "sterenn Doe", "items": {"product": "Beer","qty": 9}}', FALSE);

create table data_source(
id              SERIAL PRIMARY KEY,
title           VARCHAR(100) NOT NULL,
ip              INET,
folder          VARCHAR(300)
);