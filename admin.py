from db.models import AdminUser, db
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv
from Sample_data import new_data
load_dotenv()

db.connect(reuse_if_open=True)
i=0
try:
    admin = AdminUser.create(
        username="admin",
        password_hash=generate_password_hash(os.getenv('ADMIN_PASSWORD')),
    )
    admin.save()
    i=1
except Exception as e:
    print("Админ уже существует:", e)

if i==1:
    new_data()
db.close()