from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from datetime import date, datetime


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patients Info'
    _inherit = 'res.partner'

    birthday = fields.Date(required=True)
    age = fields.Char(readonly=True)
    passport = fields.Char()
    contact_person = fields.Char()

    @api.onchange('birthday')
    def set_age(self):
        for rec in self:
            if rec.birthday:
                dt = rec.birthday
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + ' years'
