from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserRegistrationTestCase(TestCase):
    """Test cases for user registration process"""
    
    def setUp(self):
        """Set up test client and test data"""
        self.client = Client()
        self.register_url = reverse('register')
        self.valid_user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123'
        }
    
    def test_registration_page_loads(self):
        """Test that registration page loads successfully"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_successful_registration(self):
        """Test successful user registration"""
        response = self.client.post(self.register_url, self.valid_user_data)
        
        # Check user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        
        # Check password is hashed correctly
        self.assertTrue(user.check_password('testpass123'))
        
        # Check response
        self.assertEqual(response.status_code, 200)
    
    def test_registration_with_missing_fields(self):
        """Test registration fails when required fields are missing"""
        # Missing username
        data = self.valid_user_data.copy()
        data['username'] = ''
        response = self.client.post(self.register_url, data)
        self.assertContains(response, 'All fields are required')
        self.assertFalse(User.objects.filter(email='testuser@example.com').exists())
        
        # Missing email
        data = self.valid_user_data.copy()
        data['email'] = ''
        response = self.client.post(self.register_url, data)
        self.assertContains(response, 'All fields are required')
        
        # Missing password
        data = self.valid_user_data.copy()
        data['password'] = ''
        response = self.client.post(self.register_url, data)
        self.assertContains(response, 'All fields are required')
    
    def test_registration_with_mismatched_passwords(self):
        """Test registration fails when passwords don't match"""
        data = self.valid_user_data.copy()
        data['password_confirm'] = 'differentpassword'
        response = self.client.post(self.register_url, data)
        
        self.assertContains(response, 'Passwords do not match')
        self.assertFalse(User.objects.filter(username='testuser').exists())
    
    def test_registration_with_duplicate_username(self):
        """Test registration fails when username already exists"""
        # Create a user first
        User.objects.create_user(
            username='testuser',
            email='existing@example.com',
            password='password123'
        )
        
        # Try to register with same username
        response = self.client.post(self.register_url, self.valid_user_data)
        self.assertContains(response, 'Username already exists')
        
        # Ensure only one user exists with this username
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)
    
    def test_registration_with_duplicate_email(self):
        """Test registration fails when email is already registered"""
        # Create a user first
        User.objects.create_user(
            username='existinguser',
            email='testuser@example.com',
            password='password123'
        )
        
        # Try to register with same email
        response = self.client.post(self.register_url, self.valid_user_data)
        self.assertContains(response, 'Email already registered')
        
        # Ensure user with testuser username was not created
        self.assertFalse(User.objects.filter(username='testuser').exists())
    
    def test_user_logged_in_after_registration(self):
        """Test that user is automatically logged in after successful registration"""
        response = self.client.post(self.register_url, self.valid_user_data)
        
        # Check user is authenticated
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)
        
        # Check session contains user
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.id)
    
    def test_registration_with_invalid_email_format(self):
        """Test registration with invalid email format"""
        data = self.valid_user_data.copy()
        data['email'] = 'invalidemail'
        
        # This test depends on whether you have email validation in the view
        # Currently the view doesn't validate email format
        # You may want to add this validation
        response = self.client.post(self.register_url, data)
        # This will currently pass, but ideally should fail
    
    def test_registration_with_weak_password(self):
        """Test registration with weak password"""
        data = self.valid_user_data.copy()
        data['password'] = '123'
        data['password_confirm'] = '123'
        
        # This test depends on password strength validation
        # Currently the view doesn't validate password strength
        # You may want to add this validation
        response = self.client.post(self.register_url, data)
        # This will currently pass, but ideally should enforce strong passwords
    
    def test_get_request_returns_empty_form(self):
        """Test GET request returns registration form without errors"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'error')
    
    def tearDown(self):
        """Clean up after tests"""
        User.objects.all().delete()
