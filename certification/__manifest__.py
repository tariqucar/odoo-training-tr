# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Mücahit & Tarık Eğitim",
    'version': '12.0.1.0.0',
    "category": "Customer Relationship Management",
    "website": "https://github.com/oca/partner-contact",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    "contributors": [
        'Tarık Uçar <tako@tai.com.tr>',
        'Selahattin Mücahit Keskin <selo@tai.com.tr>',
    ],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/certification.xml",
        "views/certification_standard.xml",
        "views/certification_bodies.xml",
        "views/res_partner.xml"
    ],
    # 'post_init_hook': 'post_init_hook',
}
