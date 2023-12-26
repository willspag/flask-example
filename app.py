from flask import Flask, redirect, render_template, flash, request, jsonify, session, request, url_for, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import os

# Load environment variables
from dotenv import load_dotenv



load_dotenv()



app = Flask(__name__, static_url_path='', static_folder='frontend', template_folder="frontend/html")

app.secret_key = os.environ.get("FLASK_SECRET_KEY")



###############################################################################
###############################################################################
'''                               Flask Forms                               '''
###############################################################################
###############################################################################

class ExampleForm(FlaskForm):
    text_area_input = TextAreaField('Example Input Field')
    submit = SubmitField('Submit')


###############################################################################
###############################################################################
'''                                  Routes                                 '''
###############################################################################
###############################################################################

@app.route('/', methods=['GET', 'POST'])
def pub_med_search_chat():
    
    example_form = ExampleForm()
    
    if example_form.validate_on_submit():
        user_input = example_form.text_area_input.data
        
        example_response = "Submission Received! Here is the text you provided in the form: " + str(user_input)
        
        # Add Markdown Capabilities
        return render_template('index.html', example_form=example_form, example_response = example_response)
    return render_template('index.html', example_form=example_form, example_response = "")


if __name__ == "__main__":
    
    # Automatically set the debug mode based on the environment variable
    if os.environ.get("PRODUCTION_MODE_TRUE_OR_FALSE", "TRUE").upper() == "TRUE":
        debug = False
    else:
        debug = True
    app.run(
        debug = debug,
        host = os.environ.get("FLASK_HOST", "0.0.0.0"),
        port = int(os.environ.get("FLASK_PORT", 8080))
    )
    
