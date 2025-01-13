#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMessageBox>
#include <QRegularExpression>
#include "contactlist.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_addContactButton_clicked();
    void on_displayContactsButton_clicked();
    void on_deleteContactButton_clicked();
    void on_searchContactButton_clicked();

private:
    Ui::MainWindow *ui;
    ContactList *contactList;

    bool validatePhone(const QString &phone);
    bool validateEmail(const QString &email);
};

#endif // MAINWINDOW_H
