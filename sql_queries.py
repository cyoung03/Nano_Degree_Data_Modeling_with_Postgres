# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays (songplay_id serial PRIMARY KEY NOT NULL, start_time timestamp WITH TIME ZONE NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar, user_agent varchar); """)

user_table_create = ("""create table if not exists users (user_id int PRIMARY KEY NOT NULL, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""create table if not exists songs (song_id varchar PRIMARY KEY NOT NULL, title varchar NOT NULL, artist_id varchar, year int, duration float NOT NULL);""")

artist_table_create = ("""create table if not exists artists (artist_id varchar PRIMARY KEY NOT NULL, name varchar NOT NULL, location varchar, latitude float, longitude float);""")

time_table_create = ("""create table if not exists time (start_time timestamp WITH TIME ZONE PRIMARY KEY NOT NULL, hour int, day int, week int, month int, year int, weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; """)

user_table_insert = ("""insert into users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

song_table_insert = ("""insert into songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

artist_table_insert = ("""insert into artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

time_table_insert = (""" insert into time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

# FIND SONGS
song_select = ("""select s.song_id, a.artist_id, s.title, a.name, s.duration
                  from songs s
                  join artists a on s.artist_id = a.artist_id
                  WHERE s.title = %s AND a.name = %s AND s.duration = %s
                  """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# terminate connection

term_conn = """REVOKE CONNECT ON DATABASE TARGET_DB FROM sparkifydb;"""