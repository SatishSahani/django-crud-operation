
from operator import index
from django.contrib import admin
from django.urls import path,include
from crudapp.views import login_view
from crudapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add/',views.add_show, name="addandshow"),
    path('<int:id>/',views.update_data, name="updatestudent"),
    path('delete/<int:id>', views.delete_data, name="deletedata"),
    # path('date',views.date_range_view,name='date'),
    path('', login_view, name='login'),

  
]

