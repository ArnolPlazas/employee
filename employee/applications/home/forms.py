from django import forms

from .models import Test

class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('title', 'subtitle', 'amount')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'type the title',
                }
            )
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 10:
            raise forms.ValidationError('Type the amount greater than 10')
        return amount

