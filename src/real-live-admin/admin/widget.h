#ifndef WIDGET_H
#define WIDGET_H

#include <iostream>
#include <memory>

#include <QWidget>
#include <QListWidget>
#include <QStackedWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QIcon>
#include <Qt>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget() override;
    void initHomePageUI();
    void initAppMgrUI();
    void initLiveMgrUI();
    void initTvMgrUI();
    void initRsMgrUI();

private:
    QStackedWidget *_stack = new QStackedWidget;
//    std::shared_ptr<QStackedWidget> _stack = std::make_shared<QStackedWidget>();
    QListWidget *_list = new QListWidget;
    QVBoxLayout *mainLayout = new QVBoxLayout;
    QHBoxLayout *hLayout = new QHBoxLayout;
    QWidget homepage;   // 首页
    QWidget appMgr;    // 软件管理
    QWidget liveMgr;    // 直播管理
    QWidget tvMgr;      // 电视管理
    QWidget rsMgr;      // 电台管理

public slots:
    void widgetDisplay(int index);

signals:

private slots:

signals:


};
#endif // WIDGET_H
