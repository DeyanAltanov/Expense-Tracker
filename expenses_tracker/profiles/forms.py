from django import forms

from expenses_tracker.profiles.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'