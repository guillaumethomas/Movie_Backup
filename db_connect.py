import psycopg2

'''
http://www.postgresqltutorial.com/postgresql-python/insert/
http://www.postgresqltutorial.com/postgresql-python/query/
http://www.postgresqltutorial.com/postgresql-boolean/
http://www.postgresqltutorial.com/postgresql-json/
'''

# conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")


class PsqlConnect:

    def __init__(self, db, cred):

        self.conn = psycopg2.connect(host=db["host"],
                                database=db["database"],
                                user=cred["user"],
                                password=cred["password"])
        self.cursor = self.conn.cursor()
        self.test = "test"

    def query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.errors.UndefinedTable:
            return None

    def insert(self, sql):
        self.cursor.execute('''insert into film_locations(filename, filelocation, backup) values ('test3', '{ "customer": "sterenn Doe", "items": {"product": "Beer","qty": 9}}', FALSE);''')
        self.conn.commit()

if __name__ == "__main__":

    db_info = {
            "host": "192.168.86.143",
            "database": "backup",
                }

    cred_info = {
             "user": "guillaume",
             "password": "psql"
                }

    query = '''SELECT * from film_locations;'''


    connect = PsqlConnect(db_info, cred_info)
    '''
    con = connect.cursor
    con.execute(query)
    rows = con.fetchall()
    for row in rows:
        print(row)
    print("test")
    '''
    connect.insert("t")

    res = connect.query(query)
    if res is not None:
        for row in res:
            print(row)


