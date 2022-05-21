from email.policy import default
from django import forms
from .models import Product
from colorfield import fields


class ProductForm(forms.ModelForm):

    size_choices = [
        ('small', 'S'),
        ('medium', 'M'),
        ('large', 'XL'),
        ('extra_large', 'XXL')
    ]

    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['color', 'size']

    size = forms.ChoiceField(choices=size_choices)
    color = fields.ColorField(choices=COLOR_PALETTE, format='hexa', default='#FF0000', null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})