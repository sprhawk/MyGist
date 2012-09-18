Sqlite3
=======

check if the table exists
-------------------------
select count(type) from sqlite_master where type='table' and name='TABLE_NAME_TO_CHECK';

