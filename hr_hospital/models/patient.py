from odoo import fields, models


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patients Info'

    name = fields.Char(string='Patient name', required=True)
    age = fields.Integer(string='Patient age', required=True)
