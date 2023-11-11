#include <iostream>
#include <vector>

template <typename T>
struct Node
{
    Node *parent = nullptr;
    T value;
    int rank = 0;
};

template <typename T>
Node<T>* findRoot(Node<T> *node)
{
    while (node->parent)
    {
        node = node->parent;
    }
    return node;
}

template <typename T>
Node<T>* merge(Node<T> *first, Node<T> *second)
{
    Node<T> *firstRoot = findRoot(first);
    Node<T> *secondRoot = findRoot(second);
    Node<T> *newRoot, *toMerge;
    if (firstRoot->rank < secondRoot->rank)
        std::tie(newRoot, toMerge) = {secondRoot, firstRoot};
    else
        std::tie(newRoot, toMerge) = {firstRoot, secondRoot};
    toMerge->parent = newRoot;
    if (newRoot->rank == toMerge->rank)
        newRoot->rank++;
    return newRoot;
}

int main()
{
    int n,m;
    std::cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int k;
        std::cin >> k;
        int langs[k];
        for (int j = 0; j < k; j++)
            std::cin >> langs[j];
        Node<int> *currentNode = nullptr;
        for (int j = 0; j < k; j++)
        {
            Node<int> *newNode;
            newNode->value = langs[j];
            if (currentNode == nullptr)
            {
                currentNode = newNode;
                continue;
            }
            
        }
    }
}
