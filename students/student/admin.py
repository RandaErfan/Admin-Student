from django.contrib import admin
from .models import Student, Book, Borrow

# Register your models here.
admin.site.register(Book)
admin.site.register(Borrow)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','age','book','school')
    search_fields = ['id']

admin.site.register(Student,StudentAdmin)
