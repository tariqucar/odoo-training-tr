from odoo import models, fields


class Hr_Employee(models.Model):

    _inherit = "hr.employee"

    identification_ids= fields.One2many(comodel_name = "employee_identity", inverse_name = 'employee_name')
