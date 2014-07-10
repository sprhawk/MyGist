MySQL
=====

desc tablename

show index from tablename


Clear command line history:
'''
    rm ~/.mysql_history
'''


show all users:
'''
    SELECT User, Host, Password FROM mysql.user;
'''    

reset root password:
1. stop mysqld service
2. mysqld_safe --skip-grant-tables &
3. mysql
4. 

'''
    update mysql.user set password=password('') where user="root";
    flush privileges;
''' 

