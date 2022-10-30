# importing flask module fro
from Tools.scripts.dutree import display
from flask import Flask, render_template, request, g
from flaskext.mysql import MySQL
import requests  # for API example
import urllib.parse  # for API example

mysql = MySQL()

# initializing a variable of Flask
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'feed_me'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


con = mysql.connect()
cur = con.cursor()
con = mysql.connect()
cur = con.cursor()
cur.execute('SELECT recipe_id,name FROM recipes WHERE category = "Non-Vegeterian" ORDER BY RAND() LIMIT 1')
data = cur.fetchone()
print(data)
recipe_id = data[0]
recipe_nm = data[1]
print(recipe_id)
print(recipe_nm)
cur.execute('SELECT name,price FROM ingredients WHERE ingredient_id IN '
                '(SELECT ingredient_id FROM relations WHERE recipe_id ='
                '(%s))', recipe_id)
ing = cur.fetchall()
print(ing)

if __name__ == "__main__":
    app.run()
