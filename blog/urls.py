from django.urls import path
from blog import views
from .views import BlogListView, AboutPageView, ImputPageView, profile_view
from .views import search_view, advanced_search_view

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('imput/', ImputPageView.as_view(), name='imput'),
    path('search/', search_view, name='search'),  # Обычный поиск
    path('advanced_search/', advanced_search_view, name='advanced_search'),  # Расширенный поиск
    path('profile/', profile_view, name='profile'),
]
