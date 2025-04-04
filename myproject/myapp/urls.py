from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index1',views.index1,name='index1'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('logout2',views.logout2,name='logout2'),
    path('gallery',views.gallery,name='gallery'),
    path('packages',views.packages,name='packages'),
    path('goa',views.goa,name='goa'),
    path('kerala',views.kerala,name='kerala'),
    path('all_over',views.all_over,name='all_over'),
    path('tamilnadu',views.tamilnadu,name='tamilnadu'),
    path('manali',views.manali,name='manali'),
    path('agra',views.agra,name='agra'),
    path('bookings/<int:id>/',views.booked,name='bookings'),
    path('success_page/<int:id>/',views.success_page,name='success_page'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard_package',views.dashboard_packages,name='dashboard_package'),
    path('dashboard_booking',views.dashboard_bookings,name='dashboard_booking'),
    path('user_information',views.user_information,name='user_information'),
]