# coding=utf-8
from django import forms
from taggit_labels.widgets import LabelWidget
from taggit.forms import TagField
from .models import Newsletter
from django.contrib.auth.models import User

class ArticleAdminForm(forms.ModelForm):
   tags = TagField(required=False, widget=LabelWidget)

   # def __init__(self, *args, **kwargs):
   #     super(ArticleAdminForm, self).__init__(*args, **kwargs)
   #     self.fields['image'].required = False

class NewsletterForm(forms.ModelForm):

    class Meta:
      model = Newsletter
      fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs \
            .update({
            'placeholder': 'Κωδικός Χρήστη',
        })
        self.fields['password'].widget.attrs \
            .update({
            'placeholder': '******',
        })

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                              widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                               widget=forms.PasswordInput)
    email = forms.CharField(max_length=75, required=True)
    val = forms.CharField(label='Πόσο κάνει πέντε συν τέσσερα; ')


    class Meta:
       model = User
       fields = ('username', 'first_name', 'email',)


    def clean_password2(self):
       cd = self.cleaned_data
       if cd['password'] != cd['password2']:
           raise forms.ValidationError('Passwords don\'t match.')
       return cd['password2']
    def clean_val(self):
        cd=self.cleaned_data
        if cd['val'] != '9':
            raise forms.ValidationError('Λάθος αριθμός.')
        return cd['val']


class UserEditForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ('first_name', 'last_name', 'email')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)
    
