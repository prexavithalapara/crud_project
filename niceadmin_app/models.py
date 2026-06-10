from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    roll = models.IntegerField()
    dob = models.DateField(null=True,blank=True)
    contact = models.IntegerField()
    
class teacher(models.Model):
    yer = models.ForeignKey(student,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField(null=True,blank=True)
    contact = models.IntegerField()
    
class employee(models.Model):
    stud = models.ForeignKey(teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    emp_code = models.IntegerField(unique=True)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    salary = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField(10)
    joining_date = models.DateField()
    status = models.CharField(max_length=255)
    
class product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.IntegerField(unique= True)
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    stock = models.IntegerField()
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='images/')
    
class customer(models.Model):
    name = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    phone = models.IntegerField(10)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    register_date = models.DateField()
    gender = models.CharField(max_length=255)
    
class order(models.Model):
    arr = models.ForeignKey(customer,on_delete=models.CASCADE)
    order_no = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    order_date = models.DateField()
    delivery_date = models.DateField()
    payment_mode = models.IntegerField()
    total_amount =models.IntegerField()
    discount = models.IntegerField()
    status = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    supplier_code = models.IntegerField()
    phone = models.IntegerField(10)
    email = models.EmailField()
    gst_no = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
class Vehicle(models.Model):
    wwww = models.ForeignKey(student,on_delete=models.CASCADE)
    xyz= models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Vehicle_no = models.IntegerField()
    model_name = models.CharField(max_length=255) 
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    registration_date = models.DateField()
    color = models.CharField(max_length=50)
    insurance_expiry = models.DateField()
    status = models.CharField(max_length=255)
    
class LibraryBook(models.Model):
    abc = models.ForeignKey(student,on_delete=models.CASCADE)
    title = models.CharField(max_length=255) 
    isbn = models.IntegerField()
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    edition = models.IntegerField()
    pages = models.IntegerField()
    category = models.IntegerField()
    stock = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
    
    
class Attendance(models.Model):
    xyz = models.ForeignKey(teacher,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    lecture_no = models.IntegerField()
    remarks = models.CharField(max_length=255)
    teacher_name =models.CharField(max_length=255)
    attendance_code = models.IntegerField()
    type = models.CharField(max_length=255)
    
class HostelRoom(models.Model):
    xyz = models.ForeignKey(teacher,on_delete=models.CASCADE)
    room_no = models.IntegerField()
    block = models.CharField(max_length=255)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    room_type =models.BooleanField()
    price = models.IntegerField()
    availability = models.BooleanField()
    status = models.BooleanField()
    
class HostelStudent(models.Model):
    name = models.CharField(max_length=255)
    room_no = models.IntegerField()
    join_date = models.DateField()
    phone = models.IntegerField()
    guardian_name = models.CharField(max_length=255)
    address = models.CharField()
    id_proof = models.BooleanField()
    fees_paid = models.BooleanField()
    gender = models.BooleanField()
    
class Invoice(models.Model):
    stud = models.ForeignKey(HostelStudent,on_delete=models.CASCADE)
    invoice_no = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.IntegerField()
    gst = models.IntegerField()
    discount = models.IntegerField()
    net_amount = models.IntegerField()
    payment_mode = models.BooleanField()
    status =  models.BooleanField()
 
class Payment(models.Model):
    payment_id = models.IntegerField()
    payer_name = models.CharField(max_length=255)
    mode = models.BooleanField()
    date = models.DateField()
    amount = models.IntegerField()
    reference_no = models.IntegerField() 
    status = models.BooleanField()
    note = models.CharField(max_length=255)
    verified = models.BooleanField()
    
class Course(models.Model):
    abc = models.ForeignKey(teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    fees = models.IntegerField() 
    syllabus = models.CharField(max_length=255)
    created_date = models.DateField()
    update_date = models.DateField()
    active_status =models.BooleanField()
    level = models.BooleanField()
    
class Enrollment(models.Model):
    wwww = models.ForeignKey(student,on_delete=models.CASCADE)
    enrollment_no = models.IntegerField()
    student_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    batch = models.CharField(max_length=255)
    join_date = models.DateField()
    status = models.BooleanField()
    payment_status = models.BooleanField()
    remark = models.CharField(max_length=255)
    mode = models.BooleanField()   
    
class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    capacity = models.IntegerField()
    registration_required = models.BooleanField()
    status = models.BooleanField()
    
class Ticket(models.Model):
    kkk = models.ForeignKey(Event,on_delete=models.CASCADE)
    ticket_no = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.BooleanField()
    status = models.CharField(max_length=255)
    created_date = models.DateField()
    updated_date = models.DateField()
    assigned_to = models.CharField(max_length=255)
    type = models.BooleanField()
