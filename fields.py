from datetime import timedelta

from django.forms import fields, util

from widgets import DurationWidget

class HourField(fields.IntegerField):
    def clean(self, value):
        value = super(HourField, self).clean(value)
        return value

class MinuteField(fields.IntegerField):
    default_error_messages = {
        'out_of_range': u'Value must be within 0 and 59'
    }

    def clean(self, value):
        value = super(MinuteField, self).clean(value)
        if not 0 <= value <= 59:
            raise util.ValidationError(self.error_messages['out_of_range'])
        return value

class DurationField(fields.MultiValueField):
    widget = DurationWidget

    def __init__(self, *args, **kwargs):
        all_fields = (HourField(), MinuteField())

        super(DurationField, self).__init__(all_fields, *args, **kwargs)

    def compress(self, datalist):
        if datalist:
            hours = datalist[0]
            minutes = datalist[1]
            return timedelta(hours=hours, minutes=minutes).seconds
        return None
