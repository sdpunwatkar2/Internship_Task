## problem 2: The Captain's Room

K = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)

print((sum(room_set) * K - sum(rooms)) // (K - 1))
