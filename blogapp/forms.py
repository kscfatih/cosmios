from django import forms
from .models import *

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, label='Kategori Adı', widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active = forms.BooleanField(label='Aktif mi ?')

class CategoryModelForm(forms.ModelForm):
    class Meta:
        models = Category
        fields = ['name','is_active']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','is_active','category','image']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'id':'title'
            }),
            'content':forms.Textarea(attrs={
                'class':'form-control'
            }),
            'is_active':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            }),
            'category':forms.SelectMultiple(attrs={
                'class':'form-select'
            }),
            'image':forms.FileInput(attrs={
                'class':'form-control'
            })
        }