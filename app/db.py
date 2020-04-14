import sqlite3
import time


database = 'aes_flask.db'

create_table_sql = '''
CREATE TABLE aes
(
`id` INTEGER PRIMARY KEY NOT NULL,
`time` INT NOT NULL,
`method` VARCHAR(255) NOT NULL,
`content` VARCHAR(255) NOT NULL,
`result` VARCHAR(255) NOT NULL
);
'''


class DB:
    def __init__(self, url):
        self.url = url
        self.db = sqlite3.connect(self.url)

    def execute(self, sql):
        data = []
        try:
            c = self.db.cursor()
            rows = c.execute(sql)
            for row in rows:
                data.append(row)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
        finally:
            self.db.close()
        return data


def init_db():
    db = DB(database)
    db.execute(create_table_sql)


def insert_aes(method, content, result):
    db = DB(database)
    sql = "INSERT INTO aes (`id`, `time`, `method`, `content`, `result`) values(NULL, %s, '%s', '%s', '%s')"
    db.execute(sql % (str(time.time()), method, content, result))


def fetchall_aes():
    db = DB(database)
    data = []
    rows = db.execute("SELECT * from aes;")
    for row in rows:
        data.append({'id': row[0], 'time': row[1], 'method': row[2], 'content': row[3], 'result': row[4]})
    return data


if __name__ == '__main__':
    init_db()
    insert_aes('encode', '1111', 'f1571cdfbe1bc160fb300c2a26bc33bf')
    print(fetchall_aes())
