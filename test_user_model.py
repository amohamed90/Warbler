"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase
import forms
from models import db, User, Message, Follows
from sqlalchemy.exc import IntegrityError

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        user1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        user2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD",
        )

        user1.following.append(user2)
        db.session.add_all([user1, user2])
        db.session.commit()

        self.client = app.test_client()
        self.user1 = user1
        self.user2 = user2

    def tearDown(self):
        """Rolls back the database for set up."""

        db.session.rollback()

    def test_user_model(self):
        """Does basic model work?"""

        new_user = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(new_user)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(new_user.messages), 0)
        self.assertEqual(len(new_user.followers), 0)

    def test_repr(self):
        """Test for a repr"""

        self.assertEqual(
            repr(self.user1), f'<User #{self.user1.id}: testuser1, test1@test.com>')

    def test_is_following(self):
        """Test if a user is following or is being followed by another user"""

        self.assertEqual(self.user1.is_following(self.user2), True)
        self.assertEqual(self.user2.is_following(self.user1), False)
        self.assertEqual(self.user1.is_followed_by(self.user2), False)
        self.assertEqual(self.user2.is_followed_by(self.user1), True)

    def test_User_create(self):
        """ Tests if new user created with valid credentials """

        User.query.delete()

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        users = User.query.all()

        self.assertEqual(len(users), 1)

    def test_creating_user_error(self):
        """ Tests if no new user created with invalid credentials """

        with self.assertRaises(IntegrityError) as raised:
            User.signup("testuser1", "user123@user.com", "PASSWORD", None)
            db.session.commit()
        self.assertIn('duplicate key value violates unique constraint', str(raised.exception))
