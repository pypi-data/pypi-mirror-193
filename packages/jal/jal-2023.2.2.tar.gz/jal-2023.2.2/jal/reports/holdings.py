from functools import partial

from PySide6.QtCore import Qt, Slot, QObject, QDateTime
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu
from jal.ui.reports.ui_holdings_report import Ui_HoldingsWidget
from jal.reports.reports import Reports
from jal.db.asset import JalAsset
from jal.db.holdings_model import HoldingsModel
from jal.widgets.mdi import MdiWidget
from jal.db.tax_estimator import TaxEstimator
from jal.widgets.price_chart import ChartWindow

JAL_REPORT_CLASS = "HoldingsReport"


# ----------------------------------------------------------------------------------------------------------------------
class HoldingsReport(QObject):
    def __init__(self):
        super().__init__()
        self.name = self.tr("Holdings")
        self.window_class = "HoldingsReportWindow"


# ----------------------------------------------------------------------------------------------------------------------
class HoldingsReportWindow(MdiWidget, Ui_HoldingsWidget):
    def __init__(self, parent: Reports, settings: dict = None):
        MdiWidget.__init__(self, parent.mdi_area())
        self.setupUi(self)
        self._parent = parent
        self.name = self.tr("Holdings")

        self.holdings_model = HoldingsModel(self.HoldingsTableView)
        self.HoldingsTableView.setModel(self.holdings_model)
        self.holdings_model.configureView()
        self.HoldingsTableView.setContextMenuPolicy(Qt.CustomContextMenu)

        self.connect_signals_and_slots()

        # Setup holdings parameters
        current_time = QDateTime.currentDateTime()
        current_time.setTimeSpec(Qt.UTC)  # We use UTC everywhere so need to force TZ info
        self.HoldingsDate.setDateTime(current_time)
        self.HoldingsCurrencyCombo.setIndex(JalAsset.get_base_currency())

    def connect_signals_and_slots(self):
        self.HoldingsDate.dateChanged.connect(self.HoldingsTableView.model().setDate)
        self.HoldingsCurrencyCombo.changed.connect(self.HoldingsTableView.model().setCurrency)
        self.HoldingsTableView.customContextMenuRequested.connect(self.onHoldingsContextMenu)
        self.SaveButton.pressed.connect(partial(self._parent.save_report, self.name, self.HoldingsTableView.model()))

    @Slot()
    def onHoldingsContextMenu(self, pos):
        index = self.HoldingsTableView.indexAt(pos)
        contextMenu = QMenu(self.HoldingsTableView)
        actionShowChart = QAction(text=self.tr("Show Price Chart"), parent=self.HoldingsTableView)
        actionShowChart.triggered.connect(partial(self.showPriceChart, index))
        contextMenu.addAction(actionShowChart)
        actionEstimateTax = QAction(text=self.tr("Estimate Russian Tax"), parent=self.HoldingsTableView)
        actionEstimateTax.triggered.connect(partial(self.estimateRussianTax, index))
        contextMenu.addAction(actionEstimateTax)
        contextMenu.popup(self.HoldingsTableView.viewport().mapToGlobal(pos))

    @Slot()
    def showPriceChart(self, index):
        model = index.model()
        account, asset, currency, asset_qty = model.get_data_for_tax(index)
        self._parent.mdi_area().addSubWindow(ChartWindow(account, asset, currency, asset_qty))

    @Slot()
    def estimateRussianTax(self, index):
        model = index.model()
        account, asset, currency, asset_qty = model.get_data_for_tax(index)
        self._parent.mdi_area().addSubWindow(TaxEstimator(account, asset, asset_qty))
