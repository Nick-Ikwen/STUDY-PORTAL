from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from . models import *

# Form class for the NOTES section
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "description"]


# The following are class forms for the HOMEWORK section
class DateInput(forms.DateInput):
    input_type = "date"


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {"due":DateInput()}
        fields = ["subject", "title", "description", "due", "is_finished"]


# Common form class for Web Search
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=500, label="Enter search text: ")


# Form class for the TO-DO section
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "is_finished"]


# Form class for WIKI section
class WikiForm(forms.Form):
    text = forms.CharField(max_length=500, label="Enter text without any space! ")


# Form class for CONVERSION section
class ConversionForm(forms.Form):
    CHOICES = [("length", "Length"), ("mass", "Mass")]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


# Length Conversion form class
class ConversionLengthForm(forms.Form):
    CHOICES = [("yard", "Yard"), ("foot", "Foot")]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs = {
            "type":"number",
            "placeholder":"Enter the Number"
        }
    ))
    measure1 = forms.CharField(
        label="",
        widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label="",
        widget=forms.Select(choices=CHOICES)
    )


# Mass Conversion form class
class ConversionMassForm(forms.Form):
    CHOICES = [("pound", "Pound"), ("kilogram", "Kilogram")]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs = {
            "type":"number",
            "placeholder":"Enter the Number"
        }
    ))
    measure1 = forms.CharField(
        label="",
        widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label="",
        widget=forms.Select(choices=CHOICES)
    )


# Form class for User Registration
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]