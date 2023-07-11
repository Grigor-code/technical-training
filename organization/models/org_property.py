""" Организация имеет характеристики:
•	Наименование
•	Набор подразделений
 """
from odoo import fields, models

class OrgProperty(models.Model):
    _name="org.property"
    _description="Org Property"
    name = fields.Char(string="Наименование",required=True)
    union=fields.One2many("org.union", "name",string="Подразделения")