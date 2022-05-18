import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
storagevendor = [
    {'id': 0,
     'Vendor': 'DellEMC',
     'Product': 'VMAX'
     },
    {'id': 1,
     'Vendor': 'DellEMC',
     'Product': 'Isilon'
    },
    {'id': 2,
     'Vendor': 'NetApp',
     'Product': 'FAS2012'
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Storage Vendor List</h1>
<p>A prototype API for Storage Vendor.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/storagevendor/all', methods=['GET'])
def api_all():
    return jsonify(storagevendor)

@app.route('/api/v1/resources/storagevendor', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for i in storagevendor:
        if i['id'] == id:
            results.append(i)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
