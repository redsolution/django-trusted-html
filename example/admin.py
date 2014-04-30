from django.contrib import admin
from example.models import MyModel, ExternalModel

admin.site.register(MyModel)
admin.site.register(ExternalModel)
