#pragma once
#include "ui_mangemen.h"
#include <QMainWindow>

class mangemen : public QMainWindow {
    Q_OBJECT
    
public:
    mangemen(QWidget* parent = nullptr);
    ~mangemen();

private:
    Ui_mangemen* ui;
};