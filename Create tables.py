import sqlalchemy

db = 'postgresql://user_1:user_1_55555@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

req = '''
    create table if not exists collection (
	id serial primary key,
	name varchar(40) not null unique,
	year integer check(year > 0)
);
create table if not exists genre (
	id serial primary key,
	name varchar(40) not null unique
);
create table if not exists executor (
	id serial primary key,
	name varchar(40) not null unique,
	alias varchar(40) not null unique
);
create table if not exists album (
	id serial primary key,
	name varchar(40) not null,
	year integer check(year > 0)
);
create table if not exists track (
	id serial primary key,
	name VARCHAR(40) not null,
	long integer check(long > 0) ,
	id_album integer references album(id)
);
create table if not exists track_collection (
	id serial primary key,
	id_collection integer references collection(id),
	id_track integer references track(id)
);
create table if not exists genre_executor (
	id serial primary key,
	id_genre integer references genre(id),
	id_executor integer references executor(id)
);
create table if not exists album_executor (
	id serial primary key,
	id_executor integer references executor(id),
	id_album integer references album(id)
);
    '''

connection.execute(req)