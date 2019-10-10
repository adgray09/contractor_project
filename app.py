from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
chips = db.chips

app = Flask(__name__)

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
    print(request.form.to_dict())
    return redirect(url_for('chips_index'))

if __name__ == '__main__':
    app.run(debug=True)