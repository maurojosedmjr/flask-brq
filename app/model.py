from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_db(app):
    db.init_app(app)
    app.db = db


class Residencias(db.Model):
    id_residencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(150))
    host_id = db.Column(db.Integer)
    host_name = db.Column(db.String(150))
    neighbourhood = db.Column(db.String(150))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    room_type = db.Column(db.String(150))
    price = db.Column(db.Float)
    minimum_nights = db.Column(db.Integer)
    number_of_reviews = db.Column(db.Integer)
    last_review = db.Column(db.String(10))
    reviews_per_month = db.Column(db.Float)
    calculated_host_listings_count = db.Column(db.Integer)
    availability_365 = db.Column(db.Integer)
    neighbourhood_group = db.Column(db.String(150))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "host_id": self.host_id,
            "host_name": self.host_name,
            "neighbourhood_group": self.neighbourhood_group,
            "neighbourhood": self.neighbourhood,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "room_type": self.room_type,
            "price": self.price,
            "minimum_nights": self.minimum_nights,
            "number_of_reviews": self.number_of_reviews,
            "last_review": self.last_review,
            "reviews_per_month": self.reviews_per_month,
            "calculated_host_listings_count": self.calculated_host_listings_count,
            "availability_365": self.availability_365,
        }
