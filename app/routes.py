from app import app

@app.route('/')
def index():
  return "App is running correctly"
