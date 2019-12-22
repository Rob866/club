from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post,Comentario
from .forms import CommentForm
from django.http import HttpResponseRedirect
def blog(request):
    posts = Post.objects.filter(status=1).order_by('-create_on')
    context= {
    'posts': posts
    }
    return render(request,'blog/blog.html',context)

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
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_object
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post_object
            # save
            new_comment.save()
            return HttpResponseRedirect(post_object.get_absolute_url())
    else:
        comment_form= CommentForm()
    context = {
    'post': post_object,
    'comentarios': comentarios,
    'comment_form':comment_form
    }
    return render(request,'blog/detail_post.html',context)
