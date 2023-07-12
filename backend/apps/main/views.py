from django.shortcuts import render
from .models import Photo
from backend.apps.gallery.models import Video
from ..gallery.models import Gallery
from backend.apps.news.models import Articles
    

def index(request):
    video = Video.objects.all()[:2]
    gallery = Gallery.objects.all()[:2]
    photos = Photo.objects.all()[:1]
    news = Articles.objects.all()[:3]        # если добавить то только выйдет 6 информации[:6]
    context = {
        "photos": photos,
        "video": video,
        "news": news,
        "gallery": gallery,
    }
    return render(request, 'main/index.html', context)

    
def about(request):
    return render(request, 'main/about.html')   


def finance(request):
    return render(request, 'main/finance.html')

def whoe(request):
    return render(request, 'main/whole_funding.html')