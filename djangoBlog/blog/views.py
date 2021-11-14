import markdown
from django.shortcuts import render, get_object_or_404
# 视图,逻辑控制核心,模板渲染返回
# Create your views here.
from  django.http import  HttpResponse
from .models import  Post
def index(request):
    '''
    data={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    }
    return render(request, 'blog/index.html', context=data)
    return HttpResponse("欢迎访问我的博客首页！")'''
    posts=Post.objects.all()
    post_list=Post.objects.all().order_by('-createtime')
    return render(request,'blog/index.html', context={'post_list':post_list})

def detail(request, pk):
     post = get_object_or_404(Post, pk=pk)
     post.body = markdown.markdown(post.body,
                                   extensions=[
                                       'markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.toc',
                                   ])
     return render(request, 'blog/detail.html', context={'post': post})

