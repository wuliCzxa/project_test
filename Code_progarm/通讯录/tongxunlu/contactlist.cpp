#include "contactlist.h"

ContactList::ContactList(QObject *parent) : QObject(parent), head(nullptr), size(0)
{
}

ContactList::~ContactList()
{
    // 清空链表，释放内存
    while (head) {
        ContactNode *temp = head;
        head = head->next;
        delete temp;
    }
}

void ContactList::addContact(const QString &name, const QString &phone, const QString &qq, const QString &email)
{
    ContactNode *newContact = new ContactNode(name, phone, qq, email);
    if (isEmpty()) {
        head = newContact;
        head->prev = head;
        head->next = head;
    } else {
        ContactNode *last = head->prev;
        last->next = newContact;
        newContact->prev = last;
        newContact->next = head;
        head->prev = newContact;
    }
    size++;
}

void ContactList::deleteContact(const QString &name)
{
    ContactNode *toDelete = findNode(name);
    if (toDelete) {
        if (toDelete == head && size == 1) {
            delete toDelete;
            head = nullptr;
        } else {
            ContactNode *prevNode = toDelete->prev;
            ContactNode *nextNode = toDelete->next;
            prevNode->next = nextNode;
            nextNode->prev = prevNode;
            if (toDelete == head) {
                head = nextNode;
            }
            delete toDelete;
        }
        size--;
    }
}

QVector<ContactNode*> ContactList::findContacts(const QString &keyword)
{
    QVector<ContactNode*> result;
    if (isEmpty()) {
        return result;
    }

    ContactNode *current = head;
    do {
        if (current->name.contains(keyword, Qt::CaseInsensitive) ||
            current->phone.contains(keyword, Qt::CaseInsensitive) ||
            current->qq.contains(keyword, Qt::CaseInsensitive) ||
            current->email.contains(keyword, Qt::CaseInsensitive)) {
            result.push_back(current);
        }
        current = current->next;
    } while (current != head);

    return result;
}

QVector<ContactNode*> ContactList::getAllContacts() const
{
    QVector<ContactNode*> result;
    if (isEmpty()) {
        return result;
    }

    ContactNode *current = head;
    do {
        result.push_back(current);
        current = current->next;
    } while (current != head);

    return result;
}

bool ContactList::isEmpty() const
{
    return size == 0;
}

ContactNode* ContactList::findNode(const QString &name)
{
    if (isEmpty()) {
        return nullptr;
    }

    ContactNode *current = head;
    do {
        if (current->name.compare(name, Qt::CaseInsensitive) == 0) {
            return current;
        }
        current = current->next;
    } while (current != head);

    return nullptr;
}
