from django.shortcuts import render,redirect
from django.http import HttpResponse
from niceadmin_app import forms
from niceadmin_app import models

# Create your views here.
def index(request):
    return render(request,'index.html')

def accordion(request):
    return render(request,'components-accordion.html')

def alerts(request):
    return render(request,'components-alerts.html')

def badges(request):
    return render(request,'components-badges.html')

def breadcrumbs(request):
    return render(request,'components-breadcrumbs.html')

def buttons(request):
    return render(request,'components-buttons.html')

def cards(request):
    return render(request,'components-cards.html')

def carousel(request):
    return render(request,'components-carousel.html')

def listgroup(request):
    return render(request,'components-list-group.html')

def modal(request):
    return render(request,'components-modal.html')

def tabs(request):
    return render(request,'components-tabs.html')

def pagination(request):
    return render(request,'components-pagination.html')

def progress(request):
    return render(request,'components-progress.html')

def spinners(request):
    return render(request,'components-spinners.html')

def tooltips(request):
    return render(request,'components-tooltips.html')

def elements(request):
    return render(request,'forms-elements.html')

def layouts(request):
    return render(request,'forms-layouts.html')

def editors(request):
    return render(request,'forms-editors.html')

def validation(request):
    return render(request,'forms-validation.html')

def general(request):
    return render(request,'tables-general.html')

def data(request):
    return render(request,'tables-data.html')

def chartjs(request):
    return render(request,'charts-chartjs.html')

def apexcharts(request):
    return render(request,'charts-apexcharts.html')
    
def echarts(request):
    return render(request,'charts-echarts.html')

def profile(request):
    return render(request,'users-profile.html')

def faq(request):
    return render(request,'pages-faq.html')

def contact(request):
    return render(request,'pages-contact.html')

from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            return HttpResponse("User does not exist")
    return render(request,'pages-login.html')

from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            try:
                User.objects.get(username=username)
                return HttpResponse("Username Alredy Exists Please Try Again")
            except:
                User.objects.create_user(username=username,password=password)
                return redirect(login_view)
        else:
            return HttpResponse("Password Do Not Match!!")
    return render(request,'pages-register.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)

def error(request):
    return render(request,'pages-error-404.html')

def blank(request):
    return render(request,'pages-blank.html')

def bootstrap(request):
    return render(request,'icons-bootstrap.html')

def boxicons(request):
    return render(request,'icons-boxicons.html')

def remix(request):
    return render(request,'icons-remix.html')

# ------------------------------------------ STUDENT CRUD ----------------------------------------------------

def create_student(request):
    if request.method == 'POST':
        form = forms.student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_student)
        else:   
            print(form.errors)
    return render(request,'create_student.html')

def list_student(request):
    stud = models.student.objects.all()
    context = {'stud':stud}
    return render(request,'list_student.html',context)

def update_student(request,id):
    stud = models.student.objects.get(id=id)
    if request.method == 'POST':
        form = forms.student_form(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect(list_student)
        else:
            print(form.errors)
    context = {'stud':stud}
    return render(request,'update_student.html',context)

def delete_student(request,id):
    tic = models.student.objects.get(id=id)
    tic.delete()
    return redirect(list_student)
# ------------------------------------------ TEACHER CRUD ----------------------------------------------------

def create_teacher(request):
    stud = models.student.objects.all()
    if request.method == 'POST':
        form = forms.teacher_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_teacher)
        else:
            print(form.errors)
    context = {'stud':stud}
    return render(request,'create_teacher.html',context)

def list_teacher(request):
    teacher = models.teacher.objects.all()
    context = {'teacher':teacher}
    return render(request,'list_teacher.html',context)

def delete_teacher(request,id):
    tic = models.teacher.objects.get(id=id)
    tic.delete()
    return redirect(list_teacher)

def update_teacher(request,id):
    teacher = models.teacher.objects.get(id=id)
    if request.method == 'POST':
        form = forms.teacher_form(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(list_teacher)
        else:
            print(form.errors)
    context = {'teacher':teacher}
    return render(request,'update_teacher.html',context)


# ------------------------------------------ EMPLOYEE CRUD ----------------------------------------------------

def create_employee(request):
    teach = models.teacher.objects.all()
    if request.method == 'POST':
        form = forms.employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_employee)
        else:
            print(form.errors)
    context = {'teach':teach}
    return render(request,'create_employee.html',context)

def list_employee(request):
    emp = models.employee.objects.all()
    context = {'emp':emp}
    return render(request,'list_employee.html',context)

def delete_employee(request,id):
    tic = models.employee.objects.get(id=id)
    tic.delete()
    return redirect(list_employee)

