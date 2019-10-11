from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os 

host = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.Contractor
chips = db.chips

app = Flask(__name__)

@app.route('/chip/<chips_id>')
def chips_show(chips_id):
    """Show a single playlist."""
    chip = chips.find_one({'_id': ObjectId(chips_id)})
    return render_template('chip_item.html', chip=chip)

@app.route('/')
def chips_index():
    """Show all chips."""
    chips_items = chips.find()
    return render_template('chips_index.html', chips_items=chips_items)

@app.route('/chips/new')
def chips_new():
    """Create a new chip."""
    return render_template('chips_new.html')

@app.route('/chips', methods=['POST'])
def chips_submit():
    """Submit a new playlist."""
    added_chip = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'url': request.form.get('url')
    }
    print(added_chip)
    chips.insert_one(added_chip)
    return redirect(url_for('chips_index'))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))