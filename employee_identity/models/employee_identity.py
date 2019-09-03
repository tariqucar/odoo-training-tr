from odoo import models, fields


class employee_identity(models.Model):

    _name = "employee_identity"
    _description = "Employee Identity"

    employee_name = fields.Many2one("hr.employee", string="Employee Name", required=True)

    type = fields.Selection([('passport', 'Passport'), ('id_card', 'ID Card'), ('driving_license', 'Driving License')], string="Card Type")
    id_number=fields.Char(size=20,string="ID Number")