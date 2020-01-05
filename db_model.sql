-- create database ggpy

create table users (
    id serial primary key,
    name varchar(50) not null unique,
    hashed_password char(80)
);

create table messages (
    id serial primary key,
    from_id int not null,
    to_id int not null,
    date_sent timestamp not null,
    contents text,

    foreign key (from_id)
    references users (id)
    on delete cascade,

    foreign key (to_id)
    references users (id)
    on delete cascade
);
