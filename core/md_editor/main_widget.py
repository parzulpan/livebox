# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""
import sys

from PyQt5.QtWidgets import QWidget, QSplitter, QPlainTextEdit, QHBoxLayout, QMenu, QAction, QFileDialog, QApplication
from PyQt5.QtCore import Qt, QUrl, QFile, QIODevice
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

from core.md_editor.preview_page import PreviewPage
from core.md_editor.document import Document
from utils.common import PromptBox


class MainWidget(QWidget):
    """

    """
    def __init__(self):
        super(MainWidget, self).__init__()

        # ui
        self.preview_page = PreviewPage()
        self.document = Document()

        self.splitter = QSplitter(Qt.Horizontal)

        self.editor = QPlainTextEdit(self.splitter)
        self.editor.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont))

        self.preview = QWebEngineView(self.splitter)
        self.preview.setContextMenuPolicy(Qt.NoContextMenu)
        self.preview.setPage(self.preview_page)
        self.preview.setUrl(QUrl("./resources/index.html"))

        self.channel = QWebChannel()
        self.channel.registerObject("content", self.document)
        self.preview_page.setWebChannel(self.channel)
        self.default_text_file = QFile("./resources/default.md")
        self.default_text_file.open(QIODevice.ReadOnly)
        self.editor.setPlainText(str(self.default_text_file.readAll()))

        self.h_layout = QHBoxLayout()
        self.menu_widget = QWidget(self)
        self.menu_file = QMenu(self.menu_widget)
        self.new_action = QAction()
        self.open_action = QAction()
        self.save_action = QAction()
        self.save_as_action = QAction()
        self.exit_action = QAction()

        #
        self.file_path = None
        self.content = None

        self.editor.textChanged.connect(lambda: self.document.set_text(self.editor.toPlainText()))
        self.new_action.triggered.connect(self.answer_new_action_triggered)
        self.open_action.triggered.connect(self.answer_open_action_triggered)
        self.save_action.triggered.connect(self.answer_save_action_triggered)
        self.save_as_action.triggered.connect(self.answer_save_as_action_triggered)
        self.exit_action.triggered.connect(self.answer_exit_action_triggered)
        self.editor.document().modificationChanged.connect(self.answer_editor_document_modification_changed)

        self._init_ui()

    def _init_ui(self):
        """

        :return:
        """
        self.menu_file.addAction(self.new_action)
        self.menu_file.addAction(self.save_action)
        self.menu_file.addAction(self.open_action)
        self.menu_file.addAction(self.save_as_action)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.exit_action)

        self.h_layout.addWidget(self.editor)
        self.h_layout.addWidget(self.preview)

        self.setLayout(self.h_layout)

    def open_file(self, path: str) -> None:
        """

        :param path:
        :return:
        """
        f = QFile(path)
        if not f.open(QIODevice.ReadOnly):
            _tip = PromptBox(3, "不能打开文件！")
            _tip.exec_()
            return
        self.file_path = path
        self.editor.setPlainText(str(f.readAll()))

    def is_modified(self) -> bool:
        """

        :return:
        """
        return self.editor.document().isModified()

    def answer_new_action_triggered(self):
        """

        :return:
        """
        if self.is_modified():
            _tip = PromptBox(1, "您尚未保存更改。\n您是否仍要创建一个新文档？")
            flag = _tip.exec_()
            if not flag:
                return
        self.file_path = None
        self.editor.setPlainText("## New document")
        self.editor.document().setModified(False)

    def answer_open_action_triggered(self):
        """

        :return:
        """
        if self.is_modified():
            _tip = PromptBox(1, "您尚未保存更改。\n您是否仍要创建一个新文档？")
            flag = _tip.exec_()
            if not flag:
                return
        file_path = QFileDialog.getOpenFileName(self, "打开md文件", "", "MarkDown File (*.md)")
        if not file_path[0]:
            return

        self.open_file(file_path[0])

    def answer_save_action_triggered(self):
        """

        :return:
        """
        if not self.file_path:
            self.answer_save_as_action_triggered()
            return
        f = QFile(self.file_path)
        if not f.open(QIODevice.ReadOnly | QIODevice.Text):
            _tip = PromptBox(3, "无法写入文件！")
            _tip.exec_()
            return
        f.write(self.editor.toPlainText())
        self.editor.document().setModified(False)

    def answer_save_as_action_triggered(self):
        """

        :return:
        """
        file_path = QFileDialog.getSaveFileName(self, "保存md文件", "", "MarkDown File (*.md)")
        if not file_path[0]:
            return
        self.file_path = file_path[0]
        self.answer_save_action_triggered()

    def answer_exit_action_triggered(self):
        """

        :return:
        """
        if self.is_modified():
            _tip = PromptBox(1, "您尚未保存更改。\n确定退出吗？")
            flag = _tip.exec_()
            if not flag:
                return
        self.close()

    def answer_editor_document_modification_changed(self):
        """

        :return:
        """
        self.save_action.triggered.emit()
        self.save_action.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec_())
