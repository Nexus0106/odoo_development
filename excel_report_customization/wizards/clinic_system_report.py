import base64
import io
from io import BytesIO
import xlsxwriter
from odoo import api,fields,models

class ClinicSystemWizard(models.TransientModel):
    _name = 'clinic.system.wizard'
    _description = 'Clinic System Wizard'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    doctor_ids = fields.Many2many('hr.employee','Doctors')


