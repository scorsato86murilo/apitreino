from django.contrib.auth.models import User
from django.db import IntegrityError

def create_superuser():
    if not User.objects.filter(username='adminadmin').exists():
        try:
            # Cria o superusuário
            User.objects.create_superuser(
                username='adminadmin',
                email='admin@example.com',
                password='adminpassword'
            )
            print("Superuser created successfully!")
        except IntegrityError:
            print("Error: A superuser with the username 'admin' already exists.")
    else:
        print("Superuser with username 'admin' already exists. No action taken.")
