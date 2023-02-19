from odoo import fields, models


class PersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person Mixin'

    name = fields.Char()
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')])
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image(related="photo",
                         max_width=256,
                         max_height=256,
                         store=True)
