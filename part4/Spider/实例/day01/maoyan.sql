create database maoyan_db default character set 'utf8';

use maoyan_db

create table maoyan(
    id int auto_increment primary key,
    actor varchar(512),
    movie varchar(512),
    score varchar(32),
    rate varchar(32),
    time varchar(128),
    image varchar(1024)
);

create index ix_maoyan_actor on maoyan(actor);

create unique index ux_maoyan_movie on maoyan(movie);

