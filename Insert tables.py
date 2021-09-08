import sqlalchemy
import random

db = 'postgresql://user_1:user_1_55555@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

list_executors = ['Andrey', 'Ruslan', 'Misha', 'Ura', 'DJSmash', 'Anaconda', 'Rammstain', 'Aria', 'Linkin Park',
                  'Nice May']
list_alias = ['Andry', 'Rus', 'Crug', 'Long Hand', 'DJSmash', 'Anaconda', 'Rammstain', 'Aria', 'Linkin Park', 'NM']
list_genres = ['Rock',  'Hip hop', 'Reggae', 'Pop', 'Jazz', 'Blues']
list_albums = ['Album 1994', 'Album 1995', 'Album 1996', 'Album 1997', 'Album 1998', 'Album 1999', 'Album 2000',
               'Album 2001', 'Album 2002', 'Album 2003', 'Album 2018', 'Album 2019']
list_years = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2018, 2019]
list_tracks = ['Мой день', 'My son', 'ljeflf', 'kdowpw', 'Drims', 'jfpjf', 'wrpr', '50', '49', 'krp3rk', 'lvnln',
               'nvlnvl', '8048094', '8744', 'My dog']
list_longs = [180, 200, 350, 400, 150, 187, 188, 165, 212, 200, 190, 170, 147, 188, 192]
list_collections = ['Collection 1993', 'Collection 1994', 'Collection 1998', 'Collection 2000', 'Collection 2003',
                    'Collection 2005', 'Collection 2018', 'Collection 2019', 'Collection 2020', 'Collection 2021']
list_coll_years = [1993, 1994, 1998, 2000, 2003, 2005, 2018, 2019, 2020, 2021]

# Заполняем таблицу исполнителей
for i in range(len(list_executors)):
    str_exec = f'''
    INSERT INTO executor
            VALUES({i}, '{list_executors[i]}', '{list_alias[i]}')
    '''

    connection.execute(str_exec)

# Заполняем таблицу жанров
for i in range(len(list_genres)):
    str_genr = f'''
    INSERT INTO genre
        VALUES({i}, '{list_genres[i]}');
    '''
    connection.execute(str_genr)

# Заполнение таблицы альбомы
for i in range(len(list_albums)):
    str_alb = f'''
    INSERT INTO album
        VALUES({i}, '{list_albums[i]}', {list_years[i]});
    '''
    connection.execute(str_alb)

# Заполнение таблицы треки
for i in range(len(list_tracks)):
    str_track = f'''
    INSERT INTO track
        VALUES({i}, '{list_tracks[i]}', {list_longs[i]}, {random.randint(0, len(list_albums) - 1)});
    '''
    connection.execute(str_track)

# Заполнение таблицы сборник
for i in range(len(list_collections)):
    str_coll = f'''
    INSERT INTO collection
        VALUES({i}, '{list_collections[i]}', {list_coll_years[i]});
    '''
    connection.execute(str_coll)

# Заполнение таблицы ЖанрИсполнитель
for i in range(25):
    str_genr_execut = f'''
    INSERT INTO genre_executor
        VALUES({i},  {random.randint(0, len(list_genres)-1)}, {random.randint(0, len(list_executors)-1)});
    '''
    connection.execute(str_genr_execut)

# Заполнение таблицы АльбомИсполнитель
for i in range(25):
    str_alb_execut = f'''
    INSERT INTO album_executor
        VALUES({i}, {random.randint(0, len(list_executors)-1)}, {random.randint(0, len(list_albums)-1)});
    '''
    connection.execute(str_alb_execut)

#Заполнение таблицы ТрекСборник
for i in range(25):
    str_tr_coll = f'''
    INSERT INTO track_collection
        VALUES({i}, {random.randint(0, len(list_collections)-1)}, {random.randint(0, len(list_tracks)-1)});
    '''
    connection.execute(str_tr_coll)
