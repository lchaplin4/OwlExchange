from random import randint
from models import db, Product, Category
from app import app

with app.app_context():
    db.drop_all(); db.create_all()

    cats = [Category(name=n) for n in ["Hats", "Shirts", "Shoes"]]
    db.session.add_all(cats); db.session.commit()

    items = []
    for i in range(1, 40):
        c = cats[i % len(cats)]
        items.append(Product(
            title=f"Item {i}",
            description="Sample item",
            price_cents=randint(500, 15000),
            stock=randint(0, 50),
            image_url=f"https://picsum.photos/seed/{i}/600/400",
            category=c
        ))
    db.session.add_all(items); db.session.commit()
    print("Database seeded with sample data.")