def update_employee(request,id):
    employee = models.employee.objects.get(id=id)
    if request.method == 'POST':
        form = forms.employee_form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect(list_employee)
        else:
            print(form.errors)
    context = {'employee':employee}
    return render(request,'update_employee.html',context)


# ------------------------------------------ PRODUCT CRUD ----------------------------------------------------

def create_product(request):
    
    if request.method == 'POST':
        form = forms.product_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_product)
        else:
            print(form.errors)
    return render(request,'create_product.html')

def list_product(request):
    product = models.product.objects.all()
    context = {'product':product}
    return render(request,'list_product.html',context)

def delete_product(request,id):
    tic = models.product.objects.get(id=id)
    tic.delete()
    return redirect(list_product)

def update_product(request,id):
    product = models.product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.product_form(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect(list_product)
        else:
            print(form.errors)
    context = {'product':product}
    return render(request,'update_product.html',context)

# ------------------------------------------ CUSTOMER CRUD ----------------------------------------------------

def create_customer(request):
    if request.method == 'POST':
        form = forms.customer_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_customer)
        else:
            print(form.errors)
    return render(request,'create_customer.html')

def list_customer(request):
    customer = models.customer.objects.all()
    context = {'customer':customer}
    return render(request,'list_customer.html',context)

def delete_customer(request,id):
    tic = models.customer.objects.get(id=id)
    tic.delete()
    return redirect(list_customer)

def update_customer(request,id):
    customer = models.customer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.customer_form(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(list_customer)
        else:
            print(form.errors)
    context = {'customer':customer}
    return render(request,'update_customer.html',context)


# ------------------------------------------ ORDER CRUD ----------------------------------------------------

def create_order(request):
    cust = models.customer.objects.all()
    if request.method == 'POST':
        form = forms.order_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_order)
        else:
            print(form.errors)
    context = {'cust':cust}
    return render(request,'create_order.html',context)

def list_order(request):
    order = models.order.objects.all()
    context = {'order':order}
    return render(request,'list_order.html',context)

def delete_order(request,id):
    tic = models.order.objects.get(id=id)
    tic.delete()
    return redirect(list_order)

def update_order(request,id):
    order = models.order.objects.get(id=id)
    if request.method == 'POST':
        form = forms.order_form(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect(list_order)
        else:
            print(form.errors)
    context = {'order':order}
    return render(request,'update_order.html',context)


# ------------------------------------------ SUPPLIER CRUD ----------------------------------------------------

def create_Supplier(request):
    if request.method == 'POST':
        form = forms.Supplier_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Supplier)
        else:
            print(form.errors)
    return render(request,'create_Supplier.html')

def list_Supplier(request):
    Supplier = models.Supplier.objects.all()
    context = {'Supplier':Supplier}
    return render(request,'list_Supplier.html',context)

def delete_Supplier(request,id):
    tic = models.Supplier.objects.get(id=id)
    tic.delete()
    return redirect(list_Supplier)

def update_Supplier(request,id):
    Supplier = models.Supplier.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Supplier_form(request.POST,instance=Supplier)
        if form.is_valid():
            form.save()
            return redirect(list_Supplier)
        else:
            print(form.errors)
    context = {'Supplier':Supplier}
    return render(request,'update_Supplier.html',context)


# ------------------------------------------ VEHICLE CRUD ----------------------------------------------------

def create_Vehicle(request):
    stud = models.student.objects.all()
    spr = models.Supplier.objects.all()
    if request.method == 'POST':
        form = forms.Vehicle_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Vehicle)
        else:
            print(form.errors)
    context = {'spr':spr,'stud':stud}
    return render(request,'create_Vehicle.html',context)

def list_Vehicle(request):
    Vehicle = models.Vehicle.objects.all()
    context = {'Vehicle':Vehicle}
    return render(request,'list_Vehicle.html',context)

def delete_Vehicle(request,id):
    tic = models.Vehicle.objects.get(id=id)
    tic.delete()
    return redirect(list_Vehicle)

def update_Vehicle(request,id):
    Vehicle = models.Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Supplier_form(request.POST,instance=Vehicle)
        if form.is_valid():
            form.save()
            return redirect(list_Vehicle)
        else:
            print(form.errors)
    context = {'Vehicle':Vehicle}
    return render(request,'update_Vehicle.html',context)


# ------------------------------------------ LIBRARYBOOK CRUD ----------------------------------------------------

def create_LibraryBook(request):
    stud = models.student.objects.all()
    if request.method == 'POST':
        form = forms.LibraryBook_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_LibraryBook)
        else:
            print(form.errors)
    context = {'stud':stud}
    return render(request,'create_LibraryBook.html',context)

