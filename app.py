from japronto import Application
import random
import string
import os
import sqlite3

NUMBER_OF_RANDOM_LETTERS_IN_DESCRIPTION = 200
NUMBER_OF_PRODUCTS = 50000
conn = sqlite3.connect('example.sqlite')


init = True
if init:
    try:
        os.remove('example.sqlite')
    except:
        pass
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE product (
            product_id INTEGER PRIMARY KEY, 
            description TEXT)''')
    for product_id in range(1, NUMBER_OF_PRODUCTS + 1):
        description = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for n in range(NUMBER_OF_RANDOM_LETTERS_IN_DESCRIPTION))
        c.execute('INSERT INTO product VALUES (?, ?)', (product_id, description))
    conn.commit()


def params(request):
    product_id = request.match_dict['product_id']
    # actually discard `product_id` and use random
    product_id = random.randint(1, NUMBER_OF_PRODUCTS)
    c = conn.cursor()
    c.execute('SELECT description FROM product WHERE product_id=?', (product_id, ))
    description, = c.fetchone()
    return request.Response(text=description)


app = Application()
app.router.add_route('/{product_id}', params)
app.run(debug=False)
