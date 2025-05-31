""" Запускаем веб админку """
from web.app import app
from admin import *
load_dotenv()

def start_web():
    app.run(host='0.0.0.0',port=os.getenv('PORT'),use_reloader=False)

if __name__ == '__main__':
    check_admin()
    start_web()