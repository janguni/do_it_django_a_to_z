from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# FBV 방식 blog 목록
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request, d
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

# FBV 방식 blog 상세목록
# def single_post_page(request,pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
