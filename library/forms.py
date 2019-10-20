from django import forms

class ContactoForm(forms.Form):

    asunto = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)