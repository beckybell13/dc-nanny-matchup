import os
import logging
import json
import datetime
import random
from flask import render_template, jsonify, request

from server import app, db_session, base_dir
from server.models.listing import Listing, AgeGroups, TimeFrame

logger = logging.getLogger(__name__)

# show map on index
@app.route('/', methods=['GET'])
def index():

    # TODO: render map

    # will need to grab whatever data we need from the Database
    #   to render the map
    # data=json.dumps(str(current_user))

    # viz_types = map(lambda x: x.name, list(VizType))
    return render_template('index.html')


@app.route('/listing', methods=['GET', 'POST'])
def listing():

    # if param has form submit or whatever, create new listing in database:
    # TODO: grab data from form entries
    # new_listing = Listing(....)
    # db_session.add(new_listing)
    # db_session.commit()
    return render_template('listing.html')



# def save_viz_response(request):
#     # Retrieve responses
#     theme1 = request.form['theme1']
#     theme1_word1 = request.form['theme1_word1']
#     theme1_word2 = request.form['theme1_word2']
#     theme1_word3 = request.form['theme1_word3']
#     theme2 = request.form['theme2']
#     theme2_word1 = request.form['theme2_word1']
#     theme2_word2 = request.form['theme2_word2']
#     theme2_word3 = request.form['theme2_word3']
#     # info = json.loads(request.form['info'])
#     viz_type = request.form['viz_type']
#     current_user_id = request.form['user_id']
#     start_time = request.form['start_time']
#     end_time = str(datetime.datetime.now())
#
#     # Add to database
#     current_user = db_session.query(User).filter(User.id == current_user_id).first()
#     user_response = Response(theme1=theme1, theme1_word1=theme1_word1, theme1_word2=theme1_word2, theme1_word3=theme1_word3,
#                              theme2=theme2, theme2_word1=theme2_word1, theme2_word2=theme2_word2, theme2_word3=theme2_word3,
#                              viz_type=viz_type, start_time=start_time, end_time=end_time)
#
#     current_user.responses.append(user_response)
#     db_session.commit()
