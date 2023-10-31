from django.db import models #C언어의 include
from django.contrib.auth.models import User

# 게시판 모델
class Post(models.Model):
    member_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, null=False)
    content = models.TextField()
    hit = models.PositiveIntegerField(default=0)

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()


# 댓글 모델
class Reply(models.Model):
    member_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    


# 태그 모델
class Tag(models.Model):
    tag_name = models.CharField(max_length=30)



