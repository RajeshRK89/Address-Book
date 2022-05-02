import re
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from sequence import get_next_value


class Sequence(models.Model):

    name = models.CharField(
        verbose_name=_("name"),
        max_length=100,
        primary_key=True,
    )

    last = models.PositiveIntegerField(
        verbose_name=_("last value"),
    )

    class Meta:
        verbose_name = _("sequence")
        verbose_name_plural = _("sequences")

    def __str__(self):
        return "Sequence(name={}, last={})".format(repr(self.name), repr(self.last))


def parse_sequence(value, initial_value):
    # intial value is valid only for the first time
    val = get_next_value(value, initial_value=initial_value)
    return "{}{}".format(value, val)


class SequenceField(models.CharField):
    description = (
        "A field to save ID's with specific prefix by automatically generation consequent values from a sequence"
    )

    def __init__(self, verbose_name=None, name=None, prefix=None, initial_value=1000, **kwargs):
        self.initial_value = initial_value
        self.prefix = prefix
        super(SequenceField, self).__init__(verbose_name=None, name=None, **kwargs)

    def get_db_prep_value(self, value, *args, **kwargs):
        # if value exists never call the get value
        if value is None and self.prefix is None:
            return None
        elif value is not None and value != "":
            return value
        return parse_sequence(self.prefix, self.initial_value)

    def to_python(self, value):
        if value is None or isinstance(value, CharField):
            return value
        try:
            return value
        except (TypeError, ValueError):
            raise ValidationError("This value must be an CHAR or a string represents an charfield.")
