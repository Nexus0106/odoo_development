# -*- coding: utf-8 -*-
{
    'name': 'Disable Quick Create',
    'summary':'Disable Quick Create',
    'description': 'Disable Quick Create',
    'author':'Test Developer',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'web',
    ],
    'data': [

    ],
    'assets':{
        "web.assets_backend":[
            'disable_quick_create/static/src/js/field.esm.js',
        ]
    },
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}