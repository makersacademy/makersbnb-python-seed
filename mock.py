


#this is a get route
'''
tesitng stuff
'''

@app.route('/listings')
def get_listings():
    return render_template('listings.html')