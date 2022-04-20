from django.urls import path

from expenses_tracker.profiles.views import home, create_expense, edit_expense, delete_expense, profile_info, \
    edit_profile, \
    delete_profile, create_profile

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
    path('profile/', profile_info, name='profile info'),
    path('create_profile/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]