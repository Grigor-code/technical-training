# Характеристики ресурса:
# •	Наименование

from odoo import fields, models

class OrgResource(models.Model):
    _name="org.resource"
    _description="Org Resource"
    name = fields.Char(string="Наименование",required=True)