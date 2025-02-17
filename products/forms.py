from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, data = ..., files = ..., auto_id = ..., prefix = ..., initial = ..., error_class = ..., label_suffix = ..., empty_permitted = ..., instance = ..., use_required_attribute = ..., renderer = ...):
        super().__init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in Categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.item():
            field.widget.attrs['class'] = 'border-black rounded-0'