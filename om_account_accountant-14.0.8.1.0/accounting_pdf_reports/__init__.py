# -*- coding: utf-8 -*-

from . import wizard
from . import report
from . import tests


def _pre_init_clean_m2m_models(cr):
    cr.execute("""DROP TABLE IF EXISTS account_journal_account_report_partner_ledger_rel""")
