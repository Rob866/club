from django.urls import path
from . import views

app_name ='blog'
urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('blog/<slug:id>',views.postDetail,name="post_detail"),

]
