from django import forms


class Subscribe(forms.Form):
    Email = forms.EmailField()
    subject = forms.CharField()
    Email_body = forms.CharField()
    def __str__(self):
        return self.Email
