from django.shortcuts import render
from .models import Index, Video
from .superuser import create_superuser


def index(request):
    index = Index.objects.all().first()
    video = Video.objects.all().first()

    # Chame a função que cria o superusuário
    create_superuser()

    if request.method == 'GET':
        return render(request, 'index.html', {'index': index, 'video': video})
    elif request.method == 'POST':
        return render(request, 'index.html', {'index': index, 'video': video})
