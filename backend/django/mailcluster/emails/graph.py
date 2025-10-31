from collections import defaultdict, deque
from .models import Email
class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)         # adjacency list
        self.adjMatrix = defaultdict(lambda: defaultdict(int))
        self.threadGraph = defaultdict(list)     # email_id -> reply/forward edges
        self.nextThreadId = 100

    def getNextThreadId(self):
        self.nextThreadId += 1
        return self.nextThreadId - 1

    def addEdge(self, fromEmail, toEmail, thread_id):
        found = False
        for edge in self.adjList[fromEmail]:
            if edge["to"] == toEmail:
                edge["weight"] += 1
                found = True
                break
        if not found:
            self.adjList[fromEmail].append({"to": toEmail, "weight": 1, "thread_id": thread_id})
        self.adjMatrix[fromEmail][toEmail] += 1

    def sendEmail(self, from_addr, to_addr, subject, body):
        threadId = self.getNextThreadId()
        self.addEdge(from_addr, to_addr, threadId)

        email = Email.objects.create(
            sender=from_addr,
            receiver=to_addr,
            subject=subject,
            body=body,
            thread_id=threadId,
            parent_email=None
        )
        return email

    def replyEmail(self, email_id, from_addr, to_addr, body):
        try:
            original = Email.objects.get(email_id=email_id)
        except Email.DoesNotExist:
            return None
        if from_addr != original.receiver or to_addr != original.sender:
            return "ERROR"

        reply_subject = "Re: " + original.subject
        self.addEdge(from_addr, to_addr, original.thread_id)


        reply = Email.objects.create(
            sender=from_addr,
            receiver=to_addr,
            subject=reply_subject,
            body=body,
            thread_id=original.thread_id,
            parent_email=original
        )

        self.threadGraph[original.email_id].append({
            "toEmailId": reply.email_id,
            "relation": "reply"
        })
        return reply

    def forwardEmail(self, email_id, from_addr, to_addr, body):
        try:
            original = Email.objects.get(email_id=email_id)
        except Email.DoesNotExist:
            return None
        if (from_addr != original.receiver and from_addr != original.sender):
            return "ERROR"

        fwd_subject = "Fwd: " + original.subject
        self.addEdge(from_addr, to_addr, original.thread_id)

        fwd = Email.objects.create(
            sender=from_addr,
            receiver=to_addr,
            subject=fwd_subject,
            body=body+"\n"+original.body,
            thread_id=original.thread_id,
            parent_email=original
        )

        self.threadGraph[original.email_id].append({
            "toEmailId": fwd.email_id,
            "relation": "forward"
        })
        return fwd

    def viewThread(self, rootEmailId):
        try:
            root = Email.objects.get(email_id=rootEmailId)
            while root.parent_email is not None:
                root=root.parent_email
            rootEmailId=root.email_id
        except Email.DoesNotExist:
            return []
        result = []
        q = deque([rootEmailId])
        visited = set([rootEmailId])

        while q:
            curr = q.popleft()
            e = Email.objects.get(email_id=curr)
            result.append({
                "email_id": e.email_id,
                "from": e.sender,
                "to": e.receiver,
                "subject": e.subject,
                "body": e.body,
                "parent_email_id": e.parent_email.email_id if e.parent_email else None
            })

            for edge in self.threadGraph[curr]:
                if edge["toEmailId"] not in visited:
                    q.append(edge["toEmailId"])
                    visited.add(edge["toEmailId"])
        return result
    
    def showgraph(self):
        print("Adjency List: ")
        for from_email, edges in self.adjList.items():
            print(f"{from_email} -> {edges}")
        
        print("\n Thread Graph")
        for email_id,edges in self.threadGraph.items():
            print(f"{email_id} -> {edges}")
        