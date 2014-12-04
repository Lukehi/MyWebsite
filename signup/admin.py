from django.contrib import admin

# Takes the models and registers them. Makes them useable by the server
# Register your models here.

# To make a model available to the admin page we first need to import it
from models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
