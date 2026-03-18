from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        data = self.cleaned_data
        if data.get("password") != data.get("password2"):
            raise forms.ValidationError("Password must be same")
        return data


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()