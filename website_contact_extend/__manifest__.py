###################################################################
#
#    IT IS AG, software solutions: http://www.itis.de
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#
###################################################################

{
    'name': "Website Contact Form Extend",

    'summary': "Extended Website Contact View",

    'author': "IT IS AG, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/data-protection",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/
    # addons/base/module/module_data.xml
    # for the full list
    'version': '12.0.1.0',
    'license': 'AGPL-3',
    'category': 'Data Protection',
    'depends': ['base',
                'contacts',
                'website_crm',
                'mail',
                'contacts'
                ],

    'data': [
        'views/website_contact.xml',
        'views/res_partner.xml',
        'views/contact_report.xml',
        'data/email_templates.xml',
        'views/means_of_contact.xml',
        'views/disp_msg_template.xml',
        'views/email_template.xml'
        #'security/ir.model.access.csv',
    ],
}
