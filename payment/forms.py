from django import forms
from .models import Account


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('bank_name', 'account_name', 'account_number', )