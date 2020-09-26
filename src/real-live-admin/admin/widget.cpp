#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    initHomePageUI();
    initAppMgrUI();
    initLiveMgrUI();
    initTvMgrUI();
    initRsMgrUI();
    _stack->addWidget(&homepage);
    _stack->addWidget(&appMgr);
    _stack->addWidget(&liveMgr);
    _stack->addWidget(&tvMgr);
    _stack->addWidget(&rsMgr);
    auto *homepageItem = new QListWidgetItem("首页");
    homepageItem->setTextAlignment(Qt::AlignCenter);
    homepageItem->setSizeHint(QSize(100, 50));
    _list->insertItem(0, homepageItem);
    auto *appMgrItem = new QListWidgetItem("软件管理");
    appMgrItem->setTextAlignment(Qt::AlignCenter);
    appMgrItem->setSizeHint(QSize(100, 50));
    _list->insertItem(1, appMgrItem);
    auto *liveMgrItem = new QListWidgetItem("直播管理");
    liveMgrItem->setTextAlignment(Qt::AlignCenter);
    liveMgrItem->setSizeHint(QSize(100, 50));
    _list->insertItem(2, liveMgrItem);
    auto *tvMgrItem = new QListWidgetItem("电视管理");
    tvMgrItem->setTextAlignment(Qt::AlignCenter);
    tvMgrItem->setSizeHint(QSize(100, 50));
    _list->insertItem(3, tvMgrItem);
    auto *rsMgrItem = new QListWidgetItem("电台管理");
    rsMgrItem->setTextAlignment(Qt::AlignCenter);
    rsMgrItem->setSizeHint(QSize(100, 50));
    _list->insertItem(4, rsMgrItem);
    _list->setCurrentRow(0);
    _list->setFixedWidth(102);
    connect(_list, SIGNAL(currentRowChanged(int)), this, SLOT(widgetDisplay(int)));

    mainLayout->setContentsMargins(0, 0, 0, 0);
    mainLayout->setSpacing(0);
    hLayout->setContentsMargins(0, 0, 0, 0);
    hLayout->setSpacing(0);
    hLayout->addWidget(_list);
    hLayout->addWidget(_stack);
    mainLayout->addLayout(hLayout);
    setLayout(mainLayout);
    setMinimumSize(800, 600);
}

Widget::~Widget()
{
    delete _stack;
    delete _list;
    delete mainLayout;
    delete hLayout;
}

void Widget::initHomePageUI() {
    std::cout << "initHomePageUI" << std::endl;
}

void Widget::initAppMgrUI() {
    std::cout << "initAppMgrUI" << std::endl;
}

void Widget::initLiveMgrUI() {
    std::cout << "initLiveMgrUI" << std::endl;
}

void Widget::initTvMgrUI() {
    std::cout << "initTvMgrUI" << std::endl;
}

void Widget::initRsMgrUI() {
    std::cout << "initRsMgrUI" << std::endl;
}

void Widget::widgetDisplay(int index) {
    std::cout << index << std::endl;
    _stack->setCurrentIndex(index);
}

