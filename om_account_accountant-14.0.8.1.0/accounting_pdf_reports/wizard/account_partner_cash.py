# -*- coding: utf-8 -*-

from odoo import fields, models, _

class AccountPartnerCash(models.TransientModel):
    _inherit = "account.common.partner.report"
    _name = "account.report.partner.cash"
    _description = "Account Partner Cash In/Out"

    role = fields.Char(string="role")
    partners = fields.Many2one('res.partner', string='Partner')

    def _get_report_data(self, data):
        data = self.pre_print_report(data)
        data['form'].update({
            'role': self.role,
            'partners': self.partners.ids
        })
        return data

    def _print_report(self, data):
        data = self._get_report_data(data)
        return self.env.ref('accounting_pdf_reports.action_report_partner_cash').report_action(self, data=data)

