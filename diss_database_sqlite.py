
import sqlite3

# create a database connection
conn = sqlite3.connect('ddb_python')
print('Opened database successfully')


cur = conn.cursor()


# creating a cursor or something from
# http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

# def select_all_tasks(conn):
#     """
#     Query all rows in the tasks table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)
#
#
# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)


# drop prior YESNO table
conn.execute('drop table YESNO')

# create YESNO table
conn.execute('''create table YESNO
(id integer primary key autoincrement,
value    text    not null);''')
print('YESNO Table created successfully')

# populate YESNO
conn.execute("insert into YESNO (value) \
    VALUES ('yes')")
conn.execute("insert into YESNO (value) \
    VALUES ('no')")
conn.execute("insert into YESNO (value) \
    VALUES ('maybe')")
conn.commit()
print('YESNO Records created successfully')


# drop prior COUNTRIES table
conn.execute('drop table COUNTRIES')


# create COUNTRIES table
conn.execute('''create table COUNTRIES
(id integer primary key autoincrement,
name text not null,
date_independence text,
date_end text,
colony  int,
foreign key (colony) references YESNO(id));''')
print('COUNTRIES Table created successfully')


# def insertCOUNTRIES
def insertCOUNTRIES(name, date_independence, date_end, colony):
    conn.execute("insert into COUNTRIES (name,date_independence,date_end,colony) \
    VALUES (?,?,?,?)", (name, date_independence, date_end, colony))
    conn.commit()
    print('Country Record created successfully')
# insertCOUNTRIES('British India', "NULL", '1947', 1)


# drop prior CITIES table
conn.execute('drop table CITIES')

# create CITIES table
conn.execute('''create table CITIES
(id integer primary key autoincrement,
name text not null,
country_name int,
current int,
foreign key (current) references YESNO(id));''')
print('CITIES Table created successfully')


# def insertCITIES
def insertCITIES(name, country_name, current):
    conn.execute("insert into CITIES (name,country_name,current) \
    VALUES (?,?,?)", (name, country_name, current))
    conn.commit()
    print('City Record created successfully')


# insertCITIES('Lahore', (select id from COUNTRIES where name = 'Pakistan'), 1)
insertCITIES('Multan', 2, 1)
print('Multan created successfully')


# drop prior ARCHIVES table
conn.execute('drop table ARCHIVES')


# create ARCHIVES table
conn.execute('''create table ARCHIVES
(id integer primary key autoincrement,
short_name text not null,
country_name int,
city_name int,
contact text,
website text,
hours text,
foreign key (country_name) references COUNTRIES(id),
foreign key (city_name) references CITIES (id));''')
print('ARCHIVES Table created successfully')


# drop prior EVENT_TYPES table
conn.execute('drop table EVENT_TYPES')


# create EVENT_TYPES table
conn.execute('''create table EVENT_TYPES
(id integer primary key autoincrement,
type text not null,
death_event int,
foreign key (death_event) references YESNO (id));''')
print('EVENT_TYPES Table created successfully')

# drop prior EVENTS table
conn.execute('drop table EVENTS')


# create EVENTS table
conn.execute('''create table EVENTS
(id integer primary key autoincrement,
name text not null,
date_start text,
date_end text,
event_type int,
country_name int,
city_name int,
foreign key (event_type) references EVENT_TYPES(id),
foreign key (country_name) references COUNTRIES(id),
foreign key (city_name) references CITIES (id));''')
print('EVENTS Table created successfully')



# drop prior SITE_TYPES table
conn.execute('drop table SITE_TYPES')


# create SITE_TYPES table
conn.execute('''create table SITE_TYPES
(id integer primary key autoincrement,
type text not null,
body_present int,
body_prev int,
foreign key (body_prev) references YESNO (id)
foreign key (body_present) references YESNO (id));''')
print('SITE_TYPES Table created successfully')


# drop prior SITES table
conn.execute('drop table SITES')


# create SITES table
conn.execute('''create table SITES
(id integer primary key autoincrement,
name text not null,
site_type int,
country_name int,
city_name int,
event_name int,
memorial_present int,
foreign key (site_type) references site_TYPES(id),
foreign key (country_name) references COUNTRIES(id),
foreign key (city_name) references CITIES (id),
foreign key (event_name) references EVENTS (id),
foreign key (memorial_present) references YESNO (id));''')
print('SITES Table created successfully')


# drop prior DEAD_PEOPLE table
conn.execute('drop table DEAD_PEOPLE')


