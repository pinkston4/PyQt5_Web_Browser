from PyQt5.QtWidgets import QVBoxLayout
from . import tab
from . import address
from . import toolbar
from . import mainView


class CreateApp:
    """
    CreateApp is where all pieces are put togethor to build the app
    Methods:
        __init__
        create_layout
    """

    def __init__(self):
        self.create_layout()

    def create_layout(self):
        """
        createLayout sets the tabbar, main container, and toolbar(address bar is in toolbar)
        inside the layout
        """
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.tabbar = tab.TabBar()

        self.addressBar = address.AddressBar()

        self.toolbar = toolbar.ToolBar()
        self.toolbar.toolbarLayout.addWidget(self.addressBar)
        self.toolbar.toolbarLayout.addWidget(self.tabbar.addTabButton)

        self.container = mainView.Container()

        self.layout.addWidget(self.tabbar.tabbar)
        self.layout.addWidget(self.toolbar.toolbar)
        self.layout.addWidget(self.container.container)

        self.container.container.layout.addWidget(self.tabbar.tabs[self.tabbar.tabCount])
        self.container.container.layout.setCurrentWidget(self.tabbar.tabs[self.tabbar.tabCount])
        self.tabbar.tabbar.addTab("New Tab")
        self.tabbar.tabbar.setTabData(self.tabbar.tabCount, 'tab' + str(self.tabbar.tabCount))

    def update_layout(self):
        self.container.container.layout.addWidget(self.tabbar.tabs[self.tabbar.tabCount])
        self.container.container.layout.setCurrentWidget(self.tabbar.tabs[self.tabbar.tabCount])
        self.tabbar.tabbar.addTab("New Tab")
        self.tabbar.tabbar.setTabData(self.tabbar.tabCount, 'tab' + str(self.tabbar.tabCount))
