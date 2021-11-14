from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
#博客文章分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


#具体文章
class Post(models.Model):
    title = models.CharField("标题",max_length=100)
    body = models.TextField('正文')
    createtime = models.DateTimeField('创建时间', default=timezone.now)
    modifytime = models.DateTimeField('修改时间', default=timezone.now)
    #摘要
    excerpt = models.CharField('摘要',max_length=250, blank=True)
    category = models.ForeignKey(Category, verbose_name="类别",on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,verbose_name="标签", blank=True)

    from django.contrib.auth.models import User
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(User,verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数


    def get_absolute_url(self):
        #反向解析得到url地址
        return reverse('blog:detail', kwargs={'pk': self.pk})

