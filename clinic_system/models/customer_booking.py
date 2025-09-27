from odoo import models,fields,api


class CustomerBooking(models.Model):
    _name = 'customer.booking' #customer_booking
    _inherit = [ 'portal.mixin','mail.thread.main.attachment', 'mail.activity.mixin', 'avatar.mixin']
    _description = 'Customer Booking'

    name = fields.Char('Name')
    client_name = fields.Char('Client Name')
    phone = fields.Char('Phone',related='partner_id.phone')
    date = fields.Date('Date',required=True,tracking=True)
    booking_time = fields.Datetime('Booking Time')
    number_of_people = fields.Integer('No. Of People')
    partner_id = fields.Many2one('res.partner','Client')
    employee_ids = fields.Many2many('hr.employee',
                                    'customer_booking_employee_rel',
                                    'booking_id','employee_id',
                                    'Doctors')
    booking_line_ids = fields.One2many('booking.lines','booking_id','Lines')
    note = fields.Html('Note')
    image = fields.Binary('Image')
    pdf_file = fields.Binary('File')



class BookingLines(models.Model):
    _name = 'booking.lines'
    _description = 'Booking Lines'

    booking_id = fields.Many2one('customer.booking','Customer Booking')
    product_id = fields.Many2one('product.product','Product')
    qty = fields.Float('Qty')
    unit_price = fields.Float('Unit Price')
    total_price = fields.Float('Total Price',compute='change_total_price')

    # @api.onchange('qty','unit_price')
    # def change_total_price(self):
    #     self.total_price = (self.qty * self.unit_price)  + 1000

    @api.depends('qty','unit_price')
    def change_total_price(self):
        self.total_price = (self.qty * self.unit_price) + 1000
