from django.db import models

# Create your models here.

class Feedback(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name or 'Anonymous'} - {self.created_at}"
