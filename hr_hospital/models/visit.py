from odoo import fields, models


class Disease(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visits Info'

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        ondelete='cascade',
        required=True,
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        ondelete='cascade',
        required=True,
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        ondelete='cascade',
    )

    visit_date = fields.Date(default=fields.Date.today)
