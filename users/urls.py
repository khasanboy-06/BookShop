from django.urls import path
from .views import HomeView, ProductDetailView, CartDeteailView, delete_from_cart, CategoryView, LoginView, RegisterView, LogoutView, Profile, EditProfileView, AdminDashboardView, UsersView, UsersEditView, BooksView, delete_users

app_name = 'users'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:product_id>/', delete_from_cart, name='delete'),
    path('cart-detail/', CartDeteailView.as_view(), name='cart_detail'),
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('edit-profile/<int:id>/', EditProfileView.as_view(), name='edit_profile'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('users/', UsersView.as_view(), name='users'),
    path('edit-users/<int:id>/', UsersEditView.as_view(), name='edit_users'),
    path('books/', BooksView.as_view(), name='books'),
    path('delete-users/<int:id>/', delete_users, name='delete_users'),
]