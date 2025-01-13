#ifndef CONTACTLIST_H
#define CONTACTLIST_H

#include <QObject>
#include <QVector>

struct ContactNode {
    QString name;
    QString phone;
    QString qq;
    QString email;
    ContactNode *prev;
    ContactNode *next;

    ContactNode(const QString &n, const QString &p, const QString &q, const QString &e)
        : name(n), phone(p), qq(q), email(e), prev(nullptr), next(nullptr) {}
};

class ContactList : public QObject
{
    Q_OBJECT
public:
    explicit ContactList(QObject *parent = nullptr);
    ~ContactList();

    void addContact(const QString &name, const QString &phone, const QString &qq, const QString &email);
    void deleteContact(const QString &name);
    QVector<ContactNode*> findContacts(const QString &keyword);
    QVector<ContactNode*> getAllContacts() const;

private:
    ContactNode *head;
    int size;

    bool isEmpty() const;
    ContactNode *findNode(const QString &name);
};

#endif // CONTACTLIST_H
