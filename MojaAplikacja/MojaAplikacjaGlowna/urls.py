from django.urls import path
from .views import home, create_post, edit_post, delete_post, like_post, post_detail

urlpatterns = [
    path('', home, name='home'),
    path("new/", create_post, name="create_post"),
    path("edit/<int:post_id>/", edit_post, name="edit_post"),  # Nowa ścieżka do edycji posta
    path("delete/<int:post_id>/", delete_post, name="delete_post"),  # Nowa ścieżka do usuwania posta
    path("like/<int:post_id>/", like_post, name="like_post"),  # Ścieżka do polubień
path("post/<int:post_id>/", post_detail, name="post_detail"),  # Nowa ścieżka do szczegółów posta
]
