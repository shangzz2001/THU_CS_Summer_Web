from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from .forms import CommentForm
from .models import Cmt
import markdown
# 文章评论
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            # new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")
    
def cmt_delete(request, article_id, id):
    # cmt = Cmt.objects.filter(article=article_id,id=id)
    # cmt.delete()
    # 取出相应的文章
    article = ArticlePost.objects.get(id=article_id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    cmt = Cmt.objects.filter(article=article_id,id=id)
    cmt.delete()
    # cmt = Cmt.objects.filter(article=id).order_by('-created')
    cmt = Cmt.objects.filter(article=article_id).order_by('-created')
    # 需要传递给模板的对象
    context = { 'article': article, 'cmt': cmt}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)