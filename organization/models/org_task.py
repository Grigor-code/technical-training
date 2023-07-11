""" Задача характеризуется:
•	Название
•	Описание
•	Трудоемкость в человекочасах
•	Требуемые для выполнения компетенции
•	Минимальная и максимальная дата начала
•	Минимальная и максимальная дата завершения
•	Фактические сроки выполнения
•	Необходимые предшественники (другие задачи)
•	Требуемые ресурсы (инструменты, материалы)
 """
from odoo import fields, models

class OrgTask(models.Model):
    _name="org.task"
    _description="Org Task"
     
    name = fields.Char(string="Наименование",required=True)
    description=fields.Text()
    laboriousness=fields.Integer()
    min_date_start=fields.Datetime()
    max_date_start=fields.Datetime()
    min_date_end=fields.Datetime()
    max_date_end=fields.Datetime()
    resource_ids=fields.Many2many("org.resource")
    other_task_ids=fields.Char()

