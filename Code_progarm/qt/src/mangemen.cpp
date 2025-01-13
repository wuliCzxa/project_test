#include "mangemen.h"

mangemen::mangemen(QWidget* parent)
    : QMainWindow(parent)
    , ui(new Ui_mangemen)
{
    ui->setupUi(this);
}

mangemen::~mangemen()
{
    delete ui; 
}