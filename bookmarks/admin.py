from django.contrib import admin

# Register your models here.

from .models import Bookmark
from .models import PersonalBookmark

admin.site.register(Bookmark, PersonalBookmark)