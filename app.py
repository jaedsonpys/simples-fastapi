from fastapi import FastAPI

ITEMS = [{'name': 'Shampoo', 'description': 'Best for hair', 'price': '13.90'},
         {'name': 'Car', 'description': 'Car for childs', 'price': '24.50'},
         {'name': 'Smartphone Xiaomi', 'description': 'High velocity', 'price': '1250.00'},
         {'name': 'Shampoo', 'Notebook Acer': 'For work', 'price': '2500.90'}]

app = FastAPI()


@app.get('/')
def welcome():
    return {'message': 'Welcome'}


@app.get('/items')
def items():
    return ITEMS


@app.get('/items/{item_id}')
def items(item_id: int):
    if item_id >= len(ITEMS):
        return {'message': 'Product not found'}

    return ITEMS[item_id]
