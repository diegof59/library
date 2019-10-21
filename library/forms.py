from django import forms

class ContactoForm(forms.Form):

    asunto = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)

    # Validación de que el contenido del mensaje sea de al menos 3 palabras.
    def clean_mensaje(self):

        msj = self.cleaned_data['mensaje']

        cant_palabras = len(msj.split())

        if cant_palabras < 3:
            raise forms.ValidationError('Mínimo 3 palabras.')

        return msj
