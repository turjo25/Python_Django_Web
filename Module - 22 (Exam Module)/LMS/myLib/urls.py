from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.book_list, name = 'book_list'),
    path('book/add', views.add_book, name = 'add_book'),
    path('book/update/<int:id>/', views.book_update, name = 'book_update'),
    path('book/delete/<int:id>/', views.book_delete, name = 'book_delete'),
    path('book/details/<int:id>/', views.book_details, name = 'book_details'),
    path('signup/', views.signup_view, name = 'signup'),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
     path('update_profile/',views.update_profile,name='update_profile'),
      path('pass_change/',views.pass_change,name='pass_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)