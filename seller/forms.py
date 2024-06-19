from django import forms
from users.models import Product





class AddBookForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'quantity', 'description', 'image', 'category']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        