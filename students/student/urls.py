from django.urls import path 
from .views import home, books ,login, logout,search, register, show, borrow, update, profile,student_password,index,students,admin,login_admin,admin_students,admin_books,admin_borrow,books_add,books_edit,student_add,books_delete,student_delete,borrow_delete,student_show


urlpatterns = [
    path('books/', books, name='students.books'),
    path('home/',home,name='home'),
    path('index/',index,name='students.index'),
    path('register/', register, name='students.register'),
    path('login/', login, name='students.login'),
    path('logout/', logout, name='students.logout'),
    path('show/<int:book_id>/', show, name='books.show'),
    path('borrow/<int:book_id>', borrow, name='books.borrow'),
    path('update/<int:student_id>',update,name='students.update'),
    path('profile/<int:student_id>',profile,name='students.profile'),
    path('students/', students, name='students.home'),
    path('admin/', admin, name='admin.home'),
    path('login_admin/', login_admin, name='admin.login'),
    path('admin_students/', admin_students, name='admin.students'),
    path('admin_books/', admin_books, name='admin.books'),
    path('admin_borrow/', admin_borrow, name='admin.borrow'),
    path('books_add/', books_add, name='books.add'),
    path('books_edit/<int:book_id>', books_edit, name='books.edit'),
    path('books_delete/<int:book_id>', books_delete, name='books.delete'),
    path('student_add/', student_add, name='student.add'),
    path('student_show/<int:student_id>', student_show, name='student.show'),
    path('student_delete/<int:student_id>', student_delete, name='student.delete'),
    path('borrow_delete/<int:borrow_id>', borrow_delete, name='borrow.delete'),
    path('student_password/<int:student_id>', student_password, name='student.password'),
     path('search/', search, name='search.id'),

]