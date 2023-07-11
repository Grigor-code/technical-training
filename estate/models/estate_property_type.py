from odoo import fields, models

class TestModelType(models.Model):
    _name = "test.model.type"
    _description = "Test Model Type"

    name = fields.Char(string='Name',required=True)

