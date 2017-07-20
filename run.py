"""This script starts the application"""
from app.views import app
app.run(debug=True)

if __name__ == '__main__':
    app.run()
