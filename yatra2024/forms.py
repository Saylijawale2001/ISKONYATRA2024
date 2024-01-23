from django import forms
from .models import mar24yatra_reg


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = mar24yatra_reg
        fields = '__all__'
"""
    def clean_fR_Mob(self):
        fR_Mob = self.cleaned_data['fR_Mob']
        fR_Mob_digits = ''.join(filter(str.isdigit, fR_Mob))

        if len(fR_Mob_digits) != 10:
            raise forms.ValidationError('Invalid mobile number. Please enter a 10-digit number.')

        if mar24yatra_reg.objects.filter(fR_Mob=fR_Mob_digits).exists():
            raise forms.ValidationError('Mobile number is already registered.')

        return fR_Mob_digits
"""