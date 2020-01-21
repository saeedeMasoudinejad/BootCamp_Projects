from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    email = forms.EmailField()
    mobile = forms.IntegerField()
    # birth_date = forms.DateField()


