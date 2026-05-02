import collections, heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c: set() for w in words for c in w}
        inDeg = {c:0 for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)> len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDeg[w2[j]] +=1
                    break
        pq = [c for c in inDeg if inDeg[c] == 0]
        heapq.heapify(pq)
        res=[]

        while pq:
            ch = heapq.heappop(pq)
            res.append(ch)
            for nei in adj[ch]:
                inDeg[nei]-=1
                if inDeg[nei] == 0:
                    heapq.heappush(pq,nei)
        return "".join(res) if len(res) == len(inDeg) else ""
                

        adj = {c: set() for w in words for c in w}
        inDeg = {c:0 for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDeg[w2[j]]+=1
                    break
        pq = [c for c in inDeg if inDeg[c] == 0]
        heapq.heapify(pq)
        res=[]

        while pq:
            ch = heapq.heappop(pq)
            res.append(ch)
            for nei in adj[ch]:
                inDeg[nei]-=1
                if inDeg[nei] == 0:
                    heapq.heappush(pq,nei)
        return "".join(res) if len(res) == len(inDeg) else ""

        