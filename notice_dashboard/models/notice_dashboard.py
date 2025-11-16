from odoo import models,fields

class NoticeDashboard(models.Model):
    _name = 'notice.dashboard'

    name = fields.Char('Title')
    image = fields.Binary('Image')
    summary = fields.Char('Summary')
    description = fields.Text('Fully Description')
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm')
    ],'State',default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = 'draft'
