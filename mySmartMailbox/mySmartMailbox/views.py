"""
Routes and views for the flask application.
"""
import forms
import config_mysql
import SQL_lib
# import config_cosmos
import pydocumentdb.document_client as document_client
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from flask import render_template
from mySmartMailbox import app

import numpy as np
@app.route('/')
@app.route('/home')
def home():

    # Open database connection
    cnx = mysql.connector.connect(user=config_mysql.DB_USER, password=config_mysql.DB_PASSWORD,
                                  host=config_mysql.DB_HOST, port = config_mysql.DB_PORT,
                                  database=config_mysql.DB_NAME)

    # prepare a cursor object using cursor() method
    cursor = cnx.cursor()

    # Get data from database table:
    # box-id="hello"
    boxid="mailbox-container-1"
    query = SQL_lib.get_cleanning_data(boxid)
    SQL_lib.excute_query(query,cursor, extra_text = " Getting data" )
    data = cursor.fetchall()
    print data

    # Get first row (= first box)
    row=data[0]
    print row

    ## Get data from colums as list objects
    #data_table=np.array(data)
    #help_B=np.asmatrix(data_table)
    #time_list=help_B[:,0]
    #temp_list=help_B[:,1]
    #ph_list=help_B[:,2]
    #pressure_list=help_B[:,3]
    #conduc_list=help_B[:,4]
    # Create data string for chart format
    #data_str = "["
    #Npoints, Nvar = help_B.shape
    #for i in range(Npoints):
    #    time = help_B[i,0]
    #    press = help_B[i,3]
    #    data_str = data_str + "[Date.UTC(%i,%i,%i,%i,%i,%i), %.2f],"%(time.year,time.month,time.day,time.hour,time.minute,time.second, press)
    #data_str = data_str + "]"

    # Disconnect from MySQL server
    cnx.close()

    # Assign data from mailbox
    id = row[0]
    status = row[1]
    owner = row[2]
    shipment_no = row[3] 
    first_name = row[4]
    last_name = row[5]
    street = row[6]
    street_no = row[7]
    postcode = row[8]
    city = row[9]
    country = row[10] 
    assign_ts = row[11]

    # Create parsing object
    mailbox = forms.initMailbox(id, status, owner, shipment_no, first_name,last_name,street,street_no,postcode,city,country,assign_ts)
    return render_template('index.html', title="Home", mailbox=mailbox)

    # How to use CosmosDB - Microsoft Azure
    #client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'mainKey': config_cosmos.COSMOSDB_KEY})
    ## Read databases and take first since id should not be duplicated.
    #db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))
    ## Read collections and take first since id should not be duplicated.
    #coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config_cosmos.COSMOSDB_COLLECTION))
    ## Read documents and take first since id should not be duplicated.
    #doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == config_cosmos.COSMOSDB_DOCUMENT))
    ## Create a model to pass to results.html
    #class VoteObject:
    #    choices = dict()
    #    total_votes = 0
    #vote_object = VoteObject()
    #vote_object.choices = {
    #    "Web Site" : doc['Web Site'],
    #    "Cloud Service" : doc['Cloud Service'],
    #    "Virtual Machine" : doc['Virtual Machine']
    #}
    #vote_object.total_votes = sum(vote_object.choices.values())
    ## Hack to avoid zero detection in empty database
    #if vote_object.total_votes == 0:
    #    vote_object.total_votes = 1


    #return render_template(
    #    'results.html',
    #    title='Some charties',
    #    year=datetime.now().year,
    #    result = result
    #)

@app.route('/list')
def list():
    return render_template('list.html', title="List")

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/help')
def help():
    """Renders the about page."""
    return render_template(
        'help.html',
        title='Help',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/profile')
def profile():
    """Renders the about page."""
    return render_template(
        'profile.html',
        title='Profile',
        year=datetime.now().year,
        message='Your profile.'
    )

@app.route('/clear')
def clear():
    #"""Renders the contact page."""
    #client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'mainKey': config_cosmos.COSMOSDB_KEY})
    ## Attempt to delete the database.  This allows this to be used to recreate as well as create
    #try:
    #    db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))
    #    client.DeleteDatabase(db['_self'])
    #except:
    #    pass
    ## Create database
    #db = client.CreateDatabase({ 'id': config_cosmos.COSMOSDB_DATABASE })
    ## Create collection
    #collection = client.CreateCollection(db['_self'],{ 'id': config_cosmos.COSMOSDB_COLLECTION })
    ## Create document
    #document = client.CreateDocument(collection['_self'],
    #    { 'id': config_cosmos.COSMOSDB_DOCUMENT,
    #      'Web Site': 0,
    #      'Cloud Service': 0,
    #      'Virtual Machine': 0,
    #      'name': config_cosmos.COSMOSDB_DOCUMENT 
    #    })

    return render_template(
       'clear.html',
        title='Clear',
        year=datetime.now().year
    )

@app.route('/create', methods=['GET', 'POST'])
def create(): 
    if form.validate_on_submit(): # is user submitted vote  
        #client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'mainKey': config_cosmos.COSMOSDB_KEY})
        ## Read databases and take first since id should not be duplicated.
        #db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))
        ## Read collections and take first since id should not be duplicated.
        #coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config_cosmos.COSMOSDB_COLLECTION))
        ## Read documents and take first since id should not be duplicated.
        #doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == config_cosmos.COSMOSDB_DOCUMENT))
        ## Take the data from the deploy_preference and increment our database
        #doc[form.deploy_preference.data] = doc[form.deploy_preference.data] + 1
        #replaced_document = client.ReplaceDocument(doc['_self'], doc)
        ## Create a model to pass to results.html
        #class VoteObject:
        #    choices = dict()
        #    total_votes = 0
        #vote_object = VoteObject()
        #vote_object.choices = {
        #    "Web Site" : doc['Web Site'],
        #    "Cloud Service" : doc['Cloud Service'],
        #    "Virtual Machine" : doc['Virtual Machine']
        #}
        #vote_object.total_votes = sum(vote_object.choices.values())

        result = CleanTable(0,0,0,0,0)

        return render_template(
            'results.html', 
            year=datetime.now().year, 
            result = result
        )

    else :
        return render_template(
            'create.html', 
            title = 'Create',
            year=datetime.now().year
        )
