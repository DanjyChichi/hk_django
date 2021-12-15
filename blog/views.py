from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):

    # Query의 select * from Post; 와 같다
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        # django에서 자동으로 /templates/를 앞에 붙여준다.
        'blog/index.html',
        {
            "posts" : posts,
        }
    )