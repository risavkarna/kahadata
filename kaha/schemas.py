import re
from marshmallow import Schema, fields, ValidationError

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

class KahaResourceSchema(Schema):
    active  = fields.Boolean(attribute='is_active')
    contact_number = fields.Method('format_contactnumber')
    contact_name = fields.Str(attribute='contactname')
    created = fields.DateTime()
    updated = fields.DateTime()
    types = fields.Nested('KahaResourceTypeSchema', many=True, only='resource_type')
    props = fields.Nested('KahaResourcePropSchema', many=True, exclude=('resource',))

    def format_contactnumber(self, resource):
        try:
            if resource.contactnumber:
                return [int(d) for d in re.split('\s|,', resource.contactnumber)]
            return []
        except ValueError:
            return None

    class Meta:
        fields = ('resource_id',
                'uuid',
                'title', 
                'district',
                'district_code',
                'tole',
                'vdc_code',
                'description',
                'contact_name',
                'contact_number',
                'updated',
                'created',
                'types',
                'props'
                )

class KahaResourceTypeSchema(Schema):
    resource = fields.Nested(KahaResourceSchema)
    class Meta:
        fields = (
                'resource_type',
                'resource',
                )

class KahaResourcePropSchema(Schema):
    resource = fields.Nested(KahaResourceSchema)
    class Meta:
        fields = (
                'key',
                'value',
                'resource',
                )

