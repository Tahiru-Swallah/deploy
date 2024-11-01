from django import forms
from .models import Category, Product

""" class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
 """
class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={"Placeholder": 'Find product or user'}))

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Product description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Product price'}))
    image = forms.ImageField(label='image_field')
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select category'
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'description',
            'price',
            'category',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        product = super().save(commit=False)
        print("User:", self.user) 
        
        if self.user:
            product.user = self.user
            print('User:', product.user)
        if commit:
            product.save()
        return product
    
class EditProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Product description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Product price'}))
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select category'
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'description',
            'price',
            'category',
        ]