from django.forms import widgets

class DurationWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        wdgts = (widgets.TextInput({'size': '5'}), widgets.TextInput({'size': '5'}))
        super(DurationWidget, self).__init__(wdgts, attrs)

    def decompress(self, value):
        if value:
            return (value.split(':'))
        return (None, None)

