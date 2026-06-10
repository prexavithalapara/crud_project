from django import forms
from niceadmin_app import models

class student_form(forms.ModelForm):
    class Meta:
        model = models.student
        fields = '__all__'
        
class teacher_form(forms.ModelForm):
    class Meta:
        model = models.teacher
        fields = '__all__'
        
class employee_form(forms.ModelForm):
    class Meta:
        model = models.employee
        fields = '__all__'    
        
class product_form(forms.ModelForm):
    class Meta:
        model = models.product
        fields = '__all__'   
        
class customer_form(forms.ModelForm):
    class Meta:
        model = models.customer
        fields = '__all__'   
        
class order_form(forms.ModelForm):
    class Meta:
        model = models.order
        fields = '__all__'   
        
class Supplier_form(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = '__all__'  
        
class Vehicle_form(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = '__all__'     
        
class LibraryBook_form(forms.ModelForm):
    class Meta:
        model = models.LibraryBook
        fields = '__all__'     
        
class Attendance_form(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = '__all__'     
        
class HostelRoom_form(forms.ModelForm):
    class Meta:
        model = models.HostelRoom
        fields = '__all__'     
        
class HostelStudent_form(forms.ModelForm):
    class Meta:
        model = models.HostelStudent
        fields = '__all__'  
        
class Invoice_form(forms.ModelForm):
    class Meta:
        model = models.Invoice
        fields = '__all__'  
        
class Payment_form(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = '__all__'
        
class Course_form(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__' 
        
class Enrollment_form(forms.ModelForm):
    class Meta:
        model = models.Enrollment
        fields = '__all__' 
        
class Event_form(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__' 
        
class Ticket_form(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = '__all__' 