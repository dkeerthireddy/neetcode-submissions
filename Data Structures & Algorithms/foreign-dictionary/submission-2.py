import collections, heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(set)
        inDeg={char:0 for word in words for char in word}

        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minLen=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDeg[w2[j]]+=1
                    break
        q=deque()
        for ch in inDeg:
            if inDeg[ch]==0:
                q.append(ch)
        res=[]
        while q:
            ch=q.popleft()
            res.append(ch)

            for nei in adj[ch]:
                inDeg[nei]-=1
                if inDeg[nei]==0:
                    q.append(nei)
        if len(res)<len(inDeg):
            return ""

        return "".join(res)
