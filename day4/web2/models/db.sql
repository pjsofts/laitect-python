drop table if exists users;
create table users(
    id serial primary key,
    name text,
    lastname text
);

drop table if exists todos;
create table todos(
    id serial primary key,
    title text, 
    done boolean,
    user_id integer references users(id)
);