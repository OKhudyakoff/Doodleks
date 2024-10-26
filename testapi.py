from APIPostgres import APIPostgres


db = APIPostgres()

rez = db.executeQuery("create table if not exists test (a int);")

print(rez)

rez = db.executeQuery("insert into test values (1)")

print(rez)

rez = db.executeQuery("select * from test;")

print(rez)
