from django.shortcuts import HttpResponse,render
from blog.models import Post

def index(request):
    posts= Post.objects.all()[:11]
    
    #print(posts)
    data={
        'posts':posts
    }
    return render(request,'index.html',data)
