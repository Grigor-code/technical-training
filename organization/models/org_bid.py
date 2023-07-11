""" Каждый заявка имеет характеристики:
•	Название
•	Объект
•	Описание
•	Набор задач
•	Необходимые компетенции
•	Статус
•	Дата создания
•	Плановая дата завершения
•	Фактическая дата завершения
 """
from odoo import fields, models

class OrgBid(models.Model):
    _name="org.bid"
    _description="Org Bid"
    name = fields.Char(string="Наименование",required=True)
    obj=fields.Many2one("org.object",string="Обьект")
    description=fields.Text()
    task_ids=fields.Many2many("org.task",string="набор задач")
    competence=fields.Many2many("org.employee",string="набор задач")
    status=fields.Selection(selection=[('В процессе','В процессе'),('Отклонена','Отклонена'),('Закрыта','Закрыта')])
    date_create=fields.Datetime(default=lambda self: fields.Datetime.now())
    planned_date=fields.Datetime()
    actual_date=fields.Datetime()
    tipical=fields.Boolean()





