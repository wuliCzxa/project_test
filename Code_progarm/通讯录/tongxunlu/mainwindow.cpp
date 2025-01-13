#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    contactList = new ContactList();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete contactList;
}

void MainWindow::on_addContactButton_clicked()
{
    QString name = ui->nameLineEdit->text().trimmed();
    QString phone = ui->phoneLineEdit->text().trimmed();
    QString qq = ui->qqLineEdit->text().trimmed();
    QString email = ui->emailLineEdit->text().trimmed();

    if (name.isEmpty() || phone.isEmpty() || qq.isEmpty() || email.isEmpty()) {
        QMessageBox::warning(this, "添加联系人", "请输入完整的联系人信息");
        return;
    }

    if (!validatePhone(phone)) {
        QMessageBox::warning(this, "添加联系人", "手机号格式不正确");
        return;
    }

    if (!validateEmail(email)) {
        QMessageBox::warning(this, "添加联系人", "邮箱格式不正确");
        return;
    }

    contactList->addContact(name, phone, qq, email);
    QMessageBox::information(this, "添加联系人", "联系人添加成功");
    ui->nameLineEdit->clear();
    ui->phoneLineEdit->clear();
    ui->qqLineEdit->clear();
    ui->emailLineEdit->clear();
}

void MainWindow::on_displayContactsButton_clicked()
{
    ui->contactsTextEdit->clear();
    QString displayText;
    QVector<ContactNode*> contacts = contactList->getAllContacts();
    for (ContactNode *contact : contacts) {
        displayText += QString("姓名: %1, 手机: %2, QQ: %3, 邮箱: %4\n")
                .arg(contact->name)
                .arg(contact->phone)
                .arg(contact->qq)
                .arg(contact->email);
    }
    ui->contactsTextEdit->setText(displayText);
}

void MainWindow::on_deleteContactButton_clicked()
{
    QString name = ui->deleteNameLineEdit->text().trimmed();
    if (name.isEmpty()) {
        QMessageBox::warning(this, "删除联系人", "请输入要删除的联系人姓名");
        return;
    }

    contactList->deleteContact(name);
    ui->deleteNameLineEdit->clear();
}

void MainWindow::on_searchContactButton_clicked()
{
    QString keyword = ui->searchLineEdit->text().trimmed();
    if (keyword.isEmpty()) {
        QMessageBox::warning(this, "查询联系人", "请输入要查询的关键字");
        return;
    }

    QString displayText;
    QVector<ContactNode*> contacts = contactList->findContacts(keyword);
    for (ContactNode *contact : contacts) {
        displayText += QString("姓名: %1, 手机: %2, QQ: %3, 邮箱: %4\n")
                .arg(contact->name)
                .arg(contact->phone)
                .arg(contact->qq)
                .arg(contact->email);
    }
    ui->contactsTextEdit->setText(displayText);
}

bool MainWindow::validatePhone(const QString &phone)
{
    QRegularExpression regex("^1[3456789]\\d{9}$");
    return regex.match(phone).hasMatch();
}

bool MainWindow::validateEmail(const QString &email)
{
    QRegularExpression regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
    return regex.match(email).hasMatch();
}
