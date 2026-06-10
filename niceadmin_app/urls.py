from django.contrib import admin
from django.urls import path,include
from niceadmin_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('accordion/',views.accordion,name="accordion"),
    path('alerts/',views.alerts,name="alerts"),
    path('badges/',views.badges,name="badges"),
    path('breadcrumbs/',views.breadcrumbs,name="breadcrumbs"),
    path('buttons/',views.buttons,name="buttons"),
    path('cards/',views.cards,name="cards"),
    path('carousel/',views.carousel,name="carousel"),
    path('listgroup/',views.listgroup,name="listgroup"),
    path('modal/',views.modal,name="modal"),
    path('tabs/',views.tabs,name="tabs"),
    path('pagination/',views.pagination,name="pagination"),
    path('progress/',views.progress,name="progress"),
    path('spinners/',views.spinners,name="spinners"),
    path('tooltips/',views.tooltips,name="tooltips"),
    path('elements/',views.elements,name="elements"),
    path('layouts/',views.layouts,name="layouts"),
    path('editors/',views.editors,name="editors"),
    path('validation/',views.validation,name="validation"),
    path('general/',views.general,name="general"),
    path('data/',views.data,name="data"),
    path('chartjs/',views.chartjs,name="chartjs"),
    path('apexcharts/',views.apexcharts,name="apexcharts"),
    path('echarts/',views.echarts,name="echarts"),
    path('profile/',views.profile,name="profile"),
    path('faq/',views.faq,name="faq"),
    path('contact/',views.contact,name="contact"),
    
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout_view/',views.logout_view,name="logout_view"),
    
    path('error/',views.error,name="error"),
    path('blank/',views.blank,name="blank"),
    path('bootstrap/',views.bootstrap,name="bootstrap"),
    path('boxicons/',views.boxicons,name="boxicons"),
    path('remix/',views.remix,name="remix"),
    
    
    
    
    path('create_student/',views.create_student,name="create_student"),
    path('list_student/',views.list_student,name="list_student"),
    path('delete_student/<int:id>/',views.delete_student,name="delete_student"),
    path('update_student/<int:id>/',views.update_student,name="update_student"),
    
    path('create_teacher/',views.create_teacher,name="create_teacher"),
    path('list_teacher/',views.list_teacher,name="list_teacher"),
    path('delete_teacher/<int:id>/',views.delete_teacher,name="delete_teacher"),
    path('update_teacher/<int:id>/',views.update_teacher,name="update_teacher"),
    
    path('create_employee/',views.create_employee,name="create_employee"),
    path('list_employee/',views.list_employee,name="list_employee"),
    path('delete_employee/<int:id>/',views.delete_employee,name="delete_employee"),
    path('update_employee/<int:id>/',views.update_employee,name="update_employee"),
    
    path('create_product/',views.create_product,name="create_product"),
    path('list_product/',views.list_product,name="list_product"),
    path('delete_product/<int:id>/',views.delete_product,name="delete_product"),
    path('update_product/<int:id>/',views.update_product,name="update_product"),
    
    path('create_customer/',views.create_customer,name="create_customer"),
    path('list_customer/',views.list_customer,name="list_customer"),
    path('delete_customer/<int:id>/',views.delete_customer,name="delete_customer"),
    path('update_customer/<int:id>/',views.update_customer,name="update_customer"),
    
    path('create_order/',views.create_order,name="create_order"),
    path('list_order/',views.list_order,name="list_order"),
    path('delete_order/<int:id>/',views.delete_order,name="delete_order"),
    path('update_order/<int:id>/',views.update_order,name="update_order"),
    
    path('create_Supplier/',views.create_Supplier,name="create_Supplier"),
    path('list_Supplier/',views.list_Supplier,name="list_Supplier"),
    path('delete_Supplier/<int:id>/',views.delete_Supplier,name="delete_Supplier"),
    path('update_Supplier/<int:id>/',views.update_Supplier,name="update_Supplier"),
    
    path('create_Vehicle/',views.create_Vehicle,name="create_Vehicle"),
    path('list_Vehicle/',views.list_Vehicle,name="list_Vehicle"),
    path('delete_Vehicle/<int:id>/',views.delete_Vehicle,name="delete_Vehicle"),
    path('update_Vehicle/<int:id>/',views.update_Vehicle,name="update_Vehicle"),
    
    path('create_LibraryBook/',views.create_LibraryBook,name="create_LibraryBook"),
    path('list_LibraryBook/',views.list_LibraryBook,name="list_LibraryBook"),
    path('delete_LibraryBook/<int:id>/',views.delete_LibraryBook,name="delete_LibraryBook"),
    path('update_LibraryBook/<int:id>/',views.update_LibraryBook,name="update_LibraryBook"),
    
    path('create_Attendance/',views.create_Attendance,name="create_Attendance"),
    path('list_Attendance/',views.list_Attendance,name="list_Attendance"),
    path('delete_Attendance/<int:id>/',views.delete_Attendance,name="delete_Attendance"),
    path('update_Attendance/<int:id>/',views.update_Attendance,name="update_Attendance"),
    
    path('create_HostelRoom/',views.create_HostelRoom,name="create_HostelRoom"),
    path('list_HostelRoom/',views.list_HostelRoom,name="list_HostelRoom"),
    path('delete_HostelRoom/<int:id>/',views.delete_HostelRoom,name="delete_HostelRoom"),
    path('update_HostelRoom/<int:id>/',views.update_HostelRoom,name="update_HostelRoom"),
    
    path('create_HostelStudent/',views.create_HostelStudent,name="create_HostelStudent"),
    path('list_HostelStudent/',views.list_HostelStudent,name="list_HostelStudent"),
    path('delete_HostelStudent/<int:id>/',views.delete_HostelStudent,name="delete_HostelStudent"),
    path('update_HostelStudent/<int:id>/',views.update_HostelStudent,name="update_HostelStudent"),
    
    path('create_Invoice/',views.create_Invoice,name="create_Invoice"),
    path('list_Invoice/',views.list_Invoice,name="list_Invoice"),
    path('delete_Invoice/<int:id>/',views.delete_Invoice,name="delete_Invoice"),
    path('update_Invoice/<int:id>/',views.update_Invoice,name="update_Invoice"),
    
    path('create_Payment/',views.create_Payment,name="create_Payment"),
    path('list_Payment/',views.list_Payment,name="list_Payment"),
    path('delete_Payment/<int:id>/',views.delete_Payment,name="delete_Payment"),
    path('update_Payment/<int:id>/',views.update_Payment,name="update_Payment"),
    
    path('create_Course/',views.create_Course,name="create_Course"),
    path('list_Course/',views.list_Course,name="list_Course"),
    path('delete_Course/<int:id>/',views.delete_Course,name="delete_Course"),
    path('update_Course/<int:id>/',views.update_Course,name="update_Course"),
    
    path('create_Enrollment/',views.create_Enrollment,name="create_Enrollment"),
    path('list_Enrollment/',views.list_Enrollment,name="list_Enrollment"),
    path('delete_Enrollment/<int:id>/',views.delete_Enrollment,name="delete_Enrollment"),
    path('update_Enrollment/<int:id>/',views.update_Enrollment,name="update_Enrollment"),
    
    path('create_Event/',views.create_Event,name="create_Event"),
    path('list_Event/',views.list_Event,name="list_Event"),
    path('delete_Event/<int:id>/',views.delete_Event,name="delete_Event"),
    path('update_Event/<int:id>/',views.update_Event,name="update_Event"),
    
    path('create_Ticket/',views.create_Ticket,name="create_Ticket"),
    path('list_Ticket/',views.list_Ticket,name="list_Ticket"),
    path('delete_Ticket/<int:id>/',views.delete_Ticket,name="delete_Ticket"),
    path('update_Ticket/<int:id>/',views.update_Ticket,name="update_Ticket"),
    
]