def list_LibraryBook(request):
    LibraryBook = models.LibraryBook.objects.all()
    context = {'LibraryBook':LibraryBook}
    return render(request,'list_LibraryBook.html',context)

def delete_LibraryBook(request,id):
    tic = models.LibraryBook.objects.get(id=id)
    tic.delete()
    return redirect(list_LibraryBook)

def update_LibraryBook(request,id):
    LibraryBook = models.LibraryBook.objects.get(id=id)
    if request.method == 'POST':
        form = forms.LibraryBook_form(request.POST,instance=LibraryBook)
        if form.is_valid():
            form.save()
            return redirect(list_LibraryBook)
        else:
            print(form.errors)
    context = {'LibraryBook':LibraryBook}
    return render(request,'update_LibraryBook.html',context)


# ------------------------------------------ ATTENDANCE CRUD ----------------------------------------------------

def create_Attendance(request):
    teach = models.teacher.objects.all()
    if request.method == 'POST':
        form = forms.Attendance_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Attendance)
        else:
            print(form.errors)
    context = {'teach':teach}
    return render(request,'create_Attendance.html',context)

def list_Attendance(request):
    Attendance = models.Attendance.objects.all()
    context = {'Attendance':Attendance}
    return render(request,'list_Attendance.html',context)

def delete_Attendance(request,id):
    tic = models.Attendance.objects.get(id=id)
    tic.delete()
    return redirect(list_Attendance)

def update_Attendance(request,id):
    Attendance = models.Attendance.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Attendance_form(request.POST,instance=Attendance)
        if form.is_valid():
            form.save()
            return redirect(list_Attendance)
        else:
            print(form.errors)
    context = {'Attendance':Attendance}
    return render(request,'update_Attendance.html',context)


# ------------------------------------------ HOSTELROOM CRUD ----------------------------------------------------

def create_HostelRoom(request):
    teach = models.teacher.objects.all()
    if request.method == 'POST':
        form = forms.HostelRoom_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_HostelRoom)
        else:
            print(form.errors)
    context = {'teach':teach}
    return render(request,'create_HostelRoom.html',context)

def list_HostelRoom(request):
    HostelRoom = models.HostelRoom.objects.all()
    context = {'HostelRoom':HostelRoom}
    return render(request,'list_HostelRoom.html',context)

def delete_HostelRoom(request,id):
    tic = models.HostelRoom.objects.get(id=id)
    tic.delete()
    return redirect(list_HostelRoom)

def update_HostelRoom(request,id):
    HostelRoom = models.HostelRoom.objects.get(id=id)
    if request.method == 'POST':
        form = forms.HostelRoom_form(request.POST,instance=HostelRoom)
        if form.is_valid():
            form.save()
            return redirect(list_HostelRoom)
        else:
            print(form.errors)
    context = {'HostelRoom':HostelRoom}
    return render(request,'update_HostelRoom.html',context)


# ------------------------------------------ HOSTELSTUDENT CRUD ----------------------------------------------------

def create_HostelStudent(request):
    if request.method == 'POST':
        form = forms.HostelStudent_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_HostelStudent)
        else:
            print(form.errors)
    return render(request,'create_HostelStudent.html')

def list_HostelStudent(request):
    HostelStudent = models.HostelStudent.objects.all()
    context = {'HostelStudent':HostelStudent}
    return render(request,'list_HostelStudent.html',context)

def delete_HostelStudent(request,id):
    tic = models.HostelStudent.objects.get(id=id)
    tic.delete()
    return redirect(list_HostelStudent)

def update_HostelStudent(request,id):
    HostelStudent = models.HostelStudent.objects.get(id=id)
    if request.method == 'POST':
        form = forms.HostelStudent_form(request.POST,instance=HostelStudent)
        if form.is_valid():
            form.save()
            return redirect(list_HostelStudent)
        else:
            print(form.errors)
    context = {'HostelStudent':HostelStudent}
    return render(request,'update_HostelStudent.html',context)


# ------------------------------------------ INVOICE CRUD ----------------------------------------------------

def create_Invoice(request):
    hs = models.HostelStudent.objects.all()
    if request.method == 'POST':
        form = forms.Invoice_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Invoice)
        else:
            print(form.errors)
    context = {'hs':hs}
    return render(request,'create_Invoice.html',context)

def list_Invoice(request):
    Invoice = models.Invoice.objects.all()
    context = {'Invoice':Invoice}
    return render(request,'list_Invoice.html',context)

def delete_Invoice(request,id):
    tic = models.Invoice.objects.get(id=id)
    tic.delete()
    return redirect(list_Invoice)