# create DEAD_PEOPLE table
conn.execute('''create table DEAD_PEOPLE
(id integer primary key autoincrement,
name text not null,
birth_date text,
death_date text,
birth_country int,
birth_city int,
death_country int,
death_city int,
foreign key (birth_country) references COUNTRIES(id),
foreign key (birth_city) references CITIES (id),
foreign key (death_country) references COUNTRIES(id),
foreign key (death_city) references CITIES (id));''')
print('DEAD_PEOPLE Table created successfully')


# drop prior ARCHIVE_BOXES table
conn.execute('drop table ARCHIVE_BOXES')


# create ARCHIVE_BOXES Table
conn.execute('''create table ARCHIVE_BOXES
(id integer primary key autoincrement,
shelfmark text not null,
archive_name int,
shelfmark_title text,
shelfmark_description text,
date_start text,
date_end text,
date_acquired text,
alt_shelfmark text,
foreign key (archive_name) references ARCHIVES(id));''')
print('ARCHIVE_BOXES Table created successfully')


# drop prior ARCHIVE_ITEMS table
conn.execute('drop table ARCHIVE_ITEMS')

# create ARCHIVE_ITEMS Table
conn.execute('''create table ARCHIVE_ITEMS
(id integer primary key autoincrement,
name text not null,
item_box int,
date_start text,
date_end text,
foreign key (item_box) references ARCHIVE_BOXES(id));''')
print('ARCHIVE_ITEMS Table created successfully')


# drop prior FILE_TYPES table
conn.execute('drop table FILE_TYPES')

# create FILE_TYPES Table
conn.execute('''create table FILE_TYPES
(id integer primary key autoincrement,
type text not null);''')
print('FILE_TYPES Table created successfully')

# drop prior ARCHIVE_IMAGE_FILES table
conn.execute('drop table ARCHIVE_IMAGE_FILES')

# create ARCHIVE_IMAGE_FILES Table
conn.execute('''create table ARCHIVE_IMAGE_FILES
(id integer primary key autoincrement,
name text not null,
date_created text,
file_type int,
item_box int,
item_name int,
foreign key (file_type) references FILE_TYPES(id),
foreign key (item_box) references ARCHIVE_BOXES(id),
foreign key (item_name) references ARCHIVE_ITEMS(id));''')
print('ARCHIVE_IMAGE_FILES Table created successfully')


# populate COUNTRIES
insertCOUNTRIES('India', 1947, "NULL", 2)

insertCOUNTRIES('Pakistan', 1947, "NULL", 2)

insertCOUNTRIES('Bangladesh', 1971, "NULL", 2)

insertCOUNTRIES('East Pakistan', 1947, 1971, 2)

insertCOUNTRIES('British India', "NULL", '1947', 1)

conn.commit()
print('COUNTRIES Records created successfully')

# populate CITIES


# Indian cities
conn.execute("insert into CITIES (name, country_name, current) values \
('New Delhi',(select id from COUNTRIES where name = 'India'), 1)")

# conn.execute("insert into CITIES (name, country_name, current) values \
# ('Lucknow',(select id from COUNTRIES where name = 'India'), 1)",
# ('Jaipur',(select id from COUNTRIES where name = 'India'), 1)")

# WHY DOESN'T THIS WORK???
# insertCITIES('Lahore', ("select id from COUNTRIES where name = 'Pakistan'"), 1)

# Pakistani cities
conn.execute("insert into CITIES (name, country_name, current) values \
('Lahore',(select id from COUNTRIES where name = 'Pakistan'), 1)")

conn.execute("insert into CITIES (name, country_name, current) values \
('Karachi',(select id from COUNTRIES where name = 'Pakistan'), 1)")

conn.execute("insert into CITIES (name, country_name, current) values \
('Islamabad',(select id from COUNTRIES where name = 'Pakistan'), 1)")

conn.commit()
print('CITIES Records created successfully')


# cursor = conn.execute("SELECT id, name, date_independence, date_end, colony \
# from COUNTRIES")
# for row in cursor:
#     print('id = ' + str(row[0]))
#     print('name = ' + row[1])
#     print('date_independence = ' + row[2])
#     print('date_end = ' + row[3])
#     print('colony = ' + str(row[4]))

cursor = conn.execute("SELECT id, name, country_name, current \
from CITIES")
for row in cursor:
    print('id = ' + str(row[0]))
    print('name = ' + row[1])
    print('country_name = ' + str(row[2]))
    print('current = ' + str(row[3]))



conn.execute("SELECT COUNTRIES.name, YESNO.value \
from COUNTRIES inner join YESNO \
on COUNTRIES.colony = YESNO.id")
print('COUNTRIES.name joined w YESNO successfully')






print('Records printed successfully')
conn.commit()



conn.close()
