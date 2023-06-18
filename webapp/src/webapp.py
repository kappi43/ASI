import os
import pickle
import numpy as np

from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect


model_name = os.environ['MODEL_NAME']
model = pickle.load(open(model_name, 'rb'))
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    params = None
    result = ""
    if request.method == 'POST':
        params = request.form

        booking_date = params.get('booking_date')
        arrival_date = params.get('arrival_date')
        book_date = datetime.strptime(booking_date, '%Y-%m-%d')
        arr_date = datetime.strptime(arrival_date, '%Y-%m-%d')

        adults = params.get('adults')
        children = params.get('children')
        wknd_nights = params.get('wknd_nights')
        wk_nights = params.get('wk_nights')
        parking_space = 1 if 'parking' in params.keys() else 0
        lead_time = (arr_date - book_date).days
        arrival_year = arr_date.year
        arrival_month = arr_date.month
        arrival_day = arr_date.day
        repeated_guest = 1 if 'repeated' in params.keys() else 0
        prev_cancel = params.get('prev_cancel')
        not_cancelled = params.get('not_cancelled')
        avg_room_price = params.get('avg_room_price')
        spec_req = params.get('spec_req')
        meal_plan = 0
        room_type = 0
        market_segment = 0

        print(params)

        in_array = np.array([adults, children, wknd_nights, wk_nights,
                             parking_space, lead_time, arrival_year, arrival_month,
                             arrival_day, repeated_guest, prev_cancel, not_cancelled,
                             avg_room_price, spec_req, meal_plan, room_type, market_segment])
        in_array = in_array.reshape(1, -1)
        result = model.predict(in_array)
        print(result)
    return render_template('index.html', params=params, result=result)

