from flask import Flask
import pymysql.cursors
app = Flask(__name__)

@app.route("/")
def index():

    """
    create database kulendayz2018 character set utf8 collate utf8_general_ci;
    use kulendayz2018;
    create table primjer(sifra int not null primary key auto_increment,naziv varchar(50));
    ert into primjer(naziv) values ('Teacherz');
    """

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='kulendayz2018',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select naziv from primjer where sifra=%s"
            cursor.execute(sql, (1))
            rezultatIzBaze = cursor.fetchone()
    finally:
        connection.close()
    
    return "<h1>" + rezultatIzBaze["naziv"] +  "</h1>"

if __name__ == "__main__":
    app.run()
