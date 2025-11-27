from datetime import datetime, timedelta
import random
from faker import Faker

from ..database.models import Order, User
from ..database.connection import SessionLocal

fake = Faker("en_IN")   # Indian names & emails
db = SessionLocal()

# ------------------------------------------------
# 1. Create 50 Realistic Indian Users
# ------------------------------------------------
users = []
for _ in range(50):
    user = User(
        name=fake.name(),
        email=fake.email(),
        created_at=fake.date_time_this_year()
    )
    users.append(user)

db.add_all(users)
db.commit()

# Reload users with IDs
users = db.query(User).all()

# ------------------------------------------------
# 2. Create 50 Orders Linked to Random Users
# ------------------------------------------------
orders = []
for _ in range(50):
    random_user = random.choice(users)
    order = Order(
        user_id=random_user.id,
        total=round(random.uniform(100, 5000), 2),
        created_at=fake.date_time_this_year()
    )
    orders.append(order)

db.add_all(orders)
db.commit()

db.close()

print("Inserted 50 realistic users and 50 orders successfully!")
