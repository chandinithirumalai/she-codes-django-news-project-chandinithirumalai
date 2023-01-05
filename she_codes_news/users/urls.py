
from django.urls import path
from .views import CreateAccountView,UserProfileView,AuthorsView 


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('view-authors', AuthorsView.as_view(), name='authors'),
]