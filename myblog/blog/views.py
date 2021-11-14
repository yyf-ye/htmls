from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Post
def index(request):
    # return HttpResponse("欢迎访问我的博客首页！  ---by penghui")

    # data={
    #     'data1': '我的博客首页',
    #     'welcome': '欢迎访问我的博客首页'
    # }
    # return render(request, 'blog/index.html', context=data)

    post_list = Post.objects.all().order_by('-createtime')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def detail(request, pk):
    # Post.objects.get(id=1)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})

