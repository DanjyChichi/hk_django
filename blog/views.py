from django.shortcuts import render
from django.views.generic import ListView, DetailView # ListView는 여려개를 조회할떄 DetailView는 목록에 의한 한개의 아이템을 조회할때
from .models import Post

# ListView에
class PostList(ListView):
    # Post를 채울 것이다.
    model = Post # 이 코드만 써도 내부적으로 전체 조회가 된다.

    # 장고의 ListView에서 자동으로 지정하는
    # post_list.html을 사용하지 않고, index.html울 사용
    # abstraction 추상화에 대해 공부할 것
    # template_name = "blog/index.html"

    # 데이터 조회 정렬하기
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post




# def index(request):
#
#     # Query의 select * from Post; 와 같다
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         # request : 요청하는 클라이언트에게 주기 위해
#         request,
#         # django에서 자동으로 /templates/를 앞에 붙여준다.
#         'blog/index.html',
#         {
#             "posts" : posts,
#         }
#     )

# pk 같이 클라이언트가 서버에 보내는 데이터 : parameter
#  post, posts 등 서버가 클라이언트에 보내는 데이터 : attribute
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post' : post
#         }
#     )