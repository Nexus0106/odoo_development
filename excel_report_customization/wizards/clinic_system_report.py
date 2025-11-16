import base64
import io
from io import BytesIO
import xlsxwriter
from odoo import api,fields,models
from odoo.tools import file_open


class ClinicSystemWizard(models.TransientModel):
    _name = 'clinic.system.wizard'
    _description = 'Clinic System Wizard'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    doctor_ids = fields.Many2many('hr.employee','Doctors')
    excel_file = fields.Binary('Download report')
    file_name = fields.Char('Excel File Name',size=16,readonly=True)

    def action_generate_excel_report(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output,{'in_memory':True})
        worksheet = workbook.add_worksheet('Customer Booking')

        header_format= workbook.add_format({'bold':True,'font_size':25,'align':'center'})
        title_format= workbook.add_format({'bold':True,'font_size':14,'align':'center','border':1})
        body_format= workbook.add_format({'font_size':13,'align':'center','border':1,'num_format':'#,##0.00'})
        date_format= workbook.add_format({'font_size':13,'align':'center','border':1,'num_format':'dd/mm/yyyy'})

        worksheet.merge_range('A1:E1','Customer Booking Xlsx Report',header_format)

        headers = ['Name','Client','Booking Date', 'Total Amount']
        for col, header in enumerate(headers):
            worksheet.write(3, col, header,title_format)

        worksheet.set_column('A:A',15)
        worksheet.set_column('B:B',30)
        worksheet.set_column('C:D',25)

        worksheet.set_row(0,25)
        row = 4
        booking_ids = self.env['customer.booking'].search([('date','>=',self.start_date),('date','<=',self.end_date),('employee_ids','in',self.doctor_ids.ids)])
        for booking in booking_ids:
            worksheet.write(row,0,booking.name,body_format)
            worksheet.write(row,1,booking.partner_id.name if booking.partner_id else '',body_format)
            worksheet.write(row,2,booking.date,date_format)
            worksheet.write(row,3,booking.total_amount,body_format)
            row +=1

        workbook.close()
        output.seek(0)
        self.write({
            'excel_file':base64.b64encode(output.read()),
            'file_name':'Customer_Booking.xlsx'
        })

        return {
            'type':'ir.actions.act_url',
            'url':'/web/content/clinic.system.wizard/%s/excel_file/Customer_Booking.xlsx?download=true' % (self.id),
            'target':'new',
        }






