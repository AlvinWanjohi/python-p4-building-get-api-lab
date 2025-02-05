from server.models import db, Bakery, BakedGood
from datetime import datetime

# Sample bakeries
bakery1 = Bakery(name='Delightful donuts', created_at=datetime.utcnow())
bakery2 = Bakery(name='Incredible crullers', created_at=datetime.utcnow())

db.session.add(bakery1)
db.session.add(bakery2)
db.session.commit()

# Sample baked goods
baked_good1 = BakedGood(name='Chocolate dipped donut', price=2.75, bakery_id=1)
baked_good2 = BakedGood(name='Apple-spice filled donut', price=3.5, bakery_id=1)
baked_good3 = BakedGood(name='Glazed honey cruller', price=3.25, bakery_id=2)
baked_good4 = BakedGood(name='Chocolate cruller', price=100, bakery_id=2)

db.session.add(baked_good1)
db.session.add(baked_good2)
db.session.add(baked_good3)
db.session.add(baked_good4)
db.session.commit()

print("Database seeded successfully!")
