from select import select
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render, redirect

# 导入数据模型ArticlePost
from .models import ArticlePost

# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm

# 引入User模型
from django.contrib.auth.models import User

import markdown

import random

from cmt.models import Cmt

import time

# 引入分页
from django.core.paginator import Paginator

from django.db.models import Q

def article_list(request):
    if request.method =="GET":
        if request.GET.get('ranges') and request.GET.get('keyword') and request.GET.get('type'):
            print("flag!")
            key_word = request.GET.get('keyword')
            labels = request.GET.get('ranges').split(',')
            type = request.GET.get('type')
            print('get_type:',type)
            order = "normal"
            lab = ""
            for i ,label in enumerate(labels):
                if i == len(labels)-1 :
                    lab += label
                else :
                    lab += label
                    lab += ","
            if len(labels) == 0:
                lab = 'cplus,csharp,python,java,js,php,SQL'
            t = time.time()         
            if 'else' in labels:
                article_list = ArticlePost.objects.all().filter(~Q(title__icontains='python'),~Q(body__icontains='python'),
                                                                ~Q(title__icontains='java'),~Q(body__icontains='java'),
                                                                ~Q(title__icontains='JavaScript'),~Q(body__icontains='JavaScript'),
                                                                ~Q(title__icontains='C++'),~Q(body__icontains='C++'),
                                                                ~Q(title__icontains='PHP'),~Q(body__icontains='PHP'),
                                                                ~Q(title__icontains='SQL'),~Q(body__icontains='SQL'),
                                                                ~Q(title__icontains='C#'),~Q(body__icontains='C#')) 
                for i, label in enumerate(labels):
                    if label == 'else':
                        continue
                    else:
                        article_list_temp = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[i]))|Q(body__icontains=yingshe(labels[i])))
                        for j in range(0,i):
                            if labels[j] == 'else':
                                continue
                            article_list_temp = article_list_temp.exclude(Q(title__icontains=yingshe(labels[j]))|Q(body__icontains=yingshe(labels[j])))
                        article_list  = article_list|article_list_temp
                    
            elif len(labels) !=0 and len(labels) != 8:
                article_list = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[0]))|Q(body__icontains=yingshe(labels[0])))
                for i, label in enumerate(labels):
                    if i == 0:
                        continue
                    else:
                        article_list_temp = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[i]))|Q(body__icontains=yingshe(labels[i])))
                        for j in range(0,i):
                            if labels[j] == 'else':
                                continue
                            article_list_temp = article_list_temp.exclude(Q(title__icontains=yingshe(labels[j]))|Q(body__icontains=yingshe(labels[j])))
                        article_list  = article_list|article_list_temp
            else:
                article_list = ArticlePost.objects.all()
                
            article_list = article_list.filter(Q(title__icontains=key_word)|
                                               Q(body__icontains=key_word)) 
            if 'java' in labels and 'js' not in labels:
                article_list = article_list.exclude(Q(title__icontains='javascript')|
                                               Q(body__icontains='javascript'))       
                # if 'python' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='python'),~Q(body__icontains='python'))
                # if 'java' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='java'),~Q(body__icontains='java'))
                # if 'cplus' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='C++'),~Q(body__icontains='C++'))
                # if 'js' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='JavaScript'),~Q(body__icontains='JavaScript'))
                # if 'php' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='PHP'),~Q(body__icontains='PHP'))
                # if 'SQL' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='SQL'),~Q(body__icontains='SQL'))
                # if 'csharp' not in labels:
                #     article_list = article_list.filter(~Q(title__icontains='C#'),~Q(body__icontains='C#'))
            
            if type == 'newest':
                article_list = article_list.order_by("-create_time")
                search_order = "newest"
            elif type == 'hottest':
                article_list = article_list.order_by("-views")
                search_order = 'hottest'
            else:
                article_list = article_list.order_by("-create_time")
                search_order = "newest"
            num = len(article_list)
            paginator = Paginator(article_list, 12)
            # 获取 url 中的页码
            page = request.GET.get('page')
            # 将导航对象相应的页码内容返回给 articles
            articles = paginator.get_page(page)
            for article in articles:
                print(article.id)
                article.comments=len(Cmt.objects.filter(article=article.id))
            searchtime = round(time.time() - t, 3)
            context = { 'articles': articles, 'order': order, 'select':'None', 'key_word':key_word, 'ranges':lab, 'search_time':searchtime ,'search_order':search_order, 'count':num}
            return render(request, 'article/list.html', context)
    
        if request.GET.get('order') == 'random_select':
            article_list =ArticlePost.objects.all().order_by('?')
            # print(type(article_list))
            order = 'random_select'
                 # 每页显示 1 篇文章
            paginator = Paginator(article_list, 20)
            # 获取 url 中的页码
            page = request.GET.get('page')
            # 将导航对象相应的页码内容返回给 articles
            articles = paginator.get_page(page)
            for article in articles:
                print(article.id)
                article.comments=len(Cmt.objects.filter(article=article.id))
        else:
            if request.GET.get('select')==None:
                article_list = ArticlePost.objects.all()
                # print(type(article_list))i
                order = 'normal'
                # 每页显示 1 篇文章
                paginator = Paginator(article_list, 12)
                # 获取 url 中的页码
                page = request.GET.get('page')
                # 将导航对象相应的页码内容返回给 articles
                articles = paginator.get_page(page)
                for article in articles:
                    print(article.id)
                    article.comments=len(Cmt.objects.filter(article=article.id))
            elif request.GET.get('select')=='None':
                article_list = ArticlePost.objects.all()
                # print(type(article_list))i
                order = 'normal'
                 # 每页显示 1 篇文章
                paginator = Paginator(article_list, 12)
                # 获取 url 中的页码
                page = request.GET.get('page')
                # 将导航对象相应的页码内容返回给 articles
                articles = paginator.get_page(page)
                for article in articles:
                    print(article.id)
                    article.comments=len(Cmt.objects.filter(article=article.id))
            else:
                target = request.GET.get('select')
                if target == 'else':
                    article_list = ArticlePost.objects.all().filter(~Q(body__icontains='C++'),
                                                                    ~Q(title__icontains='C++'),
                                                                    ~Q(body__icontains='Python'),
                                                                    ~Q(title__icontains='Python'),
                                                                    ~Q(body__icontains='SQL'),
                                                                    ~Q(title__icontains='SQL'),
                                                                    ~Q(body__icontains='PHP'),
                                                                    ~Q(title__icontains='PHP'),
                                                                    ~Q(body__icontains='Java'),
                                                                    ~Q(title__icontains='Java'),
                                                                    ~Q(body__icontains='JavaScript'),
                                                                    ~Q(title__icontains='JavaScript'),
                                                                    ~Q(body__icontains='C#'),
                                                                    ~Q(title__icontains='C#'))
                else:
                    article_list = ArticlePost.objects.all().filter(Q(tag = target) |
                                                                Q(body__icontains=yingshe(target))|
                                                                Q(title__icontains=yingshe(target)))
                if target == 'java':
                    article_list = article_list.exclude(Q(body__icontains='javascript')|
                                                        Q(title__icontains='javascript'))
                order = 'normal'
                paginator = Paginator(article_list, 12)
                # 获取 url 中的页码
                page = request.GET.get('page')
                # 将导航对象相应的页码内容返回给 articles
                articles = paginator.get_page(page)
                articles = paginator.get_page(page)
                for article in articles:
                    print(article.id)
                    article.comments=len(Cmt.objects.filter(article=article.id))
                context = { 'articles': articles, 'order': order, 'select':target }
                return render(request, 'article/list.html', context)
        context = { 'articles': articles, 'order': order, 'select':'None' }
        return render(request, 'article/list.html', context)
    if request.method == "POST":
        print("Post")
        labels = request.POST.getlist('label')
        key_word = request.POST['search']
        type = request.POST.getlist('type')
        print(type[0])
        if key_word:
            if len(key_word) > 50:
                key_word = key_word[0:50]
        lab = ""
        for i ,label in enumerate(labels):
            if i == len(labels)-1 :
                lab += label
            else :
                lab += label
                lab += ","
        order = "normal"
        if len(lab) == 0:
            lab = 'cplus,csharp,python,java,js,php,SQL,else'
        t = time.time()
        if 'else' in labels:
            article_list = ArticlePost.objects.all().filter(~Q(title__icontains='python'),~Q(body__icontains='python'),
                                                                ~Q(title__icontains='java'),~Q(body__icontains='java'),
                                                                ~Q(title__icontains='JavaScript'),~Q(body__icontains='JavaScript'),
                                                                ~Q(title__icontains='C++'),~Q(body__icontains='C++'),
                                                                ~Q(title__icontains='PHP'),~Q(body__icontains='PHP'),
                                                                ~Q(title__icontains='SQL'),~Q(body__icontains='SQL'),
                                                                ~Q(title__icontains='C#'),~Q(body__icontains='C#')) 
            for i, label in enumerate(labels):
                if label == 'else':
                    continue
                else:
                    article_list_temp = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[i]))|Q(body__icontains=yingshe(labels[i])))
                    for j in range(0,i):
                        if labels[j] == 'else':
                            continue
                        article_list_temp = article_list_temp.exclude(Q(title__icontains=yingshe(labels[j]))|Q(body__icontains=yingshe(labels[j])))
                        article_list = article_list|article_list_temp
                    
        elif len(labels) !=0 and len(labels) !=8:
            article_list = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[0]))|Q(body__icontains=yingshe(labels[0])))
            for i, label in enumerate(labels):
                if i == 0:
                    continue
                else:
                    article_list_temp = ArticlePost.objects.all().filter(Q(title__icontains=yingshe(labels[i]))|Q(body__icontains=yingshe(labels[i])))
                    for j in range(0,i):
                        if labels[j] == 'else':
                            continue
                        article_list_temp = article_list_temp.exclude(Q(title__icontains=yingshe(labels[j]))|Q(body__icontains=yingshe(labels[j])))
                    article_list = article_list|article_list_temp
        else:
            article_list = ArticlePost.objects.all()
                
        article_list = article_list.filter(Q(title__icontains=key_word)|
                                               Q(body__icontains=key_word))  
        if 'java' in labels and 'js' not in labels:
            article_list = article_list.exclude(Q(title__icontains='javascript')|
                                               Q(body__icontains='javascript'))
        if type[0] == 'new':
            # print('if')
            article_list = article_list.order_by("-create_time")
            search_order = "newest"
        elif type[0] == 'hot':
            # print('elif')
            article_list = article_list.order_by("-views")
            search_order = 'hottest'
        else:
            # print('else')
            article_list = article_list.order_by("-create_time")
            search_order = "newest"
        paginator = Paginator(article_list, 12)
        # 获取 url 中的页码
        page = request.GET.get('page')
        # 将导航对象相应的页码内容返回给 articles
        articles = paginator.get_page(page)
        searchtime = round(time.time() - t, 3)
        num = len(article_list)
        for article in articles:
            print(article.id)
            article.comments=len(Cmt.objects.filter(article=article.id))
        context = { 'articles': articles, 'order': order, 'select':'None', 'key_word':key_word, 'ranges':lab, 'search_time':searchtime ,'search_order':search_order, 'count':num}
        return render(request, 'article/list.html', context)

