from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import datetime,timedelta

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='student/images', null=True, blank=True)
	details = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.name}'

	def get_image_url(self):
		return f'/media/{self.image}'

	@classmethod
	def get_all_books(cls):
		return cls.objects.all()
	@classmethod
	def get_specific_book(cls, book_id):
		return cls.objects.get(id=book_id)


class Student(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
	email = models.EmailField(max_length=100, null=True)
	phone =models.IntegerField(null=True)
	school=models.CharField(max_length=50,null=True)
	image = models.ImageField(upload_to='student/images', null=True, blank=True)
	book = models.CharField(null=True, max_length=100)
	password = models.CharField(max_length=50, null=True)
	password2 = models.CharField(max_length=50, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name}'

	def get_image_url(self):
		return f'/media/{self.image}'

	@classmethod
	def get_specific_student(cls, student_id):
		return cls.objects.get(id=student_id)
	@classmethod
	def get_all_students(cls):
		return cls.objects.all()
def get_return_date():
	return datetime.today()+timedelta(days=7)

class Borrow(models.Model):
	borrow_date = models.DateField(auto_now=True)
	return_date = models.DateField(default=get_return_date)
	student_id= models.CharField(max_length=50,null=True)
	book = models.CharField(max_length=100, null=True)

	def __str__(self):
		return f'{self.book}'