def update_Invoice(request,id):
    Invoice = models.Invoice.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Invoice_form(request.POST,instance=Invoice)
        if form.is_valid():
            form.save()
            return redirect(list_Invoice)
        else:
            print(form.errors)
    context = {'Invoice':Invoice}
    return render(request,'update_Invoice.html',context)


# ------------------------------------------ PAYMENT CRUD ----------------------------------------------------

def create_Payment(request):
    if request.method == 'POST':
        form = forms.Payment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Payment)
        else:
            print(form.errors)
    return render(request,'create_Payment.html')

def list_Payment(request):
    Payment = models.Payment.objects.all()
    context = {'Payment':Payment}
    return render(request,'list_Payment.html',context)

def delete_Payment(request,id):
    tic = models.Payment.objects.get(id=id)
    tic.delete()
    return redirect(list_Payment)

def update_Payment(request,id):
    Payment = models.Payment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Payment_form(request.POST,instance=Payment)
        if form.is_valid():
            form.save()
            return redirect(list_Payment)
        else:
            print(form.errors)
    context = {'Payment':Payment}
    return render(request,'update_Payment.html',context)


# ------------------------------------------ COURSE CRUD ----------------------------------------------------

def create_Course(request):
    teach = models.teacher.objects.all()
    if request.method == 'POST':
        form = forms.Course_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Course)
        else:
            print(form.errors)
    context = {'teach':teach}
    return render(request,'create_Course.html',context)

def list_Course(request):
    Course = models.Course.objects.all()
    context = {'Course':Course}
    return render(request,'list_Course.html',context)

def delete_Course(request,id):
    tic = models.Course.objects.get(id=id)
    tic.delete()
    return redirect(list_Course)

def update_Course(request,id):
    Course = models.Course.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Course_form(request.POST,instance=Course)
        if form.is_valid():
            form.save()
            return redirect(list_Course)
        else:
            print(form.errors)
    context = {'Course':Course}
    return render(request,'update_Course.html',context)


# ------------------------------------------ ENROLLMENT CRUD ----------------------------------------------------

def create_Enrollment(request):
    stud = models.student.objects.all()
    if request.method == 'POST':
        form = forms.Enrollment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Enrollment)
        else:
            print(form.errors)
    context = {'stud':stud}
    return render(request,'create_Enrollment.html',context)

def list_Enrollment(request):
    Enrollment = models.Enrollment.objects.all()
    context = {'Enrollment':Enrollment}
    return render(request,'list_Enrollment.html',context)

def delete_Enrollment(request,id):
    tic = models.Enrollment.objects.get(id=id)
    tic.delete()
    return redirect(list_Enrollment)

def update_Enrollment(request,id):
    Enrollment = models.Enrollment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Enrollment_form(request.POST,instance=Enrollment)
        if form.is_valid():
            form.save()
            return redirect(list_Enrollment)
        else:
            print(form.errors)
    context = {'Enrollment':Enrollment}
    return render(request,'update_Enrollment.html',context)


# ------------------------------------------ EVENT CRUD ----------------------------------------------------

def create_Event(request):
    if request.method == 'POST':
        form = forms.Event_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Event)
        else:
            print(form.errors)
    return render(request,'create_Event.html')

def list_Event(request):
    Event = models.Event.objects.all()
    context = {'Event':Event}
    return render(request,'list_Event.html',context)

def delete_Event(request,id):
    tic = models.Event.objects.get(id=id)
    tic.delete()
    return redirect(list_Event)

def update_Event(request,id):
    Event = models.Event.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Event_form(request.POST,instance=Event)
        if form.is_valid():
            form.save()
            return redirect(list_Event)
        else:
            print(form.errors)
    context = {'Event':Event}
    return render(request,'update_Event.html',context)


# ------------------------------------------ EVENT CRUD ----------------------------------------------------
def create_Ticket(request):
    eve = models.Event.objects.all()
    if request.method == 'POST':
        form = forms.Ticket_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_Ticket)
        else:
            print(form.errors)
    context = {'eve':eve}
    return render(request,'create_Ticket.html',context)

def list_Ticket(request):
    Ticket = models.Ticket.objects.all()
    context = {'Ticket':Ticket}
    return render(request,'list_Ticket.html',context)

def delete_Ticket(request,id):
    tic = models.Ticket.objects.get(id=id)
    tic.delete()
    return redirect(list_Ticket)

def update_Ticket(request,id):
    Ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Ticket_form(request.POST,instance=Ticket)
        if form.is_valid():
            form.save()
            return redirect(list_Ticket)
        else:
            print(form.errors)
    context = {'Ticket':Ticket}
    return render(request,'update_Ticket.html',context)
