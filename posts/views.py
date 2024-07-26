from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms  import PostForm


# 一覧画面を表示する 
class IndexView(View):
  def get(self, request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


class CreateView(View):
  # 投稿画面を表示する 
  def get(self, request, *args, **kwargs):
    form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

  # 投稿内容を保存する
  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST)
    # バリデーションのチェック
    if form.is_valid():
      # 投稿に問題がなければ保存する
      post = form.save()
      # redirectで一覧画面に移動する
      return redirect('posts:index')
  