from django.contrib import admin
from .models import KnowledgeBase, ChatSession, ChatMessage

admin.site.register(KnowledgeBase)
admin.site.register(ChatSession)
admin.site.register(ChatMessage)

