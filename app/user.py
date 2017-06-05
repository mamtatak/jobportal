import MySQLdb

conn = MySQLdb.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE user (name TEXT, addr TEXT, pin TEXT, con TEXT,gen TEXT,country TEXT,city TEXT,course TEXT,institute TEXT)')
print "Table created successfully";
conn.close()
