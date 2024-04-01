from rest_framework.authtoken.models import Token
import base64
from django.core.files.base import ContentFile

class BookStoreUtils :
    @staticmethod
    def base64_to_image(base64_image, image_name):
        try :
            format, imgstr = base64_image.split(';base64,') 
            ext = format.split('/')[-1] 
            image = ContentFile(base64.b64decode(imgstr), name=image_name+'.' + ext)
            return image
       
        except :
            return None 
        
        
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