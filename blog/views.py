from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):

    # Query의 select * from Post; 와 같다
    posts = Post.objects.all().order_by('-pk')

    return render(
        # request : 요청하는 클라이언트에게 주기 위해
        request,
        # django에서 자동으로 /templates/를 앞에 붙여준다.
        'blog/index.html',
        {
            "posts" : posts,
        }
    )

# pk 같이 클라이언트가 서버에 보내는 데이터 : parameter
#  post, posts 등 서버가 클라이언트에 보내는 데이터 : attribute
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post
        }
    )