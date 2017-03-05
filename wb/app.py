from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from PyQt5.QtCore import *
from .tab import TabBar
from .address import AddressBar
from .toolbar import ToolBar
from .mainView import Container


class CreateApp:
    """
    CreateApp is where all pieces are put together to build the app and update the application
    Methods:
        __init__
        create_layout
        go_back
        go_forward
        refresh_page
        browse_to
        update_addressbar_url
    Author: Jack Pinkston
    """

    def __init__(self):
        self.layout = QVBoxLayout()
        self.tabbar = TabBar()
        self.addressBar = AddressBar()
        self.toolbar = ToolBar()
        self.container = Container()
        self.back_button = QPushButton('<')
        self.forward_button = QPushButton('>')
        self.reload_button = QPushButton('Refresh')
        self.create_layout()

    def create_layout(self):
        """
        createLayout sets the tabbar, main container, and toolbar(address bar is in toolbar)
        inside the layout, it also sets the container to the tab (where the url actually is)
        """
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toolbar.toolbar)
        self.layout.addWidget(self.container.container)
        self.addressBar.returnPressed.connect(self.browse_to)
        self.back_button.clicked.connect(self.go_back)
        self.forward_button.clicked.connect(self.go_forward)
        self.reload_button.clicked.connect(self.refresh_page)
        self.toolbar.toolbarLayout.addWidget(self.back_button)
        self.toolbar.toolbarLayout.addWidget(self.forward_button)
        self.toolbar.toolbarLayout.addWidget(self.addressBar)
        self.toolbar.toolbarLayout.addWidget(self.reload_button)
        self.container.container.layout.addWidget(self.tabbar.tab)
        self.container.container.layout.setCurrentWidget(self.tabbar.tab)
        self.update_addressbar_url()

    def go_back(self):
        """
        when back arrow is clicked, go back one page
        Author: Jack Pinkston
        """
        self.tabbar.tab.content.back()
        self.update_addressbar_url()

    def go_forward(self):
        """
        when forward arrow is pressed, go forward one page
        Author: Jack Pinkston
        """
        self.tabbar.tab.content.forward()
        self.update_addressbar_url()

    def refresh_page(self):
        """
        when the refresh button is clicked, reload the current page
        Author jack Pinkston
        """
        self.tabbar.tab.content.reload()
        self.update_addressbar_url()

    def browse_to(self):
        """
        takes what ever is in the address bar and either searches google, or navigates to that url
        Author: Jack Pinkston
        """
        text = self.addressBar.text()
        load_new_url = self.tabbar.tab.content
        if 'http' not in text:
            if '.' not in text:
                new_url = 'https://www.google.com/search?q=' + text
            else:
                new_url = 'http://' + text
        else:
            new_url = text

        load_new_url.load(QUrl.fromUserInput(new_url))
        self.update_addressbar_url()

    def update_addressbar_url(self):
        """
        updating the address bar to match the current url
        Author: Jack Pinkston
        """
        self.addressbar_url = self.tabbar.tab.content.url().toString()
        self.addressBar.setText(self.addressbar_url)
