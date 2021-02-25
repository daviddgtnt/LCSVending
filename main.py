from flask import Flask, render_template, request, redirect
from mysql import connector

site = Flask('__main__')
site.config['DEBUG'] = True

@site.route('/')
def home():
  conn = connector.connect(
    host="daviddgtntshouse.tk",
    user="lcsdev",
    password="idontcarewhatudo",
    database="lcsvendingmachinedev"
  )

  c = conn.cursor()

  c.execute('SELECT * FROM drinks ORDER BY id')

  drinkresult = c.fetchall()

  drinkbuffer = []

  c.execute('SELECT * FROM snacks ORDER BY id')

  snackresult = c.fetchall()

  snackbuffer = []

  conn.close()

  for i in drinkresult:
    drinkbuffer.append(i)

  for i in snackresult:
    snackbuffer.append(i)

  return render_template('home.html', drinklist=drinkbuffer, snacklist=snackbuffer)

@site.route('/editdrink', methods=["POST"])
def editdrink():
  ida = request.form.get('id')

  conn = connector.connect(
    host="daviddgtntshouse.tk",
    user="lcsdev",
    password="idontcarewhatudo",
    database="lcsvendingmachinedev"
  )

  c = conn.cursor()

  c.execute(f'SELECT * FROM drinks WHERE id = {ida}')

  tuples = c.fetchone()

  return render_template('editdrink.html', tuples=tuples)

@site.route('/drinkpost', methods=["POST"])
def editpost():
  ida = f"{request.form.get('id')}"

  item = request.form.get('item')

  slot = request.form.get('slot')

  stock = f"{request.form.get('stock')}"

  extra = f"{request.form.get('extra')}"

  store = f"{request.form.get('store')}"

  price = f"{request.form.get('price')}"

  conn = connector.connect(
    host="daviddgtntshouse.tk",
    user="lcsdev",
    password="idontcarewhatudo",
    database="lcsvendingmachinedev"
  )

  c = conn.cursor()

  c.execute(f"UPDATE drinks SET item = '{item}', slot = '{slot}', stock = {stock}, extra = {extra}, store = {store}, price = {price} WHERE id = {ida}")

  conn.commit()

  conn.close()

  return redirect('/')

@site.route('/editsnack', methods=["POST"])
def editsnack():
  ida = request.form.get('id')

  conn = connector.connect(
    host="daviddgtntshouse.tk",
    user="lcsdev",
    password="idontcarewhatudo",
    database="lcsvendingmachinedev"
  )

  c = conn.cursor()

  c.execute(f'SELECT * FROM snacks WHERE id = {ida}')

  tuples = c.fetchone()

  return render_template('editsnack.html', tuples=tuples)

@site.route('/snackpost', methods=["POST"])
def snackpost():
  ida = f"{request.form.get('id')}"

  item = request.form.get('item')

  slot = request.form.get('slot')

  stock = f"{request.form.get('stock')}"

  extra = f"{request.form.get('extra')}"

  store = f"{request.form.get('store')}"

  price = f"{request.form.get('price')}"

  conn = connector.connect(
    host="daviddgtntshouse.tk",
    user="lcsdev",
    password="idontcarewhatudo",
    database="lcsvendingmachinedev"
  )

  c = conn.cursor()

  c.execute(f"UPDATE snacks SET item = '{item}', slot = '{slot}', stock = {stock}, extra = {extra}, store = {store}, price = {price} WHERE id = {ida}")

  conn.commit()

  conn.close()

  return redirect('/')

site.run(host="0.0.0.0", port=8080)