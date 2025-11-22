from odoo import api,models,fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    limit_amount = fields.Float('Limit Amount')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    limit_amount = fields.Float('Limit Amount',related='company_id.limit_amount',readonly=False)