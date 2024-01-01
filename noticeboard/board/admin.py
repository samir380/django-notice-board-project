from django.contrib import admin
from .models import Notice,CategoryTypes,EmailSubscriber

admin.site.register(Notice)
admin.site.register(CategoryTypes)
admin.site.register(EmailSubscriber)