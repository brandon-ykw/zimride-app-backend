from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ride(db.Model):
    __tablename__ = 'ride'
    id = db.Column(db.Integer, primary_key=True)
    
    departure_location = db.Column(db.String, nullable=False)
    departure_year= db.Column(db.Integer, nullable=False)
    departure_month = db.Column(db.Integer, nullable=False)
    departure_day = db.Column(db.Integer, nullable=False)

    departure_hour = db.Column(db.Integer, nullable=False)
    departure_minute = db.Column(db.Integer, nullable=False)

    arrival_location = db.Column(db.String, nullable=False)
    return_year= db.Column(db.Integer, nullable=True)
    return_month = db.Column(db.Integer, nullable=True)
    return_day = db.Column(db.Integer, nullable=True)

    return_hour = db.Column(db.Integer, nullable=True)
    return_minute = db.Column(db.Integer, nullable=True)
    
    seats_total = db.Column(db.Integer, nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cash = db.Column(db.Boolean, default=True, nullable=False)
    notes = db.Column(db.String, nullable=True)

    #driver = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    
    def __init__(self, **kwargs):
        self.departure_location = kwargs.get('departure_location')
        self.departure_year = kwargs.get('departure_year')
        self.departure_month = kwargs.get('departure_month')
        self.departure_day = kwargs.get('departure_day')

        self.departure_hour = kwargs.get('departure_hour')
        self.departure_minute = kwargs.get('departure_minute')

        self.arrival_location = kwargs.get('arrival_location')
        self.return_year = kwargs.get('return_year')
        self.return_month = kwargs.get('return_month')
        self.return_day = kwargs.get('return_day')

        self.return_hour = kwargs.get('return_hour')
        self.return_minute = kwargs.get('return_minute')

        self.seats_total = kwargs.get('seats_total')
        self.seats_available = kwargs.get('seats_available')
        self.price = kwargs.get('price')
        self.cash = kwargs.get('cash')
        self.notes = kwargs.get('notes')
        #self.driver = kwargs.get('driver')
    
    def serialize(self):
        return{
            'id': self.id,

            'departure_location': self.departure_location,
            'departure_year': self.departure_year,
            'departure_month': self.departure_month,
            'departure_day': self.departure_day,

            'departure_hour': self.departure_hour,
            'departure_minute': self.departure_minute,
            'arrival_location': self.arrival_location,
            'return_year': self.return_year,
            'return_month': self.return_month,
            'return_day': self.return_day,

            'return_hour': self.return_hour,
            'return_minute': self.return_minute,

            'seats_total': self.seats_total,
            'seats_available': self.seats_available,
            'price': self.price,
            'cash': self.cash,
            'notes': self.notes
            #'driver': self.driver
        }
    
    """seat = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.String, nullable=False)
    username = db.Column(db.String,nullable=False)"""

    """def __init__(self, **kwargs):
        self.seat = kwargs.get('seat', '')
        self.price = kwargs.get('price', '')
        self.payment = kwargs.get('payment', '')
        self.username = kwargs.get('username', '')"""
    
    """def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'seat': self.seat,
            'price': self.price,
            'payment': self.payment
        }"""
