#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True;
#db = SQLAlchemy(app)


#  MONGODB CREATION
#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydb']
print("Database created........")

#Verification
print("List of databases after creating new one")
print(client.list_database_names())

# DB CREATION AND INSTANTIATION #
#DB -- OPTION 1
engine = create_engine('sqlite:///test.db', echo = True)
meta = MetaData()

# Database Schema for Item and User #
Items = Table(
   'Items', meta, 
   Column('id', Integer, primary_key = True), 
   Column('product_name', String), 
   Column('price', Float), 
   Column('quantity', Integer)
)
Users = Table(
    'Users', meta,
    Column('firstname', String),
    Column('lastname', String),
    Column('email', String),
    Column('passwd', String),
    Column('phone', Integer)
)
meta.create_all(engine)


#class Item(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    product = db.Column(db.String(200))
#    price = db.Column(db.Integer)