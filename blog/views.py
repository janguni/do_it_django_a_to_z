from unicodedata import category
from django.views.generic import ListView, DetailView
from .models import Category, Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()
        return context

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
