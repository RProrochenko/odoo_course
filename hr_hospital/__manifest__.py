# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'My Library',
    'version': '15.0.1.0.0',

    'category': 'Extra Tools',
    'summary': """
                """,
    
    'license': 'LGPL-3',
    'author': 'Rostyslav Prorochenko',
    'website': 'https://odoo.school',

    'depends': [
    ],

    'data': [
        'security/ir.model.access.csv'

        'views/menu.xml'
        'views/doctor.xml'

    ],

    'demo': [
    ],

    'support': 'support@support.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}