# Create your tests here.
from bike_connect.apps.users.models import CustomUser

# Create a superuser
user = CustomUser.objects.create_superuser(
    username='admin123',
    email='admin@example.com',
    password='adminpassword',
    role='superuser'
)
print("Superuser created successfully:", user)
