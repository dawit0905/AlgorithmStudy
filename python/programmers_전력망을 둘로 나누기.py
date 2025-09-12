def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(graph)

    def dfs(curr, visited, v2):
        visited[curr] = 1
        count = 1

        for neighbor in graph[curr]:
            if not visited[neighbor] and neighbor != v2:
                count += dfs(neighbor, visited, v2)

        return count

    for v1, v2 in wires:
        visited = [False] * (n + 1)
        count = dfs(v1, visited, v2)

        diff = abs(count - (n - count))
        answer = min(answer, diff)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
