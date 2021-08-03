from django.core.exceptions import ValidationError
    def clean(self):
        variant must have size or color
        if self.color and self.size == "" or self.color and self.size == null:
            raise ValidationError('Variant must include at least one size or color')