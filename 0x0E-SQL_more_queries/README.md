# Project: 0x0E. SQL - More queries

This is a continuation to the introduction to MySQL. This project focuses on The following:

- How to create a new user and grant permissions in MySQL.
- How To Use MySQL GRANT Statement To Grant Privileges To a User.
- MySQL constraints
- SQL technique: subqueries
- Basic query operation: the join
- SQL technique: multiple joins and the distinct keyword
- SQL technique: join types
- SQL technique: union and minus
- The Seven Types of SQL Joins
- SQL Style Guide
- MySQL 8.0 SQL Statement Syntax

# __How to import a SQL dump__:

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
![image](https://github.com/user-attachments/assets/57cd77fb-02ac-4252-8615-f4979876f359)


