
def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    d = {}  # key:val = email:index
    from collections import defaultdict
    graph = defaultdict(list)  # graph connecting the indices of the same account
    for i, a in enumerate(accounts):
        for email in a[1:]:
            if email in d:
                graph[i].append(d[email])
                graph[d[email]].append(i)
            else:
                d[email] = i

    # dfs, return indices belong to the same account
    def dfs(i):
        tmp = [i]
        for j in graph[i]:
            if j not in seen:
                seen.add(j)
                tmp += dfs(j)
        return tmp

    seen = set()
    res = []
    for i in range(len(accounts)):
        if i in seen:
            continue
        res.append([accounts[i][0]] + sorted(set(email for j in dfs(i) for email in accounts[j][1:])))

    return res

if __name__ == '__main__':
    print(accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                         ["John", "johnsmith@mail.com", "john00@mail.com"],
                         ["Mary", "mary@mail.com"],
                         ["John", "johnnybravo@mail.com"]]))
