from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Cart, Category, Client, User, Seller
from .forms import LoginForm, RegisterForm, ProfileForm, UsersEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdminRequiredMixin

class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(in_stock=True)
        cart = Cart.objects.count()
        categories = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'users/home.html', context={"products":products, "cart":cart, "categories":categories})
    
class CategoryView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        products = category.product.all()
        categories = Category.objects.all()
        return render(request, 'users/home.html', context={"products":products, "categories":categories})

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.count()
        return render(request, 'users/detail.html', context={"product":product, "cart":cart})
    

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.product = product
            cart.quantity = quantity
            cart.save()
        return redirect('users:home')
    
class CartDeteailView(View):
    def get(self, request):
        products = Cart.objects.all()
        return render(request, 'users/cart_detail.html', context={"products":products})
    

def delete_from_cart(request, product_id):
    cart = get_object_or_404(Cart, id=product_id)
    cart.delete()
    return redirect('users:home')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role == 'admin':
                    return redirect('users:home')
                elif user.user_role == 'client':
                    return redirect('users:home')
                elif user.user_role == 'seller':
                    return redirect('users:home')
        

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'client':
                new_client = Client()
                new_client.user = user
                new_client.save()

            return redirect('/')
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')
    

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/') 
        return render(request, 'users/edit_profile.html', {'form': form})
    
class AdminDashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/admin_dashboard.html')
    
class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/users.html', context={"users":users})
    
class UsersEditView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UsersEditForm(instance=user)
        return render(request, 'users/edit_users.html', {'form': form})
    
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UsersEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:users') 
        return render(request, 'users/edit_users.html', {'form': form})
    

class BooksView(View):
    def get(self, request):
        books = Product.objects.all()
        return render(request, 'users/books.html', context={"books":books})
    
def delete_users(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users:users')


