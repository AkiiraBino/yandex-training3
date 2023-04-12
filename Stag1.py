N = int(input())
char_id = list(map(int, input().split(' ')))
line_id = list(map(int, input().split(' ')))
K = int(input())
text_id = list(map(int, input().split(' ')))

count = 0

line_to_char = {}

for i in range(N):
    line_to_char[char_id[i]] = line_id[i]

last_line = line_to_char.get(text_id.pop(0))

for char in text_id:
    if line_to_char.get(char) != last_line:
        last_line = line_to_char.get(char)
        count += 1

print(count)