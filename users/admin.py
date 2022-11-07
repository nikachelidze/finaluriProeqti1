from django.contrib import admin
from users.models import User,car,comment

# Register your models here.

admin.site.register([User,car,comment])
