from django.urls import path
from . import views

app_name ='blog'
urlpatterns = [
    path('blog/',views.blog.as_view(),name='blog'),
    path('blog/<slug:id>/',views.postDetail,name="post_detail"),
    path('contact/', views.contact,name="contact")

]
