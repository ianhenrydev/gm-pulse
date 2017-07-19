import MySQLdb

db = MySQLdb.connect(host = 'localhost', user = 'supraman', passwd = '', db = 'pulsedb')
cur = db.cursor()
cur.execute("SELECT * FROM hockey LIMIT 1;")
for row in cur.fetchall():
    score = row[0]
    body = row[1]
    for word in body.split():
        lower = word.lower()
        response = db.cursor()
        response.execute("SELECT * FROM features WHERE word =" + lower)
        if (response.fetchall().length == 0):
            db.cursor().execute("INSERT INTO features (word, score, instances) VALUES ('" + lower + "'," + score + "," + "1);")
    
db.close()