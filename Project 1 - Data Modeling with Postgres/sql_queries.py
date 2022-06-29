# DROP TABLES

try:
    songplay_table_drop = "DROP TABLE IF EXISTS songplays"
except Exception as e:
    print('Error dropping table songplays')
    print(e)

try:
    user_table_drop = "DROP TABLE IF EXISTS users"
except Exception as e:
    print('Error dropping table users')
    print(e)

try:
    song_table_drop = "DROP TABLE IF EXISTS songs"
except Exception as e:
    print('Error dropping table songs')
    print(e)

try:
    artist_table_drop = "DROP TABLE IF EXISTS artists"
except Exception as e:
    print('Error dropping table artists')
    print(e)

try:
    time_table_drop = "DROP TABLE IF EXISTS time"
except Exception as e:
    print('Error dropping table time')
    print(e)


# CREATE TABLES

try:
    songplay_table_create = ("""
        CREATE TABLE IF NOT EXISTS songplays (
            songplay_id int PRIMARY KEY
            ,start_time TIMESTAMP
            ,user_id int
            ,level varchar
            ,song_id varchar
            ,artist_id varchar
            ,session_id int
            ,location varchar
            ,user_agent varchar
        );
    """)
except Exception as e:
    print('Error creating table songplays')
    print(e)

try:
    user_table_create = ("""
        CREATE TABLE IF NOT EXISTS users (
            user_id int PRIMARY KEY
            ,first_name varchar
            ,last_name varchar
            ,gender varchar
            ,level varchar
        );
    """)
except Exception as e:
    print('Error creating table users')
    print(e)

try:
    song_table_create = ("""
        CREATE TABLE IF NOT EXISTS songs (
            song_id varchar PRIMARY KEY
            ,title varchar
            ,artist_id varchar
            ,year int
            ,duration float
        );
    """)
except Exception as e:
    print('Error creating table songs')
    print(e)

try:
    artist_table_create = ("""
        CREATE TABLE IF NOT EXISTS artists (
            artist_id varchar PRIMARY KEY
            ,name varchar
            ,location varchar
            ,latitude float
            ,longitude float
        );
    """)
except Exception as e:
    print('Error creating table artists')
    print(e)

try:
    time_table_create = ("""
        CREATE TABLE IF NOT EXISTS time (
            star_time TIMESTAMP PRIMARY KEY
            ,hour int
            ,day int
            ,week int
            ,month int
            ,year int
            ,weekday int
        );
    """)
except Exception as e:
    print('Error creating table time')
    print(e)


# INSERT RECORDS

try:
    songplay_table_insert = ("""
        INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (songplay_id) DO NOTHING;
    """)
except Exception as e:
    print('Error inserting data into songplays')
    print(e)

try:
    user_table_insert = ("""
        INSERT INTO users (user_id, first_name, last_name, gender, level)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING;
    """)
except Exception as e:
    print('Error inserting data into users')
    print(e)

try:
    song_table_insert = ("""
        INSERT INTO songs (song_id, title, artist_id, year, duration)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (song_id) DO NOTHING;
    """)
except Exception as e:
    print('Error inserting data into songs')
    print(e)

try:
    artist_table_insert = ("""
        INSERT INTO artists (artist_id, name, location, longitude, latitude)
        VALUES  (%s, %s, %s, %s, %s)
        ON CONFLICT (artist_id) DO NOTHING;
    """)
except Exception as e:
    print('Error inserting data into artists')
    print(e)

try:
    time_table_insert = ("""
        INSERT INTO time (star_time, hour, day, week, month, year, weekday)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """)
except Exception as e:
    print('Error inserting data into time')
    print(e)


# FIND SONGS
# artists table, and original log file are all needed for the songplays table. Since the log file does not specify an ID for either the song or the artist,
# you’ll need to get the song ID
# and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time.
song_select = ("""
    SELECT * 
    FROM songs as s join artists as a on s.artist_id = a.artist_id
    WHERE s.title = %s and
          a.name = %s  and
          s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
