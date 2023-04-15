from django import forms
from .models import User, Project

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
'''
class AssociateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users', 'name']
        widgets = {
            'users': forms.CheckboxSelectMultiple(),
            'name': forms.CheckboxSelectMultiple(),
        }
'''
class AssociateForm(forms.ModelForm):

    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Project
        fields = ['project', 'users']
    def clean(self):
        cleaned_data = super().clean()
        project = cleaned_data.get('project')
        users = cleaned_data.get('users')
        if project.users.count() + len(users) > 5:
            raise forms.ValidationError('O projeto já tem o máximo de usuários permitidos.')
        for user in users:
            if user.users_projects.count() >= 3:
                raise forms.ValidationError(f'O usuário {user} já está em 3 projetos.')
        return cleaned_data