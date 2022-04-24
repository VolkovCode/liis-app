from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class LetterPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall(r"[A-Za-z]", password) or not re.findall(r"\d", password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну букву и цифру"),
            )

    def get_help_text(self):
        return _(
            "Ваш пароль должен содержать как минимум одну букву и цифру"
        )
