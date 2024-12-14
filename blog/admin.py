from django.contrib import admin
from .models import Post

# Adding our Post model to administration page
admin.site.register(Post)