from odoo import fields, models


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis info'

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
        required=True,
    )

    treatment = fields.Char(required=True)
    diagnosis_date = fields.Datetime(default=fields.Date.today,
                                     required=True)
