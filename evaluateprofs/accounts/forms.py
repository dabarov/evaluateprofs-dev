from django import forms
from django.contrib.auth import authenticate, get_user_model


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            if not user:
                raise forms.ValidationError('Wrong username or password.')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password.')
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')
        else:
            raise forms.ValidationError('Fill all the fields.')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        username_qs = get_user_model().objects.filter(username=username)
        email = self.cleaned_data.get('email')
        email_qs = get_user_model().objects.filter(email=email)
        password = self.cleaned_data.get('password')
        if username:
            if username_qs.exists():
                raise forms.ValidationError('Username is already taken.')
        if email:
            if not email.endswith('nu.edu.kz'):
                raise forms.ValidationError('Please register with your\
                                            univirsity email.')
            if email_qs.exists():
                raise forms.ValidationError('This email has already been\
                                            registered.')
        if password:
            if len(password) < 8:
                raise forms.ValidationError('Password should be at least 8\
                                            charecters long.')
        if not(username and email and password):
            raise forms.ValidationError('Fill all the fields.')
        return super(UserRegistrationForm, self).clean(*args, **kwargs)
