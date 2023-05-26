# -*- coding: utf-8 -*-

from odoo.tests import TransactionCase


class TestPartnerCashReport(TransactionCase):

    def test_partners_field_type_positive(self):
        partner_info = self.env['res.partner'].search([])[0]
        record = self.env['account.report.partner.cash'].create({'partners': partner_info.id})
        self.assertIsNotNone(record.partners, partner_info)
        print("Positive Test case for checking TYPE of field partners")
        print('Your test was successful!')

    def test_partners_field_type_negative(self):
        try:
            record = self.env['account.report.partner.cash'].create({'partners': "any partner"})
            self.assertIsNotNone(record.partners, "any partner")
        except:
            print("Negative Test case for checking TYPE of field partners")
            print('Your test was successful!')

    def test_partners_if_not_exist(self):
        record = self.env['account.report.partner.cash'].create({'partners': None})
        self.assertIsNotNone(record.partners, None)
        print("Test case for checking if partner field has None value")
        print('Your test was successful!')


    # def test_partner_ledger_cash(self):
    #     partner = self.env['res.partner'].search([])[0]
    #     account_move_lines = self.env['account.move.line'].search([])
    #     # new_moves = []
    #     # for move_line in account_move_lines:
    #     #     if move_line.move_id.partner_id.id == partner.id:
    #     #         new_moves.append(move_line)
    #     # accounts = self.env['account.account'].search([])
    #     # print("==== MOVE LINES ====")
    #     # print(new_moves)
    #
    #     query_get_data = ('"account_move_line"',
    #                       '(((("account_move_line"."parent_state" = %s) AND ("account_move_line"."company_id" = %s)) AND (("account_move_line"."display_type" not in (%s,%s)) OR "account_move_line"."display_type" IS NULL)) AND (("account_move_line"."parent_state" != %s) OR "account_move_line"."parent_state" IS NULL)) AND ("account_move_line"."company_id" IS NULL  OR ("account_move_line"."company_id" in (%s)))',
    #                       ['posted', 1, 'line_section', 'line_note', 'cancel', 1])
    #     reconcile_clause = ""
    #     query = """
    #         SELECT "account_move_line".id, "account_move_line".date, j.code, acc.code as a_code, acc.name as a_name, "account_move_line".ref, m.name as move_name, "account_move_line".name, "account_move_line".debit, "account_move_line".credit, "account_move_line".amount_currency,"account_move_line".currency_id, c.symbol AS currency_code
    #         FROM """ + query_get_data[0] + """
    #         LEFT JOIN account_journal j ON ("account_move_line".journal_id = j.id)
    #         LEFT JOIN account_account acc ON ("account_move_line".account_id = acc.id)
    #         LEFT JOIN res_currency c ON ("account_move_line".currency_id=c.id)
    #         LEFT JOIN account_move m ON (m.id="account_move_line".move_id)
    #         WHERE "account_move_line".partner_id = %s
    #             AND m.state IN %s
    #             AND "account_move_line".account_id IN %s AND """ + query_get_data[1] + reconcile_clause + """
    #             ORDER BY "account_move_line".date"""
    #
    #     self.env.cr.execute(query)
    #     res = self.env.cr.dictfetchall()
    #     print(res)