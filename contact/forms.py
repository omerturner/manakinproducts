from django import forms

# our new form
class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)