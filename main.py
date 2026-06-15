from fastapi import FastAPI,Depends
from models import Product
from database_config import session,engine
import database_models
from sqlalchemy.orm import Session

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

# now every time I open this application, It should check if table if empty then fill it with dummy data. and if it has any data, just don't do it 

products = [
  Product(id=1,name="Phone",description="budget phone",price=99,quantity=10),
  Product(id=2,name="laptop",description="gaming laptop", price=999,quantity=6),
  Product(id=3,name="Table", description="wooden table", price=120, quantity=500),
  Product(id=8,name="Bag", description="Tracking Bag", price=400, quantity=50),
  Product(id=6,name="Chair", description="wooden chair", price=100, quantity=500)
]

def get_db():
  db = session()
  try :
    yield db
  finally:
    db.close()


# populating db with dummy data
def init_db():
  db = session()

  count = db.query(database_models.Product).count()

  if count == 0:
    for product in products:
      db.add(database_models.Product(**product.model_dump()))
  db.commit()

init_db()

@app.get("/")
def greet():
  return "Welcome to Home"

@app.get("/products")
def get_all_products(db : Session = Depends(get_db)):
  db_products = db.query(database_models.Product).all()
  return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db : Session = Depends(get_db)):
  db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
  if db_product:
    return db_product
  return "Product Not Found"

@app.post("/product")
def add_product(product:Product,db : Session = Depends(get_db)):
  db.add(database_models.Product(**product.model_dump()))
  db.commit()
  return product


@app.put("/product")
def update_product(id:int, product:Product,db : Session = Depends(get_db)):
  db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
  if db_product:
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
  else :
    return "No Product Found"


@app.delete("/product",)
def delete_product(id:int,db : Session = Depends(get_db)):
  db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

  if db_product:
    db.delete(db_product)
    db.commit()
  else:
    return "product not found"
