from django import forms
from .models import Item, ItemReview

PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('P', 'PayPal')
)

COUNTRY_CHOICES = {
    ('U','Uganda'),
    ('K','Kenya'),
    ('T','Tanzania'),
    ('R','Rwanda')
}

class CheckoutForm(forms.Form): 
    phone_number = forms.FloatField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone number',
        'class':'form-control'
    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Street address',
        'class':'form-control', 
        'id':'add1'
    }))
    ZIP = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ZIP Code',
        'class':"form-control"
    }))
    home_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Home Address',
        'class':'form-control'
    }))
    country = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Country',
        'class':'form-control'
    }))
    save_info = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput,required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class SearchForm(forms.ModelForm):
    category = forms.ChoiceField(widget=forms.RadioSelect, choices = Item.Stuff)
    

    class Meta:
        model = Item
        fields = ['category','brand','color']

class ItemReviewForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    phone_number = forms.FloatField()
    review = forms.CharField()

    