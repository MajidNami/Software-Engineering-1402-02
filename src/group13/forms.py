from django import forms
from .models import Question, Choice

class UserForm(forms.Form):
    user = forms.CharField(max_length=100)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'is_correct']
