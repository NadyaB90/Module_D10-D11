from django.urls import path
from django.views.decorators.cache import cache_page

from .views import PostsList, PostDetail, SearchList, PostCreateView, PostUpdateView, PostDeleteView, \
    CategorySubscribeView, subscribe_category


urlpatterns = [
    path('', cache_page(60), PostsList.as_view()),
    path('<int:pk>', cache_page(300), PostDetail.as_view()),
    path('search/', SearchList.as_view(), name='post_search'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/', CategorySubscribeView.as_view()),
    path('subscribe/<int:pk>', subscribe_category, name='subscribe_category'),
]

