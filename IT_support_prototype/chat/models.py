from django.db import models
from django.contrib.auth.models import User

class KnowledgeBase(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    chunk_index=models.PositiveIntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-Chunk {self.chunk_index}"

class ChatSession(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    session_id=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.session_id}({self.user.username})"
    
class ChatMessage(models.Model):
    session=models.ForeignKey(ChatSession,on_delete=models.CASCADE)
    message=models.TextField()
    is_user=models.BooleanField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'User' if self.is_user else "Bot"}:{self.message[:30]}..."
    