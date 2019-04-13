from mysql.connector import connect
from mysql.connector.cursor import MySQLCursor

class DB:
  def __init__(self, config):
    self.__connection = connect(**config)
    self.__cursor = self.__connection.cursor()


  def delete(self, query, data):
    try:
      self.__cursor.execute(query, data)
      self.__connection.commit()

    except Exception as e:
      self.__connection.rollback()
      raise e

  def replace(self, query, data):
    try:
      self.__cursor.execute(query, data)
      self.__connection.commit()

    except Exception as e:
      self.__connection.rollback()
      raise e

  def insert(self, query, data):
    try:
      self.__cursor.execute(query, data)
      self.__connection.commit()
      return self.__cursor.lastrowid

    except Exception as e:
      self.__connection.rollback()
      raise e

  def select(self, query, data=None, limit=0):
    self.__cursor.execute(query, data)
    results = None
    if limit == 1:
      results = self.__cursor.fetchone()
    elif limit > 1:
      results = self.__cursor.fetchmany(int(limit))
    else:
      return self.__cursor.fetchall()
    
    try:
      self.__cursor.fetchall()
    except:
      pass
    
    return results
