from django import forms
from .models import Ticket, TicketFeedback


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ticket title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your problem'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }


class TicketFeedbackForm(forms.ModelForm):
    class Meta:
        model = TicketFeedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your feedback'}),
        }
