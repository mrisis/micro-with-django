from django.db import models


class Post(models.Model):
    POST_TYPES = (
        ('EDUCATIONAL', 'Educational'),
        ('CONSULTING', 'Consulting'),
        ('JOB', 'Job Opportunity'),
        ('COURSE', 'Course'),
        ('GENERAL', 'General'),
    )

    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by User {self.user_id} on {self.post.title}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user_id = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user_id')

    def __str__(self):
        return f"Like by User {self.user_id} on {self.post.title}"