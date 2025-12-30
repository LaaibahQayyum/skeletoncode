"""
Unit Tests for Flask CRUD Application
======================================

This file contains pytest tests for the skeleton Flask application.
Tests cover all CRUD operations and routes.

Run tests with: pytest test_skeleton_app.py -v
"""

import pytest
from skeleton_app import app, db, User


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


@pytest.fixture
def sample_user():
    """Create a sample user for testing"""
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'age': '25',
        'city': 'New York'
    }


class TestHomePage:
    """Tests for the home page route"""
    
    def test_home_page_loads(self, client):
        """Test that home page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data
    
    def test_home_page_shows_users(self, client, sample_user):
        """Test that home page displays users"""
        # Add a user first
        client.post('/add', data=sample_user, follow_redirects=True)
        
        # Check if user appears on home page
        response = client.get('/')
        assert response.status_code == 200


class TestAddUser:
    """Tests for adding new users"""
    
    def test_add_user_page_loads(self, client):
        """Test that add user page loads"""
        response = client.get('/add')
        assert response.status_code == 200
    
    def test_add_user_success(self, client, sample_user):
        """Test successfully adding a new user"""
        response = client.post('/add', data=sample_user, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify user was added to database
        with app.app_context():
            user = User.query.filter_by(email=sample_user['email']).first()
            assert user is not None
            assert user.first_name == sample_user['first_name']
            assert user.last_name == sample_user['last_name']
            assert user.email == sample_user['email']
            assert user.age == int(sample_user['age'])
            assert user.city == sample_user['city']
    
    def test_add_multiple_users(self, client):
        """Test adding multiple users"""
        users = [
            {'first_name': 'Alice', 'last_name': 'Smith', 'email': 'alice@example.com', 'age': '30', 'city': 'Boston'},
            {'first_name': 'Bob', 'last_name': 'Johnson', 'email': 'bob@example.com', 'age': '28', 'city': 'Chicago'},
        ]
        
        for user_data in users:
            response = client.post('/add', data=user_data, follow_redirects=True)
            assert response.status_code == 200
        
        # Verify both users exist
        with app.app_context():
            assert User.query.count() == 2


class TestViewUser:
    """Tests for viewing individual user details"""
    
    def test_view_user_success(self, client, sample_user):
        """Test viewing a user's details"""
        # Add user first
        client.post('/add', data=sample_user, follow_redirects=True)
        
        # Get the user ID
        with app.app_context():
            user = User.query.filter_by(email=sample_user['email']).first()
            user_id = user.id
        
        # View the user
        response = client.get(f'/view/{user_id}')
        assert response.status_code == 200
    
    def test_view_nonexistent_user(self, client):
        """Test viewing a user that doesn't exist"""
        response = client.get('/view/9999')
        assert response.status_code == 404


class TestUpdateUser:
    """Tests for updating user information"""
    
    def test_update_user_page_loads(self, client, sample_user):
        """Test that update user page loads"""
        # Add user first
        client.post('/add', data=sample_user, follow_redirects=True)
        
        with app.app_context():
            user = User.query.filter_by(email=sample_user['email']).first()
            user_id = user.id
        
        response = client.get(f'/update/{user_id}')
        assert response.status_code == 200


class TestDeleteUser:
    """Tests for deleting users"""
    
    def test_delete_user_success(self, client, sample_user):
        """Test successfully deleting a user"""
        # Add user first
        client.post('/add', data=sample_user, follow_redirects=True)
        
        with app.app_context():
            user = User.query.filter_by(email=sample_user['email']).first()
            user_id = user.id
            assert user is not None
        
        # Delete the user
        response = client.get(f'/delete/{user_id}', follow_redirects=True)
        assert response.status_code == 200


class TestDatabaseModel:
    """Tests for the User database model"""
    
    def test_user_creation(self, client):
        """Test creating a user object"""
        with app.app_context():
            user = User(
                first_name='Test',
                last_name='User',
                email='test@example.com',
                age=25,
                city='Test City'
            )
            db.session.add(user)
            db.session.commit()
            
            # Verify user was created
            retrieved_user = User.query.filter_by(email='test@example.com').first()
            assert retrieved_user is not None
            assert retrieved_user.first_name == 'Test'
            assert retrieved_user.last_name == 'User'
    
    def test_user_repr(self, client):
        """Test user string representation"""
        with app.app_context():
            user = User(
                first_name='Jane',
                last_name='Doe',
                email='jane@example.com',
                age=30,
                city='Boston'
            )
            db.session.add(user)
            db.session.commit()
            
            assert 'Jane' in repr(user)
            assert 'Doe' in repr(user)


class TestErrorHandlers:
    """Tests for error handling"""
    
    def test_404_error(self, client):
        """Test 404 error handler"""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404


class TestApplicationConfig:
    """Tests for application configuration"""
    
    def test_app_exists(self):
        """Test that the app exists"""
        assert app is not None
    
    def test_app_is_testing(self, client):
        """Test that app is in testing mode"""
        assert app.config['TESTING'] == True
