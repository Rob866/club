from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post,Comentario,Mensaje
from .forms import CommentForm,MensajeForm
import uuid
from django.http import HttpResponseRedirect
from django.views.generic import (ListView)
from django.urls import reverse

class blog(ListView):
    template_name= 'blog/blog.html'
    context_object_name='posts'
    paginate_by= 3

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-create_on')

def contact(request):

    if request.method == 'POST':
        mensaje_form = MensajeForm(data=request.POST)
        if mensaje_form.is_valid():
            mensaje = Mensaje(nombre=request.POST["nombre"],asunto=request.POST["asunto"],email=request.POST["email"],body=request.POST["body"])
            mensaje.save()
            mensaje_form.cleaned_data
            return HttpResponseRedirect(reverse('blog:contact'))
    else:
        mensaje_form = MensajeForm()
        context = {
         'mensaje_form': mensaje_form
        }
        return render(request,'blog/contact.html',context)


def postDetail(request,id):
    post_object = get_object_or_404(Post,id=id)
    comentarios = post_object.comentarios.filter(active=True,parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_object= None
            try:
                parent_id = request.POST.get('parent_id')
            except :
                parent_id= None
            if parent_id:
                parent_object= Comentario.objects.get(id=parent_id)
                if parent_object:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_object
            new_comment = comment_form.save(commit=False)
            new_comment.post = post_object
            new_comment.save()
            return HttpResponseRedirect(post_object.get_absolute_url())
    else:
        comment_form= CommentForm()

    posts = Post.objects.filter(status=1).order_by('-create_on')
    post = posts.get(id=id)
    index = list(posts).index(post)
    post_anterior = posts[index]

    if( (index + 1 ) < len(posts)):
        post_anterior = posts[index + 1]

    context = {
    'post_anterior': post_anterior,
    'posts': posts,
    'post': post_object,
    'comentarios': comentarios,
    'comment_form':comment_form
    }
    return render(request,'blog/detail_post.html',context)
