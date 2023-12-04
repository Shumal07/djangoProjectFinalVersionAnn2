from django.views.generic import ListView, TemplateView
from .models import Post
from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Post

class BlogListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImputPageView(TemplateView):
    template_name = 'imput.html'


def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})



