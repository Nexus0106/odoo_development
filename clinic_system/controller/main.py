from odoo import http,api
import requests
from odoo.http import request,Response
import json


class BookingAPI(http.Controller):

    @http.route('/api/booking',type='http',auth='none',methods=['POST'],csrf=False,cors="*")
    def booking_data(self,**kwargs):
        booking_lines = request.env['customer.booking'].search([])
        data = []
        for rec in booking_lines:
            data.append(rec.name)
        return Response(
            json.dumps({"count":len(booking_lines),"results":data}),
            content_type = 'application/json;charset=utf-8',
            status = 200
        )

    @http.route('/api/booking_lines',type='json',auth='none',methods=['POST'],csrf=False,cors="*")
    def booking_data_json(self, **kwargs):
        booking_lines = request.env['customer.booking'].search([])

        data = [{
            "id":rec.id,
            "name":rec.name,
        } for rec in booking_lines
        ]

        return {"count": len(data), "results": data}

    @http.route('/api/booking_create', type='http', auth='none', methods=['POST'], csrf=False, cors="*")
    def booking_data(self, **kwargs):
        booking = request.env['customer.booking']
        data = json.loads(request.httprequest.data or {})
        date = data.get('date')
        partner = data.get('partner')
        record = booking.sudo().create({
            'date':date,
            'partner_id':partner
        })
        return Response(
            json.dumps({"results": record.id}),
            content_type='application/json;charset=utf-8',
            status=200
        )

    @http.route('/api/date_changes', type='http', auth='none', methods=['POST'], csrf=False, cors="*")
    def booking_changes(self, **kwargs):
        data = json.loads(request.httprequest.data or {})
        date = data.get('date')
        booking_id = data.get('booking_id')
        booking = request.env['customer.booking'].sudo().browse(booking_id)
        booking.date = date

        return Response(
            json.dumps({"results": "Success Update"}),
            content_type='application/json;charset=utf-8',
            status=200
        )


