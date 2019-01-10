import json
from db import db, Ride
from flask import Flask, request
from datetime import date

db_filename = "rides.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
  db.create_all()

@app.route('/')
@app.route('/api/rides/')
def get_rides():
  """Returns all rides"""
  rides = Ride.query.all()
  res = {'success': True, 'data': [ride.serialize() for ride in rides]}
  return json.dumps(res), 200

@app.route('/api/rides/', methods = ['POST'])
def create_ride():
  """Create a new ride"""
  body = json.loads(request.data)
  ride = Ride(
    departure_location=body.get('departure_location'),
    departure_year=body.get('departure_year'),
    departure_month=body.get('departure_month'),
    departure_day=body.get('departure_day'),
    departure_hour=body.get('departure_hour'),
    departure_minute=body.get('departure_minute'),
    arrival_location=body.get('arrival_location'),
    return_year=body.get('return_year'),
    return_month=body.get('return_month'),
    return_day=body.get('return_day'),
    return_hour=body.get('return_hour'),
    return_minute=body.get('return_minute'),
    seats_total=body.get('seats_total'),
    seats_available=body.get('seats_available'),
    price=body.get('price'),
    cash=body.get('cash'),
    notes=body.get('notes')
  )
  db.session.add(ride)
  db.session.commit()
  return json.dumps({'success': True, 'data': ride.serialize()}), 201


@app.route('/api/ride/search/', methods = ['POST'])
def search_ride():
  """Get a specified ride"""

  body = json.loads(request.data)
  deploc=body.get('departure_location')
  depyear=body.get('departure_year')
  depmonth=body.get('departure_month')
  depday=body.get('departure_day')
  arrloc=body.get('arrival_location')
  
  retyear=body.get('return_year')
  retmonth=body.get('return_month')
  retday=body.get('return_day')

  if retday is None:  
    rides = Ride.query.filter_by(departure_location=deploc, arrival_location=arrloc, 
      departure_day=depday, departure_month=depmonth, departure_year=depyear, return_year=None).all()
  else:
    rides = Ride.query.filter_by(departure_location=deploc, arrival_location=arrloc, 
      departure_day=depday, departure_month=depmonth, departure_year=depyear,
      return_day=retday, return_month=retmonth, return_year=retyear).all() 
  if rides is not None:
    return json.dumps({'success': True, 'data': [ride.serialize() for ride in rides]}), 200    
  return json.dumps({'success': False, 'error': 'Ride not found!'}), 404


@app.route('/api/ride/<int:ride_id>/', methods = ['POST'])
def edit_ride(ride_id):
  """Edit specificties of a specified ride"""
  ride = Ride.query.filter_by(id=ride_id).first()
  if ride is not None:
    body = json.loads(request.data)
    ride.seat = body.get('seat', ride.seat)
    ride.price = body.get('price', ride.price)
    ride.payment = body.get('payment', ride.payment)
    db.session.commit()
    return json.dumps({'success': True, 'data': ride.serialize()}), 200    
  return json.dumps({'success': False, 'error': 'Ride not found!'}), 404
  

@app.route('/api/ride/<int:ride_id>/', methods = ['GET'])
def take_ride(ride_id):
  """Edit specificities of a specified ride"""
  ride = Ride.query.filter_by(id=ride_id).first()
  if ride is not None and ride.seats_available > 0:
    ride.seats_available -= 1
    db.session.commit()
    return json.dumps({'success': True, 'data': ride.serialize()}), 200    
  if ride is not None and ride.seats_available <= 0:
    return json.dumps({'success': False, 'error': 'No more rides!'}), 404

  return json.dumps({'success': False, 'error': 'Ride not found!'}), 404

@app.route('/api/rides/', methods = ['DELETE'])
def delete_ride():
  """Delete rides with preceding dates"""
  today = date.today()
  year = today.year
  month = today.month
  day = today.day

  all_rides = []

  rides_year = Ride.query.filter(Ride.departure_year < year).all()
  if rides_year is not None:
    for ride in rides_year:
      db.session.delete(ride)
      all_rides.append(ride.serialize())
    db.session.commit()
  
  rides_month = Ride.query.filter(Ride.departure_month < month, Ride.departure_year == year).all()
  if rides_month is not None:
    for ride in rides_month:
      db.session.delete(ride)
      all_rides.append(ride.serialize())
    db.session.commit()

  rides_day = Ride.query.filter(Ride.departure_day < day, Ride.departure_month == month, Ride.departure_year == year).all()
  if rides_day is not None:
    for ride in rides_day:
      db.session.delete(ride)
      all_rides.append(ride.serialize())
    db.session.commit()
  
  if all_rides == []:
    return json.dumps({'success': False, 'error': 'Ride not found!'}), 404
  return json.dumps({'success': True, 'data': all_rides}), 200  

  
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5000, debug = True)