from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by("-created_at")  # Pobierz wszystkie posty, najnowsze pierwsze
    # Aktualizujemy liczbę wyświetleń, jeśli użytkownik otworzy stronę
    for post in posts:
        post.save()

    return render(request, "MojaAplikacjaGlowna/home.html", {"posts": posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Zapisujemy nowy post do bazy
            return redirect("home")  # Po zapisaniu przekierowujemy na stronę główną
    else:
        form = PostForm()

    return render(request, "MojaAplikacjaGlowna/create_post.html", {"form": form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Pobranie posta lub zwrócenie 404
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")  # Powrót do strony głównej po zapisaniu zmian
    else:
        form = PostForm(instance=post)  # Wczytanie istniejącego posta do formularza

    return render(request, "MojaAplikacjaGlowna/edit_post.html", {"form": form, "post": post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":  # Jeśli użytkownik kliknął "Usuń"
        post.delete()
        return redirect("home")  # Powrót na stronę główną po usunięciu

    return render(request, "MojaAplikacjaGlowna/delete_post.html", {"post": post})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({"likes": post.likes})  # Zwracamy nową liczbę polubień


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Zwiększenie licznika wyświetleń tylko dla danego posta
    post.views += 1
    post.save()

    return render(request, "MojaAplikacjaGlowna/post_detail.html", {"post": post})
