create table north (
north_id SERIAL primary key,
row_1 varchar(30),
row_2 varchar(30),
row_3 varchar(30),
sid INT REFERENCES northwest (sid)
);

