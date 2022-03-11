# python -m pytest --cov --cov-report term-missing

from flask_testing import TestCase
from werkzeug.wrappers import response
from application import app, db
from application.models import Engine, Car
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False  
        )
        return app
    
    def setUp(self):
        # Create table schema
        db.drop_all()
        db.create_all()

        # Create test Engine
        vroom = Engine(
                style = 'gibberish',
                cc = '11',
                power = '22'
        )
        # Create test Car
        boom = Car(
                engine_id = '1',
                make = 'Ford',
                model = 'Focus',
                registration = 'JACK'
        )

        # Add test objects to database
        db.session.add(vroom)
        db.session.add(boom)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_get_index(self):
        # Checking objects have been added to test database and displayed on home page
        response = self.client.get(url_for('index'))
        self.assert200
        self.assertIn(b'gibberish', response.data)
        self.assertIn(b'Ford', response.data)

class TestEntry(TestBase):
    def test_engine_page(self):
        # Check add_engine page is displayed
        response = self.client.get(url_for('add_engine'))
        self.assert200
        self.assertIn(b'Engine', response.data)
    
    def test_post_engine(self):
        # Testing functionality of add_engine page
        response = self.client.post(
            url_for('add_engine'),
            data = dict(
                style = 'v6',
                cc = '44',
                power = '55'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertIn(b'v6', response.data)
    
    def test_update_engine(self):
        # Testing functionality of update_engine page
        response = self.client.post(
            url_for('update_engine', id=1),
            data = dict(
                style = 'v8',
                cc = '999',
                power = '888'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertIn(b'v8', response.data)

    def test_car_page(self):
        # Check add_car page is displayed
        response = self.client.get(url_for('add_car'))
        self.assert200
        self.assertIn(b'Car', response.data)

    def test_post_car(self):
        # Testing functionality of add_car page
        response = self.client.post(
            url_for('add_car'),
            data = dict(
                engine_id = '1',
                make = 'ferrari',
                model = '360',
                registration = '360x'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertIn(b'ferrari', response.data)

    def test_update_car(self):
        # Testing functionality of update_car page
        response = self.client.post(
            url_for('update_car', id=1),
            data = dict(
                engine_id = '1',
                make = 'audi',
                model = 's5',
                registration = 's5x'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertIn(b'audi', response.data)

    def test_delete_engine(self):
        # Testing delete function for engine database
        response = self.client.post(
            url_for('delete'),
            data = dict(
                id = '1',
                question = 'engine'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertNotIn(b'gibberish', response.data)

    def test_delete_car(self):
        # Testing delete function for car database
        response = self.client.post(
            url_for('delete'),
            data = dict(
                id = '1',
                question = 'car'
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertNotIn(b'Ford', response.data)
    
  

    

    