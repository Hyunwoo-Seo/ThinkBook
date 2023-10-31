from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Reply, Tag
from .forms import PostForm, ReplyForm
from django.utils import timezone
from django.contrib.auth.models import User


def postDetailView(request, pk):
    post_detail = get_object_or_404(Post, id=pk)
    return render(request, 'board/postDetail.html',{'post':post_detail})



def postListView(request):
    post_list = Post.objects.all() # 페이징 구현 해와
    context = {'post_list', post_list}
    return render(request, 'board/postList.html', {'post_list': post_list}) # 페이지는 나중에 추가할 예정 테스트 할려면 html 만들어서 하셈

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.member_id = request.user
            post.save()
            return redirect('board:post_list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'board/postWrite.html', context)

    
def postDelete(request, pk):
    board = Post.objects.get(id=pk)
    board.delete()
    return redirect('/')

def comment(request, post_id):

    if request.method == "POST":
        Reply_form = ReplyForm(request.POST)
        Reply_form.instance.author_id = request.user.id
        Reply_form.instance.post_id = post_id
        if Reply_form.is_valid():
            comment = Reply_form.save()
    return redirect(request, '/', {'Reply_form':Reply_form}) # 댓글 작성 후 해당 페이지 다시 보게 수정해야함


def commentDelete(request, pk):
    comment = Reply.objects.get(id=pk)
    comment.delete()
    return redirect('comment')
