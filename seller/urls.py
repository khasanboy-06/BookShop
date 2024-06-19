from django.urls import path
from .views import BooksView, CreateBookView, delete_book, EditBookView

app_name = 'seller'

urlpatterns = [
    path('books/', BooksView.as_view(), name='books'),
    path('add-book/', CreateBookView.as_view(), name='add_book'),
    path('delete-book/<int:product_id>/', delete_book, name='delete_book'),
    path('edit-book/<int:product_id>/', EditBookView.as_view(), name='edit_book'),
]