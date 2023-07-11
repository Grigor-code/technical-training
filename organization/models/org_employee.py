""" Сотрудники характеризуется:
•	ФИО
•	Табельный номер
•	Подразделение
•	Должность
•	Перечень компетенций
•	Календарь доступности
•	Стоимость часа работы
 """
from odoo import fields, models


class OrgEmployee(models.Model):
    _name="org.employee"
    _description="Org Employee"
    name=fields.Char(string="ФИО",required=True)
    number=fields.Integer()
    union=fields.Many2one("org.union",string="Подразделение")
    post=fields.Selection(selection=[('диспечер','диспечер'),('Руководитель подразделения','Руководитель подразделения'),('Сотрудник подразделения','Сотрудник подразделения'),('Руководитель проекта','Руководитель проекта')])
    competence=fields.Selection(selection=[('коммуникативность','коммуникативность'),('творческое мышление','творческое мышление')])
    free_date=fields.Datetime()
    price=fields.Float()

    _sql_constraints = [
        ('unique_number', 'UNIQUE(number)', 'Number should be unique!')
    ]







