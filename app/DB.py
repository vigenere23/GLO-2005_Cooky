from mysql.connector import connect
from mysql.connector.cursor import MySQLCursor

class DB:
  def __init__(self, config):
    self.__connection = connect(**config)
    self.__cursor = self.__connection.cursor()

  def insert(self, query, data):
    try:
      results = self.__cursor.execute(query, data, multi=True)
      self.__connection.commit()
      return results

    except Exception as e:
      self.__connection.rollback()
      raise e

  def insertMany(self, query, data):
    if (not isinstance(data, list)):
      raise Exception("Data must be a list")

    try:
      results = self.__cursor.executeMany(query, data, multi=True)
      self.__connection.commit()
      return results

    except Exception as e:
      self.__connection.rollback()
      raise e

  def select(self, query, data, limit=0):
    self.__cursor.execute(query, data)
    if limit == 1:
      return self.__cursor.fetchone()
    elif limit > 1:
      return self.__cursor.fetchmany(int(limit))
    else:
      return self.__cursor.fetchall()
