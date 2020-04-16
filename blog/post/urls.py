from django.urls import path
from . import views

app_name='post'

urlpatterns=[
    path('',views.home,name='home'),
    path('addpost',views.add_post,name='add_post'),
    path('tag_post/<str:tag>',views.tag_post,name='tag_post'),
    path('login',views.log_in,name='log_in'),
    path('signup',views.sign_up,name='sign_up'),
    path('logout',views.log_out,name='log_out'),
    path('allposts',views.all_post,name='all_post'),
    path('post_detail/<int:p_id>',views.post_detail,name='detail'),
    path('like/<int:p_id>',views.like,name='like'),
    

]