from django.shortcuts import render, HttpResponse, redirect
from .models import Article, Comment

def check(request):
    return HttpResponse("Everything is fine!")

def home(request):
    articles = Article.objects.all().order_by("-publish_date")

    return render(request, "home.html", context={"articles": articles})

def article_page(request, article_id):
    article = Article.objects.get(id=article_id)

    comments = Comment.objects.filter(article=article)

    return render(request, "article.html", context={"article": article, "comments": comments})


def add_comment(request, article_id):
    if request.method == "POST":
        n = request.POST["name"]
        b = request.POST["body"]

        Comment.objects.create(name=n, body=b, article_id=article_id)

        return redirect('articles:article_page', article_id=article_id)