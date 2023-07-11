from odoo import fields, models
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char(required=True,default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True )
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    active=fields.Boolean()
    state=fields.Selection(
        string="Status",
        selection=[('new','New'),('Offer Received','Offer Received'),('Offer Accepted','Offer Accepted'),('Sold','Sold'),('Canceled','Canceled')],
        copy=False,
        default="new"
    )
    property_type_id=fields.Many2one("test.model.type",string='Types')
    buyer_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        copy=False
    )
    salesman_id = fields.Many2one(
        'res.users',
        string='Salesman',
        default=lambda self: self.env.user
    )
    tax_ids=fields.Many2many("account.tax",string="Налоги")
    tag_ids=fields.Many2many("test.model.tag", string='Тег')



