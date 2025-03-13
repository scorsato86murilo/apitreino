from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from index.models import Index


def index(request):
    index = Index.objects.all().first()
    if not User.objects.filter(username='admin').exists():
        try:
            # Cria o superusuário
            User.objects.create_superuser(
                username='adminadmin',
                email='admin@example.com',
                password='adminpassword'
            )
            print("Superuser created successfully!")
        except IntegrityError:
            # Se ocorrer erro de integridade (por exemplo, se o nome de usuário já existir)
            print("Error: A superuser with the username 'admin' already exists.")
    else:
        print("Superuser with username 'admin' already exists. No action taken.")
    if request.method == 'GET':

        return render(request, 'index.html', {'index': index})
    elif request.method == 'POST':
        return render(request, 'index.html', {'index': index})
