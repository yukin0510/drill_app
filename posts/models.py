from django.db import models
from django.utils import timezone

class Post(models.Model):
  class Meta:
    # テーブル名を定義する
    db_table = 'post'
  # テーブルのカラムに対応するフィールドを定義する
  content = models.CharField(verbose_name='投稿文')
  created_at = models.DateTimeField(verbose_name='投稿日時', default=timezone.now)
  def save(self, *args, **kwargs):
      # 新規レコードの場合のみ処理
       if not self.pk:
           # 最大のIDを取得し、それに1を加える
           max_id = Post.objects.aggregate(models.Max('id'))['id__max']
           self.pk = max_id + 1 if max_id else 1
        
       super(Post, self).save(*args, **kwargs)

  