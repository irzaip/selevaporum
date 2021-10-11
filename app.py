import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import data_upload, wacs
#, metadata, data_visualize, redundant, inference # import your pages here

# Create an instance of the app 
app = MultiPage()


# Add all your applications (pages) here
app.add_page("Upload Data", data_upload.app)
app.add_page("WhatsApp CS", wacs.app)
#app.add_page("Machine Learning", machine_learning.app)
#app.add_page("Data Analysis",data_visualize.app)
#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()