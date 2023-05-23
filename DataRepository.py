from psycopg2 import *

class DataRepository:
    
      def __init__(self) -> None:
            try:
                  self.conn = connect(
                        database="postgres",
                        user="postgres",
                        password="1001",
                        host="82.146.47.232",
                        port="5432",

                  )
                  self.cursor = self.conn.cursor()
            except Exception as e:
                  print(e)
      
      def insertVoltageValue(self, value):
            self.cursor.execute(f"INSERT INTO temperature_value (voltage) VALUES ({value})")
            self.conn.commit()

      
# Блок для тестирования, можно запустить файл и он запишел двойку в бд
if __name__ == "__main__":

      rep = DataRepository()
      rep.insertVoltageValue(2)
      rep.conn.close()
