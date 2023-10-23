import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# individual page
@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    space = {
        'name': 'Test space', 
        'description': 'Mauris tortor enim, consequat eu faucibus vitae, imperdiet at purus. Nunc non eros non est egestas sollicitudin eget vel quam.',
        'size': '71.2 sq. m.'
        }
    
    return render_template('space.html', space=space)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
