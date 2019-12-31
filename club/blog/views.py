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
    comentarios = post_object.comentarios.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = Comentario(post=post_object,nombre=request.POST["nombre"],mensaje=request.POST["mensaje"])
            new_comment.save();
            comment_form.cleaned_data
        return HttpResponseRedirect(post_object.get_absolute_url())
    else:
        comment_form= CommentForm()
    #obtengo todos los posts activos
    posts = Post.objects.filter(status=1)
    # los ordeno segun el numero de comentarios activos (mayor a menor)
    order_post_by_comments = sorted(posts,key= lambda post: len(post.comentarios.filter(active=True)),reverse=True)
    # me  aseguro que las lista de los post mas comentados sea como máximo 5 posts
    if len(order_post_by_comments) > 5 :
        order_post_by_comments = order_post_by_comments[:6]
    # post = posts.get(id=id)
    # obtengo el index de mi actual post
    index = list(posts).index(post_object)
    # hago que el index de mi post actual sea el mismo que el del post anterior
    # este se mantendra  siempre que sea el post acual el primer post
    post_anterior = posts[index]
    # mi lista es reverse(lo ultimos post se posicionan con menor index que los primeros posts)
    # si el index del item(post) + 1 es mayor que la longitud de mi lista significa
    # que es este el primer post(o el ultimo item en la lista o el post con mayor index)
    # por tanto no hay un post anterior este o un post con mayor index.
    # Para evitar acceder a un index que  esta fuera del rango
    # no incremento el index que me enviará al post anterior(ya que esun index que no existe) y
    # dejo  que sea el mismo index que el primer post.
    if( (index + 1 ) < len(posts)):
        post_anterior = posts[index + 1]

    context = {
    'post_anterior': post_anterior,
    'order_post_by_comments': order_post_by_comments,
    'posts': posts,
    'post': post_object,
    'comentarios': comentarios,
    'comment_form':comment_form
    }
    return render(request,'blog/detail_post.html',context)
