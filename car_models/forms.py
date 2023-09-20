from django import forms

# Create your models here.
class Car_(forms.Form):
    stamp_ = forms.CharField(max_length=15, label='Модель автомобиля')
    manufacturer_ = forms.CharField(max_length=15, label='Производитель')
    release_date_ = forms.IntegerField(min_value=1980, max_value=2023, label='Дата выпуска')
    state_number_ = forms.CharField(max_length=15, label='Гос. номер')

