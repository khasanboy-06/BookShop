from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.permissions import SellerRequiredMixin
from users.models import Product
from .forms import AddBookForm



class BooksView(SellerRequiredMixin, View):
    def get(self, request):
        books = Product.objects.all()
        return render(request, 'seller/books.html', context={"books":books})
    
class CreateBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'seller/add_book.html', context={"form":form})
    
    def post(self, request):
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:home')
        return render(request, 'seller/add_book.html', {'form': form})
    
def delete_book(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('users:home')


class EditBookView(SellerRequiredMixin, View):
    def get(self, request, product_id):
        book = get_object_or_404(Product, id=product_id)
        form = AddBookForm(instance=book)
        return render(request, 'seller/add_book.html', {'form': form})
    
    def post(self, request, product_id):
        book = get_object_or_404(Product, id=product_id)
        form = AddBookForm(instance=book)
        if request.method == 'POST':
            form = AddBookForm(request.POST, request.FILES, instance=book)  
            if form.is_valid():
                form.save()
                return redirect('users:home')

        return render(request, 'seller/add_book.html', context={'form':form})