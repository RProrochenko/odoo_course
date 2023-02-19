from odoo import fields, models


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctors'

    name = fields.Char(string='Doctor Name', required=True)
    specialization = fields.Selection(
        [('Pediatricians', 'Pediatricians'),
         ('Allergists', 'Allergists'),
         ('Dermatologists', 'Dermatologists'),
         ('Ophthalmologists', 'Ophthalmologists'),
         ('Cardiologists', 'Cardiologists'),
         ('Endocrinologists', 'Endocrinologists'),
         ('Nephrologists', 'Nephrologists'),
         ], required=True)
