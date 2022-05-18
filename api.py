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

app.run()
