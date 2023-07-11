""" Объект характеризуется:
•	Наименование
•	Местоположение
 """

from odoo import fields, models

class OrgObject(models.Model):
    _name="org.object"
    _description="Org Object"
    name = fields.Char(string="Наименование",required=True)
    location=fields.Text()