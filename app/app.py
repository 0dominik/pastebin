import os
import sys
from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Establish MongoDB connection
try:
    # Attempt to connect to MongoDB using the MONGO_URI environment variable or default to localhost
    client = MongoClient(os.environ.get('MONGO_URI', 'mongodb://mongodb:27017/'), serverSelectionTimeoutMS=5000)
    client.server_info()  # Verify connection by requesting server info
    db = client.db
    app.logger.info("Successfully connected to MongoDB")
except Exception as e:
    app.logger.error(f"Failed to connect to MongoDB: {e}")
    sys.exit(1)  # Exit the application if MongoDB connection fails

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        title = request.form.get('title', 'Untitled')
        content = request.form.get('content')
        author = request.form.get('author', 'Anonymous')
        date = datetime.now().strftime("%d-%m-%Y")
        
        # Create a base unique ID for the paste
        base_unique_id = f"{title.lower().replace(' ', '-')}-{date}"
        
        # Ensure unique ID is truly unique by appending a counter if necessary
        counter = 0
        while True:
            unique_id = f"{base_unique_id}-{counter}" if counter > 0 else base_unique_id
            existing_paste = db.pastes.find_one({'unique_id': unique_id})
            if not existing_paste:
                break
            counter += 1

        try:
            # Insert the new paste into the database
            db.pastes.insert_one({
                'title': title,
                'content': content,
                'author': author,
                'date': date,
                'unique_id': unique_id
            })
            app.logger.info(f"Successfully created paste with ID: {unique_id}")
        except Exception as e:
            app.logger.error(f"Failed to create paste: {e}")
            return "Error creating paste", 500

        # Redirect to the view page for the new paste
        return redirect(url_for('view_paste', unique_id=unique_id))

    # If it's a GET request, render the main page
    return render_template('index.html')

@app.route('/<unique_id>')
def view_paste(unique_id):
    try:
        # Attempt to retrieve the paste from the database
        paste = db.pastes.find_one({'unique_id': unique_id})
        if paste:
            return render_template('view_paste.html', paste=paste)
        else:
            app.logger.warning(f"Paste not found: {unique_id}")
            return "Paste not found", 404
    except Exception as e:
        app.logger.error(f"Error retrieving paste {unique_id}: {e}")
        return "Error retrieving paste", 500

if __name__ == '__main__':
    # Run the Flask app, with debug mode controlled by an environment variable
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', 'False') == 'True')
