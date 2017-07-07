from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import random
import string

# Imports for database
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

# Imports for OAuth login
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all categories
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    return render_template('catalog.html')


# Show category items
@app.route('/catalog/<string:category_name>/')
def showCategoryItems(category_name):
    return render_template('category_items.html')


# New item
@app.route('/catalog/<string:category_name>/new/')
def newItem(category_name):
    return render_template('new_item.html')


# Show item details
@app.route('/catalog/<string:category_name>/<string:item_name>/')
def showItem(category_name, item_name):
    return render_template('item.html')


# Edit item
@app.route('/catalog/<string:category_name>/<string:item_name>/edit/')
def editItem(category_name, item_name):
    return render_template('edit_item.html')


# Delete item
@app.route('/catalog/<string:category_name>/<string:item_name>/delete/')
def deleteItem(category_name, item_name):
    return render_template('delete_item.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)