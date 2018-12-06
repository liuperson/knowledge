create database maoyan default character set utf8;

use maoyan;

create table movie(
    id int auto_increment primary key,
    name varchar(256),
    actor varchar(256),
    release_time varchar(128),
    score varchar(128)
);

