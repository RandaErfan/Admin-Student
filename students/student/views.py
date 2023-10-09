from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect 
from .models import Student, Book, Borrow
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, StudentModelForm ,BookModelForm,PasswordModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from datetime import date ,timedelta

# Create your views here.
def index(request):
	return render(request,'layout/index.html')
def home(request):
	return render(request,'home.html')
def students(request):
	return render(request,'students.html')
def admin(request):
	return render(request,'admin.html')
def login_admin(request):
	students = Student.objects.all()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			for student in students:
				if username == student.name:
					return render(request, 'layout/home_admin.html', {'user':user})
		else:
			return HttpResponse("the email or password is not correct !!!")

	return render(request, 'login_admin.html')


def admin_books(request):
	books = Book.objects.all()
	return render(request, 'admin_books.html', {"books": books})

def admin_students(request):
	students = Student.objects.all()
	return render(request, 'admin_students.html', {"students": students})
def admin_borrow(request):
	borrows = Borrow.objects.all()
	books = Book.objects.all()
	return render(request, 'admin_borrow.html', {"borrows": borrows,"books":books})
def books(request):
	books = Book.objects.all()

	return render(request, 'books.html', {"books": books})

def show(request,book_id):
	book = Book.objects.get(id=book_id)
	return render(request, 'show.html', {"book": book})

def books_add(request):
	books=Book.objects.all()
	form = BookModelForm()
	if request.method == 'POST':
		form = BookModelForm(request.POST, request.FILES)
		if form.is_valid():
			for book in books:
				if request.POST['name'] == book.name:
					return HttpResponse('This book is added before ,try to add a different book!!!!')
			form.save()
			url = reverse('admin.books')
			return redirect(url)
		return render(request, 'books_add.html', context={"form": form})

	return render(request, 'books_add.html', context={"form":form})

def books_edit(request,book_id):
	if request.method == 'POST':
		book.name = request.POST['name']
		book.details = request.POST['details']
		book.image = request.FILES['image']
		book.save()
		url = reverse('admin.books')
		return redirect(url)
	return render(request, 'books_edit.html', context={'book':book})
	
def books_delete(request,book_id):
	book = Book.objects.get(id=book_id)
	book.delete()
	bact_to_url = reverse('admin.books')
	return redirect(bact_to_url)

def student_show(request,student_id):
	borrow = Borrow.objects.all()
	student = Student.objects.get(id=student_id)
	for bor in borrow:
		if student.name ==  bor.student_id:
			student.book = bor.book
			student.save()
	return render(request,'student_show.html',{"student":student})

def student_add(request):
	stds=Student.objects.all()
	form = StudentModelForm()
	if request.method == 'POST':
		form = StudentModelForm(request.POST, request.FILES)
		if form.is_valid():
			for std in stds:
				if request.POST['name'] == std.name:
					return HttpResponse('This book is added before ,try to add a different book!!!!')
			form.save()
			url = reverse('admin.students')
			return redirect(url)

	return render(request, 'student_add.html', context={"form":form})

def student_password(request,student_id):
	student = Student.get_specific_student(student_id)
	if request.method == 'POST':
		student.password = request.POST['password']
		student.password2 = request.POST['password2']
		student.save()
		url = reverse('admin.students')
		return redirect(url)

	return render(request, 'student_password.html', context={"student":student})


def student_delete(request,student_id):
    student = student.objects.get(id=student_id)
    student.delete()
    bact_to_url = reverse('admin.students')
    return redirect(bact_to_url)
	
def borrow_delete(request,borrow_id):
	borrow = Borrow.objects.get(id=borrow_id)
	borrow.delete()
	bact_to_url = reverse('admin.borrow')
	return redirect(bact_to_url)
	

def borrow(request,book_id):
	book1 = Book.objects.get(id=book_id)
	date_borrow = date.today()
	date_return = date_borrow + timedelta(days=7)
	if request.method == 'POST':
		borrow = Borrow(student_id=request.POST.get('student'),book=book1.name)
		borrow.save()
		return render(request,'books.html')
	return render(request, 'borrow.html', {"book1": book1,'date_borrow':date_borrow,'date_return':date_return})

def login(request):
	students = Student.objects.all()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			for student in students:
				if username == student.name:
					return render(request, 'layout/base.html', {'user':user,'student':student})
		else:
			return HttpResponse("the email or password is not correct !!!")

	return render(request, 'login.html')

def register(request):
	books = Book.get_all_books()
	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES)
		if form.is_valid():
			if 'image' in request.FILES:
				image = request.FILES['image']
			else:
				image = None
				book = None
			if 'book_id' in request.POST:
				book = Book.objects.get(id=request.POST['book_id'])
			if request.POST['password'] != request.POST['password2']:
				return HttpResponse("your password and confirm password are not the same")
			student = Student(name=request.POST['name'], email=request.POST['email'], image=image, age=request.POST['age'],phone=request.POST['phone'],school=request.POST['school'], password=request.POST['password'], password2=request.POST['password2'])
			student.save()
			name = request.POST.get('name')
			email = request.POST.get('email')
			pass1 = request.POST.get('password')
			pass2 = request.POST.get('password2')
			if pass1 != pass2:
				return HttpResponse("your password and confirm password are not the same")
			my_user = User.objects.create_user(name, email, pass1)
			my_user.save()
			url = reverse('students.login')
			return redirect(url)
		print(form.errors)
		return render(request, 'register.html', context={"form": form,'books': books})
	return render(request, 'register.html', {'books': books})


def createViaModelForm(request):
	form = StudentModelForm()
	if request.method == 'POST':
		form = StudentModelForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			url = reverse('students.home')
			return redirect(url)
		return render(request, 'register.html', context={"form": form})

	return render(request, 'register.html', context={"form":form})

def logout(request):
	return render(request, 'logout.html')

def update(request,student_id):
	books = Book.get_all_books()
	student = Student.get_specific_student(student_id)
	if request.method == 'POST':
		student.name = request.POST['name']
		student.age = request.POST['age']
		student.school = request.POST['school']
		student.phone = request.POST['phone']
		student.email = request.POST['email']
		student.image=request.FILES['image']
		student.save()
		url = reverse('students.books')
		return redirect(url)
	return render(request, 'update.html', context={'student': student,'books':books})


def profile(request,student_id):
	borrow = Borrow.objects.all()
	student = Student.objects.get(id=student_id)
	for bor in borrow:
		if student.name ==  bor.student_id:
			student.book = bor.book
			student.save()

	return render(request,'profile.html',{'student':student})

def search(request):
	query=	request.GET.get('q')
	student=None
	if query is not None:
		student=Student.objects.get(id=query)
	context={"object":student}
	return render(request,'search.html',{'query':query,'object':student})
	