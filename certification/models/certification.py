# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from odoo.odoo.exceptions import ValidationError
from datetime import timedelta



class Certification(models.Model):

    _name = "certification"
    _description = "Certification"

    number = fields.Char()
    date = fields.Date(string="Validation Date")
    description = fields.Text(string="Validation Detail")
    standard_id = fields.Many2one("certification.standard")
    owner_id = fields.Many2one('res.partner')
    entity_id = fields.Many2one('res.partner')

    expiry_days = fields.Integer('Expiry Days', readonly=True, compute='compute_expiry_days', store=True)
    expiry_status = fields.Selection([
        ('expired', "Expired"),
        ('available', "Available")
    ], readonly=True, compute='compute_expiry_days', store=True)

    @api.constrains('entity_id')
    def _check_entity_id(self):
        if self.entity_id and self.entity_id.is_certification_body == False:
            raise ValidationError('It is not a certification entity')

    @api.depends('date')
    def compute_expiry_days(self):
        for certificate in self:
            if certificate.date:
                certificate.expiry_days = (certificate.date - fields.Date.today()).days
                if certificate.expiry_days > 0:
                    certificate.expiry_status = 'available'
                else:
                    certificate.expiry_status = 'expired'

    @api.multi
    def update_date_one_month(self):
        self.ensure_one()
        if self.date:
            self.write({'date': self.date + timedelta(days=30)})
