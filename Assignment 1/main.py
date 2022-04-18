#!/bin/python3

import json
import turtle
import urllib.request
import time

#api
PeopleUrl = 'http://api.open-notify.org/astros.json'

#calling the api
response = urllib.request.urlopen(PeopleUrl)

#Transform JSON to python data
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for i in people:
    print(i['name'], 'in', i['craft'])

LatLongUrl = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(LatLongUrl)
result = json.loads(response.read())
location = result['iss_position']
lat = float(location['latitude'])
long = float(location['longitude'])

print('Latitude :', lat, '\nLongitude: ', long)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)
iss.penup()
iss.goto(long, lat)

lat = 49.8951
long = -97.1384
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(long,lat)
location.dot(5)
location.hideturtle()

placeUrl = 'http://api.open-notify.org/iss-pass.json'
placeUrl = placeUrl + '?lat=' + str(lat) + '&lon=' +str(long)
response = urllib.request.urlopen(placeUrl)
result = json.loads(response.read())

overhead = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(overhead), style)


screen.exitonclick()
