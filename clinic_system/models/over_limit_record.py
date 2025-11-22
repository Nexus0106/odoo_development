from odoo import models,fields,api
from odoo.addons.test_impex.models import field


class OverLimitRecord(models.Model):
    _name = 'over.limit.record'

    name = fields.Char('Booking ID')
    user_id = fields.Many2one('res.users','Confirm By')
    limit_amount = fields.Float('Limit Amount')
    booking_amount = fields.Float('Booking Amount')
    over_amount = fields.Float('Over Amount',compute='calculate_over_amount')

    @api.depends('limit_amount','booking_amount')
    def calculate_over_amount(self):
        for rec in self:
            rec.over_amount = rec.limit_amount - rec.booking_amount