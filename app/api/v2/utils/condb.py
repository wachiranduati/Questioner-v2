import psycopg2
class CrudDatabase():
    def __init__(self):
        pass

    @staticmethod
    def ConnectToDB(x):
        try:
            connection = psycopg2.connect(database='mydb', user='postgres', host='localhost', password='root', port=5432)
            cur = connection.cursor()
            cur.execute(x)
            connection.commit()
            cur.close()
            # print("Table created succefully")
        except Exception as e:
            print(e)