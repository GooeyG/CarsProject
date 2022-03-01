import unittest

from flask import abort, url_for
from application import app, db
from application.models import Car, Engine
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="sasda",
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )

    def setUp(self):
        db.drop_all()
        db.create_all()
        engine1 = Engine('A', '1', '1')
        engine2 = Engine('B', '2', '2')
        car1 = Car('1', 'A', 'A', 'A')
        car2 = Car('2', 'B', 'B', 'B')
        db.session.add(engine1)
        db.session.add(engine2)
        db.session.add(car1)
        db.session.add(car2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestPostResponse(TestBase):
    
    def test_add_engine(self):
        #tests that an engine is created with the correct attributes for the object
        response = self.client.post('/add/engine',
        data = {'style' : 'v6', 'cc' : '3200', 'power' : '350'})

        self.assertIn(b'v6', response.data)
        