from odoo import api, models, fields,_

class Sale(models.Model):
    _inherit = 'sale.order'

    phone = fields.Char('Phone')