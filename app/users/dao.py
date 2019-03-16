from app import db

def getAll():
  data = []
  query = 'SELECT * FROM Utilisateur'
  results = db.select(query)
  for result in results:
    data.append({
      "id": result[0],
      "username": result[1],
      "password": result[2],
      "settings": result[3]
    })
  return data