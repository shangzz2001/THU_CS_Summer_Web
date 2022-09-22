# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'cmt'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
    # 删除评论
    path('cmt-delete/<int:article_id>/<int:id>/', views.cmt_delete, name='cmt_delete'),
]