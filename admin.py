from db.models import AdminUser, db
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv
load_dotenv()

db.connect(reuse_if_open=True)
try:
    admin = AdminUser.create(
        username="admin",
        password_hash=generate_password_hash(os.getenv('ADMIN_PASSWORD')),
    )
    admin.save()
except Exception as e:
    print("Админ уже существует:", e)
db.close()