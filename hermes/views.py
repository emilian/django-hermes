from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'hermes/post_list.html'
    
    def get_queryset(self):
        return self.model.objects.order_by('created_on')


class CategoryPostListView(PostListView):
    slug = None
    
    def get_queryset(self):
        category_slug = self.kwargs.get('slug', None)
        
        if category_slug is None:
            category_slug = self.slug
            
        return self.model.objects.in_category(category_slug)


class ArchivePostListView(PostListView):
    def get_queryset(self):
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        day = self.kwargs.get('day', None)

        return self.model.objects.created_on(year=year, month=month, day=day)


class PostDetail(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = "hermes/post_detail.html"

class CategoryPostDetail(DetailView):
    category_slug = None
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.filter(category__slug=category_slug)
    template_name = 'hermes/post_detail.html'
