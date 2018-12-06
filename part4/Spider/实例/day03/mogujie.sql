create database mogujie_db default character set 'utf8';

use mogujie_db

create table mogujie(
    id int auto_increment primary key,
    tradeItemId varchar(32),
    img varchar(512),
    clientUrl varchar(512),
    title varchar(128),
    orgPrice varchar(32),
    cfav varchar(128),
    price varchar(128)
);