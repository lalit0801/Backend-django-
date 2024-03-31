from rest_framework.authtoken.models import Token

def create_token(user):
    try:
        # Create or retrieve token for user
        token, created = Token.objects.get_or_create(user=user)
        return token
    except Exception as e:
        # Handle any errors during token creation
        print(f"Error creating token: {e}")
        return None

def delete_token(token):
    try:
        # Delete token
        if token:
            token.delete()
            return True  # Token deletion successful
        else:
            return False  # Token does not exist
    except Exception as e:
        # Handle any errors during token deletion
        print(f"Error deleting token: {e}")
        return False