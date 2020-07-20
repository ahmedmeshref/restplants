from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    Migrate(app, db)


class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    scientific_name = db.Column(db.String(), nullable=False)
    is_poisonous = db.Column(db.Boolean, nullable=False)
    primary_color = db.Column(db.String(), nullable=False)

    def __int__(self, name, scientific_name, is_poisonous, primary_color):
        self.name = name
        self.scientific_name = scientific_name
        self.is_poisonous = is_poisonous
        self.primary_color = primary_color

    def __repr__(self):
        return f"<Plant id: {self.id}, name: {self.name}>"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'is_poisonous': self.is_poisonous,
            'primary_color': self.primary_color
        }

    @staticmethod
    def get_plant_or_404(plant_id):
        return db.session.query(Plant).get_or_404(plant_id)

    @staticmethod
    def gey_plants_by_name(name):
        return db.session.query(Plant).filter(Plant.name.ilike(f'%{name}%')).all()
