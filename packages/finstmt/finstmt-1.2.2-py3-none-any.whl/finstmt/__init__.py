"""
Work with financial statement data in Python. Can calculate free cash flows and help project
financial statements, automatically balancing the balance sheet. 
"""
__version__ = "1.2.2"
from finstmt.bs.main import BalanceSheets
from finstmt.combined.statements import FinancialStatements
from finstmt.config_manage.global_ import CONFIG
from finstmt.inc.main import IncomeStatements
