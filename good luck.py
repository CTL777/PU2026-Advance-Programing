T = int(input())

for t in range(1, T + 1):
    pages = []
    max_relevance = -1

    for _ in range(10):
        url, relevance = input().split()
        relevance = int(relevance)
        pages.append((url, relevance))
        max_relevance = max(max_relevance, relevance)

    print(f"Case #{t}:")
    for url, relevance in pages:
        if relevance == max_relevance:
            print(url)
