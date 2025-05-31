from django import forms
from .models import WebsiteOrderFormRequest, TelegramBotOrderFormRequest
from django.utils.translation import gettext as _


class WebsiteOrderForm(forms.ModelForm):
    class Meta:
        model = WebsiteOrderFormRequest
        fields = ['title', 'description', 'design_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 5}),
            'design_type': forms.Select(attrs={'class': 'form-control form-control-lg select-glass'}),
        }
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'design_type': _('Design Type'),
        }

    def clean(self):
        cleaned_data = super().clean()
        design_type = cleaned_data.get('design_type')

        if design_type == "Choose an option":
            self.add_error('design_type', _('Please select a design type.'))
        return cleaned_data


class TelegramBotOrderForm(forms.ModelForm):
    class Meta:
        model = TelegramBotOrderFormRequest
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            "description": forms.Textarea(attrs={'class': 'form-control form-control-lg', 'row': 5}),
        }
        labels = {
            'title': _('Title'),
            'description': _('Description'),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data