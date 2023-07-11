"""  Должен быть реализован справочник типовых заявок, 
в которых указан набор задач, характерный для заявки. """

from odoo import fields, models

class OrgSetTask(models.Model):
    _name="org.set.task"
    _description="Org Set Task"

    name = fields.Char()
    task_ids=fields.Many2many("org.task",string="задачи")

