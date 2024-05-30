from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django import forms

from .models import User, Meeting, LeanCanvas, WorkExperience


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            "phone_number",
            "first_name",
            "last_name",
            "email",
        )


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "birthday",
            "degree",
            "interests",
            "abilities",
            "bio",
            "college_name",
            "type",
            "specialty",
            "province",
            "city",
            "number_id",
        )
        exclude = ["password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True  # Make each field required
            if isinstance(field, forms.ModelMultipleChoiceField):
                field.widget.attrs['class'] = 'select2'


class MeetingCreateForm(ModelForm):
    class Meta:
        model = Meeting
        exclude = ("created_time", "last_update_time", "status", "rate", "uuid")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class WorkExperienceCreateForm(ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ("created_time", "last_update_time", "uuid")


class LeanCanvasForm(ModelForm):
    class Meta:
        model = LeanCanvas
        exclude = ("created_time", "last_update_time", "uuid")


class UserLoginOrRegisterForm(ModelForm):
    phone_number = forms.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                r'^09\d{9}$',
                message='شماره تماس باید با 09 شروع شده و شامل 11 رقم باشد.'
            )
        ]
    )

    class Meta(UserCreationForm):
        model = User
        fields = (
            "phone_number",
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
        # Remove labels and add placeholders
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره تماس *'
        self.fields['phone_number'].widget.attrs['style'] = 'text-align:right'
        # Remove labels
        self.fields['phone_number'].label = ''


class UserRegisterFormLevel1(UserCreationForm):
    phone_number = forms.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                r'^09\d{9}$',
                message='شماره تماس باید با 09 شروع شده و شامل 11 رقم باشد.'
            )
        ]
    )

    class Meta(UserCreationForm):
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change placeholders
        self.fields['email'].widget.attrs['placeholder'] = "* " + self.fields["email"].label
        # self.fields['phone_number'].widget.attrs['placeholder'] = "* " + self.fields["phone_number"].label
        self.fields['password1'].widget.attrs['placeholder'] = "* " + self.fields["password1"].label
        self.fields['password2'].widget.attrs['placeholder'] = "* " + self.fields["password2"].label
        self.fields['first_name'].widget.attrs['placeholder'] = "* " + self.fields["first_name"].label
        self.fields['last_name'].widget.attrs['placeholder'] = "* " + self.fields["last_name"].label
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].label = ""
            self.fields[field].widget.attrs['style'] = 'text-align:right'
        # Remove/Change help_text
        self.fields['password1'].help_text = 'گذرواژه شما باید حداقل ۸ حرف داشته باشد، نباید مشابه اطلاعات شخصی، یک رمز عبور معمول یا فقط عدد باشد'
        self.fields['password2'].help_text = ''


class UserRegisterFormLevel2(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "birthday",
            "degree",
            "college_name",
            "province",
            "city",
        )
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Change placeholders to fields
        self.fields['first_name'].widget.attrs['placeholder'] = "* " + self.fields["first_name"].label
        self.fields['last_name'].widget.attrs['placeholder'] = "* " + self.fields["last_name"].label
        self.fields['birthday'].widget.attrs['placeholder'] = "* " + self.fields["birthday"].label
        # TODO: مدرک تحصیلی و نام دانشگاه دریافت شود
        self.fields['degree'].widget.attrs['placeholder'] = "* " + self.fields["degree"].label
        self.fields['college_name'].widget.attrs['placeholder'] = "* " + self.fields["college_name"].label
        self.fields['province'].widget.attrs['placeholder'] = "* " + self.fields["province"].label
        self.fields['city'].widget.attrs['placeholder'] = "* " + self.fields["city"].label
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].label = ""
            self.fields[field].widget.attrs['style'] = 'text-align:right'


class UserRegisterFormLevel3(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "type",
            "is_accelerator_experience",
            "is_startup_experience",
        )
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs['style'] = 'text-align:right'


class UserRegisterFormLevel4(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "specialty",
            "why_us",
        )
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs['style'] = 'text-align:right'