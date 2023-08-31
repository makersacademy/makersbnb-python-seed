import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.properties import Properties
from lib.properties_repository import *




# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index


    # dic = property_repo.all()
    connection = get_flask_database_connection(app)
    property_repo = PropertiesRepository(connection)
    properties = property_repo.all()
    response = ""
    for property in properties:
        response += f"{properties}\n"
    return response
        
    
    
    # for x in property_repo.all()
    # return '''
    #     <html>
    #         <head>
    #             <title>Home Page</title>
    #         </head>
    #         <body>
    #             <h1>Hello, your sum is ''' + x[0][1] + '''!</h1>
    #         </body>
    #     </html>'''


    # return render_template('index.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


