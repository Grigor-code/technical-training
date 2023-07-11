from odoo import fields, models

class TestModelTags(models.Model):
    _name = "test.model.tag"
    _description = "Test Model Tag"

    name = fields.Char(required=True, string="Тег")