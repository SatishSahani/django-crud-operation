
from operator import index
from django.contrib import admin
from django.urls import path,include
from crudapp.views import mobile_login_view
from crudapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add/',views.add_show, name="Add"),
    path('<int:id>/',views.update_data, name="updatestudent"),
    path('delete/<int:id>', views.delete_data, name="deletedata"),
    # path('date',views.date_range_view,name='date'),
    path('', mobile_login_view, name='login'),

  
]

