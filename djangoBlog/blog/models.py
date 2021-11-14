from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
import markdown
# 用写底层类
# Create your models here.
# 文章分类
class Category(models.Model):
    # id会自动生成，可以省略不写,
    name=models.CharField(max_length=20)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name
    # 文章标签
class Tag(models.Model):
    #id , name,其中id可以.省略
    name=models.CharField(max_length=24)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name
# 文章本身
class Post(models.Model):
    # 标题、正文发表时河(创键时问、修改时间) 文章的分类文章的标签
    title=models.CharField('标题',max_length=200)
    body=models.TextField('正文')
    createtime=models.DateTimeField('创建时间', default=timezone.now)
    modifytime=models.DateTimeField('修改时间')
    # 摘要
    excerpt=models.CharField('摘要',max_length=250,blank=True)
    # 播客文章类型和文章的关系:一对多，在多的一方增加外键
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    # 文章标签
    tag = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    # 用户
    from django.contrib.auth.models import User
    author=models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.title

    def save(self, *args, **kwargs):
        self.modifytime= timezone.now()
        # super().save(*args, **kwargs)
        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

# 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    # def __str__(self):
    #     return  self.name