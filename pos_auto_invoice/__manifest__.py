# -*- coding: utf-8 -*-
{
    'name': 'POS Auto Invoice',
    'summary':'POS Auto Invoice',
    'description': 'POS Auto Invoice',
    'author':'Test Developer',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'point_of_sale',
    ],
    'data': [

    ],
    'assets':{
        'point_of_sale._assets_pos':[
            'pos_auto_invoice/static/src/js/PaymentScreen.js',
        ]
    },
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}