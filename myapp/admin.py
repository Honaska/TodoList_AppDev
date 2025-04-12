from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages

from .models import Post, Comment, AuthToken
from .utils import generate_random_token

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'label', 'created')
    readonly_fields = ('key',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate/', self.admin_site.admin_view(self.generate_token_view), name='generate_token'),
        ]
        return custom_urls + urls

    def generate_token_view(self, request):
        token = generate_random_token()
        AuthToken.objects.create(key=token, label='Generated manually')
        
        messages.success(request, f'Generated new token: {token}')
        
        return redirect('admin:myapp_authtoken_changelist')