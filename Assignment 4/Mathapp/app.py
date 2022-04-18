from re import match
from typing import Any
from flask import Flask, render_template, request
from flask.json.tag import JSONTag

from MyMath import MyMath

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', max=0, avg=0, stddev=0 )

@app.route('/', methods=['POST'])
def my_form_post():
    numbers = request.form['numbers']
    if not bool(numbers):
      numbers = '0,0,0'

    numlist = list (map(int, numbers.split(',') ))

    math = MyMath()
    math.num_list = numlist

    return render_template('index.html', max=math.max_number(), avg=math.cal_average(), stddev=math.standard_Deviation() )


if __name__ == '__main__':
  app.run( host='0.0.0.0', port=80)