def yingshe(name):
    if name == 'java':
        return 'Java'
    elif name == 'csharp':
        return 'C#'
    elif name == 'js':
        return 'JavaScript'
    elif name == 'cplus':
        return 'C++'
    elif name == 'SQL':
        return 'SQL'
    elif name == 'php':
        return 'PHP'
    elif name == 'python':
        return 'Python'
    else:
        return 'else'

def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    label = ""
    if str(article.title).lower().find('python')!=-1 or str(article.body).lower().find('python')!=-1:
        label += " Python;"
    if str(article.title).lower().find('C#')!=-1 or str(article.body).lower().find('C#')!=-1:
        label += " C#;"
    if str(article.title).lower().find('java')!=-1 or str(article.body).lower().find('java')!=-1:
        label += " Java;"
    if str(article.title).lower().find('php')!=-1 or str(article.body).lower().find('php')!=-1:
        label += " PHP;"
    if str(article.title).lower().find('sql')!=-1 or str(article.body).lower().find('sql')!=-1:
        label += " SQL;"
    if str(article.title).lower().find('javascript')!=-1 or str(article.body).lower().find('javascript')!=-1:
        label += " JavaScript;"
    if str(article.title).lower().find('c++')!=-1 or str(article.body).lower().find('c++')!=-1:
        label += " C++;"
    if label == "":
        label = '其他; '
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    cmt = Cmt.objects.filter(article=id).order_by('-created')
    # 需要传递给模板的对象
    context = { 'article': article, 'cmt': cmt, 'labels':label}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

# def article_select(request, select_type):
#     target_type = request.GET.get('select')
#     article_list = ArticlePost.objects.filter(tag = target_type)
#     order = 'normal'
#     paginator = Paginator(article_list, 20)
#     # 获取 url 中的页码
#     page = request.GET.get('page')
#     # 将导航对象相应的页码内容返回给 articles
#     articles = paginator.get_page(page)
#     context = { 'articles': articles, 'order': order }
#     return render(request, 'article/list.html', context)

def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)
    
# 删文章
def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")