#include<queue>
using namespace std;
class Solution
{
    public:
    Node* mergeKLists(vector<Node*>& arr)
    {
        auto cmp = [](Node*a,Node*b){return a->data > b->data;};
        priority_queue<Node*, vector<Node*>,decltype(cmp)>pq(cmp);
        
        for(Node*head: arr)
            if(head)pq.push(head);
        Node* dummy = new Node(0);
        Node* tail= dummy;
        
        while(!pq.empty())
        {
            Node* curr = pq.top();pq.pop();
            tail->next=curr;
            tail=tail->next;
            if (curr->next)pq.push(curr->next);
        }
        return dummy->next;
    }
};