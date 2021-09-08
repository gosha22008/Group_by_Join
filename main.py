import sqlalchemy

db = 'postgresql://user_1:user_1_55555@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# 1.количество исполнителей в каждом жанре;
request = f'''
    SELECT count(distinct id_executor), g.name FROM genre_executor ge
      join genre g on ge.id_genre = g.id
	    GROUP BY g.name
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 2.количество треков, вошедших в альбомы 2019-2020 годов;
request = f'''
    select sum(c_n) from (select count(t.name) c_n, year from track t
      left join album a on t.id_album = a.id
      where year between 2019 and 2020
      group by year) x
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 3.средняя продолжительность треков по каждому альбому;
request = f'''
    select avg(long) av, a.name from track t
      join album a on t.id_album = a.id
 	    group by a.name
 	    order by av
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 4.все исполнители, которые не выпустили альбомы в 2020 году;
request = f'''
   select distinct e."name" from executor e
    join album_executor ae on e.id = ae.id_executor
    join album a on ae.id_album = a.id
    where year != 2020
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 5.названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
request = f'''
   select distinct c."name" from executor e
      join album_executor ae on e.id = ae.id_executor
      join album a on ae.id_album = a.id
      join track t on a.id = t.id_album
      join track_collection tc on t.id = tc.id_track
      join collection c on tc.id_collection = c.id
      where e.name = 'Linkin Park'
      '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 6.название альбомов, в которых присутствуют исполнители более 1 жанра;
request = f'''
   select * from (select a.name, count(distinct  ge.id_genre) cg from album a
  join album_executor ae on a.id = ae.id_album
  join executor e on ae.id_executor = e.id
  join genre_executor ge on e.id = ge.id_executor
  group by  a.name) x
  where cg > 1
      '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 7.наименование треков, которые не входят в сборники;
request = f'''
   select t."name" from track t
      left join track_collection tc on t.id = tc.id_track
      where tc.id_track is null
      '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 8.исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
request = f'''
   select e.name,t."name",t.long from executor e
      join album_executor ae on e.id = ae.id_executor
      join album a on ae.id_album = a.id
      join track t on a.id = t.id_album
      where t.long = (select min(long) from track )
      '''
for i in connection.execute(request):
    print(i)
print('-'*30)

# 9.название альбомов, содержащих наименьшее количество треков.
request = f'''
    select a.name, count(t.id) c from album a 
    full join track t on a.id = t.id_album 
    group by a.name
    order by c
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)