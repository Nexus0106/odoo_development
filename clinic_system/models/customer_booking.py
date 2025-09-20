from odoo import models,fields

class CustomerBooking(models.Model):
    _name = 'customer.booking' #customer_booking
    _description = 'Customer Booking'

    name = fields.Char('Name')
    client_name = fields.Char('Client Name')
    phone = fields.Char('Phone')
    date = fields.Date('Date')
    booking_time = fields.Datetime('Booking Time')
    number_of_people = fields.Integer('No. Of People')