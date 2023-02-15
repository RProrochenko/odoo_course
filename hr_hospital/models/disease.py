from odoo import fields, models


class Disease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease Info'

    name = fields.Char(string='Disease', required=True)
    description = fields.Char()
