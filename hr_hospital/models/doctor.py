from odoo import fields, models


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctors'

    name = fields.Char(string='Doctor Name', required=True)
