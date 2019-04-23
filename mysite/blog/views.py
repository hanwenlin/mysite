from django.shortcuts import render,get_object_or_404
from .models import BlogArticle
# Create your views here.

def blog_title(request):
    blogs = BlogArticle.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs})

def blog_details(request,article_id):
    # articles = BlogArticle.objects.get(id=blog_id)
    article = get_object_or_404(BlogArticle,id=article_id)
    pub = article.publish
    return render(request,'blog/content.html',{'article':article,'publish':pub})
