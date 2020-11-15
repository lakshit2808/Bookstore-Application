import mysql.connector

class Database:

    def __init__(self):
        self.conn = mysql.connector.connect(host = "localhost" , user="root" , password="root" , database = "BookStore")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS mybook (title VARCHAR(255) , author VARCHAR(255) , year INTEGER(255) , isbn INTEGER(255)) ")
        self.conn.commit()

    def insert(self,title , author , year , isbn):
        self.cur.execute("INSERT INTO mybook VALUES (%s , %s ,%s ,%s)" , (title , author , year , isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM mybook")
        row = self.cur.fetchall()
        return row

    def search(a,self , b ,c ,d):
        self.cur.execute("SELECT * FROM mybook WHERE title OR author OR year OR isbn")
        x = self.cur.fetchall()
        for i in x:
            print(i)
        return x

    def delete(self, isbn):
        self.cur.execute("DELETE FROM mybook WHERE isbn= %s" , (isbn,))
        self.conn.commit()

    def update(self, title , author , year , isbn):
        self.cur.execute("UPDATE mybook SET title = %s , author = %s , year = %s WHERE isbn = %s" , (title , author , year , isbn))
        self.conn.commit()

    def __del__(self):
        self.conn.close()