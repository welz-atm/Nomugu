from django import forms
from .models import Account


Banks = (
    ('Choose Bank', 'Choose Bank'),
    ('Access Bank', 'Access Bank'),
    ('Citibank', 'Citibank'),
    ('Diamond Bank', 'Diamond Bank'),
    ('Ecobank Nigeria', 'Ecobank Nigeria'),
    ('Fidelity Bank Nigeria', 'Fidelity Bank Nigeria'),
    ('First Bank of Nigeria', 'First Bank of Nigeria'),
    ('First City Monument Bank', 'First City Monument Bank'),
    ('Guaranty Trust Bank', 'Guaranty Trust Bank'),
    ('Heritage Bank Plc', 'Heritage Bank Plc'),
    ('Jaiz Bank', 'Jaiz Bank'),
    ('Keystone Bank Limited', 'Keystone Bank Limited'),
    ('Providus Bank Plc', 'Providus Bank Plc'),
    ('Polaris Bank', 'Polaris Bank'),
    ('Stanbic IBTC Bank Nigeria Limited', 'Stanbic IBTC Bank Nigeria Limited'),
    ('Standard Bank', 'Standard Bank'),
    ('Standard Chartered Bank', 'Standard Chartered Bank'),
    ('Sterling Bank', 'Sterling Bank'),
    ('Suntrust Bank Nigeria Limited', 'Suntrust Bank Nigeria Limited'),
    ('Union Bank of Nigeria', 'Union Bank of Nigeria'),
    ('United Bank for Africa', 'United Bank for Africa'),
    ('Unity Bank Plc', 'Unity Bank Plc'),
    ('Wema Bank', 'Wema Bank'),
    ('Zenith Bank', 'Zenith Bank')
)


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('bank_name', 'account_name', 'account_number', )


class ShopperAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('employer', 'employer_address', 'job_role', 'salary', 'bank_name', 'account_name', 'account_number', )