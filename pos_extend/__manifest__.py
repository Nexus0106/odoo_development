# -*- coding: utf-8 -*-
{
    'name': 'POS Extend',
    'summary':'POS Extend',
    'description': 'POS Extend',
    'author':'POS Extend',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'point_of_sale',
    ],
    'data': [

    ],
    'assets':{
        'point_of_sale._assets_pos':[
            'pos_extend/static/src/js/pos_store.js',
            'pos_extend/static/src/js/order.js',
            'pos_extend/static/src/xml/PosReceipt.xml',
        ]
    },
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}