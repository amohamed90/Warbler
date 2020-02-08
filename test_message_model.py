import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, Follows, bcrypt
from datetime import datetime

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
from app import app


db.create_all()


class MessageModelTestCase(TestCase):
    """Test views for messages"""

    def setUp(self):

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

        user1 = User.signup(
            email="alaa@alaa.com",
            username="amohamed",
            password='PASSWORD',
            image_url=None
        )

        user1.id = 1

        db.session.add(user1)
        db.session.commit()

        user_message = Message(id=1, text='Hello World', user_id=user1.id, timestamp=datetime.utcnow())

        db.session.add(user_message)
        db.session.commit()


    def test_message_model(self):
        """Testing if message has been added successfully"""

        self.assertEqual(Message.query.count(), 1)

    def test_message(self):
        """Testing to check if the message that it related to the user is correct."""

        test_query = Message.query.get_or_404(1)

        self.assertEqual(test_query.text, 'Hello World')
        self.assertNotEqual(test_query.text, 'Hellooo Wooorld')

    def test_time_of_message_submission(self):
        """Testing to check if the message submission time is correct"""

        test_query = Message.query.get_or_404(1)

        self.assertTrue(test_query.timestamp)

    def test_user_id(self):
        """Testing to check if the message belongs to the right user"""

        test_query = Message.query.get_or_404(1)

        self.assertEqual(test_query.user_id, 1)
        self.assertNotEqual(test_query.user_id, 2)