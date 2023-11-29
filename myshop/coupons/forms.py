from django import forms


class CouponApplyForm(forms.Form):
    """Форма для ввода кода купона."""
    code = forms.CharField()
