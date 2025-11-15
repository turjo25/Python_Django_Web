from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

#router banayce ja request capture korbe
router = DefaultRouter()#crud er kon request kortese ta capture kora and sheitar response kora
router.register('authors',views.AuthorViewSet)#eita ak sthe 4 ta operation handle korbe --> CRUD

urlpatterns = [
    # path('author/',views.author_list_create,name='author_list_create'),
    path('',include(router.urls)),
    path('book/',views.book_list_create,name='book_list_create'),
    path('book/<int:id>/',views.book_details,name='book_details'),
]