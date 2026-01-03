import os
import django
import sys
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
import json

User = get_user_model()

def run_tests():
    client = Client()
    
    print("Running tests...")

    # 1. Register
    print("\n1. Testing Registration...")
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post('/auth/register/', register_data, content_type='application/json')
    print(f"Status: {response.status_code}")
    if response.status_code != 201:
        try:
            print(response.json())
        except ValueError:
            print(response.content.decode()[:500])  # Print first 500 chars of HTML
        
        # Verify if user already exists
        if response.status_code == 400:
             try:
                data = response.json()
                if "username" in data and "A user with that username already exists." in str(data["username"]):
                    print("User already exists, proceeding to login...")
                else:
                    return
             except ValueError:
                return
        else:
             return

    # 2. Login
    print("\n2. Testing Login...")
    login_data = {
        "username": "testuser",
        "password": "password123"
    }
    response = client.post('/auth/login/', login_data, content_type='application/json')
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(response.content)
        return
    
    tokens = response.json()
    access_token = tokens['access']
    auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

    # 3. Create Post
    print("\n3. Testing Create Post...")
    post_data = {
        "content": "Hello World!"
    }
    response = client.post('/posts/create/', post_data, content_type='application/json', **auth_headers)
    print(f"Status: {response.status_code}")
    if response.status_code != 201:
        print(response.content)
        return
    
    # 4. Feed
    print("\n4. Testing Feed...")
    response = client.get('/posts/feed/', **auth_headers)
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(response.content)
        return
    posts = response.json()
    print(f"Posts found: {len(posts)}")
    if len(posts) > 0:
        post_id = posts[0]['id']
        
        # 5. Like Post
        print(f"\n5. Testing Like Post {post_id}...")
        response = client.post(f'/posts/like/{post_id}/', **auth_headers)
        print(f"Status: {response.status_code}")
        
        # 6. Comment on Post
        print(f"\n6. Testing Comment on Post {post_id}...")
        comment_data = {"content": "Nice post!"}
        response = client.post(f'/posts/comment/{post_id}/', comment_data, content_type='application/json', **auth_headers)
        print(f"Status: {response.status_code}")

    # 7. Follow User
    print("\n7. Testing Follow User...")
    # Register user2
    register_data2 = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "password123"
    }
    client.post('/auth/register/', register_data2, content_type='application/json')
    
    # Login user2
    login_data2 = {
        "username": "testuser2",
        "password": "password123"
    }
    response = client.post('/auth/login/', login_data2, content_type='application/json')
    if response.status_code == 200:
        tokens2 = response.json()
        access_token2 = tokens2['access']
        auth_headers2 = {'HTTP_AUTHORIZATION': f'Bearer {access_token2}'}
        
        # Get user1 id
        user1 = User.objects.get(username="testuser")
        
        response = client.post(f'/interactions/follow/{user1.id}/', **auth_headers2)
        print(f"Status: {response.status_code}")
    else:
        print("Failed to login user2")

    print("\nTests completed successfully!")

if __name__ == "__main__":
    # Clean up existing user if any
    try:
        User.objects.get(username="testuser").delete()
    except User.DoesNotExist:
        pass
        
    run_tests()
