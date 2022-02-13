import psycopg2
from psycopg2 import extras


class PostgresDBProvider:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='d958ji5nfk24vc',
            user='kurlhatungnccl',
            password='64d9ecb15d8f85a7e244d938ef3b1db84f7ecff212211aee97fff776eb830e11',
            host='ec2-34-249-49-9.eu-west-1.compute.amazonaws.com',
        )
        self.cursor = self.conn.cursor(cursor_factory=extras.DictCursor)

    def query(self, query, need_result=True):
        """"""
        self.cursor.execute('ROLLBACK')
        self.conn.commit()

        self.cursor.execute(query)
        if need_result:
            result = self.cursor.fetchall()
            return [dict(row) for row in result]
        else:
            self.conn.commit()


db_provider = PostgresDBProvider()
