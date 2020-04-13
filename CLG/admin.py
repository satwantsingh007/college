from django.contrib import admin

from .models import Studentregister
from .models import Facultyregister
from .models import Library
from .models import Document
from .models import Report

admin.site.register(Studentregister)
admin.site.register(Facultyregister)
admin.site.register(Library)
admin.site.register(Document)
admin.site.register(Report)