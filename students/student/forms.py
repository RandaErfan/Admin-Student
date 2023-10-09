from django import forms
from .models import Book, Student

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    age = forms.IntegerField(label="Age", required=False)
    image=forms.ImageField(label='Image',required=False)
    email = forms.EmailField(label="Email", max_length=200, required=False)
    book_id = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book", required=False)
    password = forms.CharField(label='Password',max_length=50)
    password2 = forms.CharField(label='Confirm Password',max_length=50)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")

        return email

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']

        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")

        return email


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['username', 'email']


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



class PasswordModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['email','password','password2']

    def strong_password(self):
        if password == password2:
            if len(password) < 8:
                raise forms.ValidationError('Try to type a Strong password at least 8 charcters')
        else:
            raise forms.ValidationError('the confirm password not equal the password')

        return password



