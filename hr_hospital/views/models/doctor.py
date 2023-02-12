from odoo import fields, models


class doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctors'

    name = fields.Char(string='Doctor Name', required=True)
    position = fields.Selection(
        selection=[
            ('dentist', 'Dentist'),
            ('surgeon', 'Surgeon'),
            ('urologist', 'Surgeon'),
            ('neurologist', 'Surgeon'),
        ],
        string='Position',
    )
