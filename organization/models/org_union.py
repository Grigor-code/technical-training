""" Подразделение имеет характеристики:
•	Название
•	Описание
•	Руководитель 
 """
from odoo import fields, models

class OrgUnion(models.Model):
    _name="org.union"
    _description="Org Union"
    name = fields.Char(string="Наименование",required=True)
    description=fields.Text()
    head=fields.Many2one("org.employee",string="Руководитель")