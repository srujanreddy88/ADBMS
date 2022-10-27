import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'cars' },
        { "description": 'bikes' },
        { "description": 'trucks' },
        { "description": 'planes' },
        { "description": 'buses' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()