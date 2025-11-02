# -*- coding: utf-8 -*-
{
    'name': 'Clinic System',
    'summary':'Clinic System',
    'description': 'Clinic System',
    'author':'Test User',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'base',
        'hr',
        'product',
        'resource',
        'sale',
    ],
    'data': [
        'data/sequence.xml',
        'views/customer_booking_view.xml',
        'security/ir.model.access.csv',
        'security/user_group.xml',
        'data/record.xml',
        'reports/report.xml',
        'reports/clinic_system_report.xml',
        'reports/sale_order_pdf_inherit.xml',
    ],
    'assets':{
        'web.assets_backend':[
            '/clinic_system/static/src/js/order_line_widget.js',
            '/clinic_system/static/src/xml/order_line_widget.xml',
        ]
    },
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}