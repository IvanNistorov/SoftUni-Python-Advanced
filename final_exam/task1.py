from collections import deque

eggs_size = deque([int(x) for x in input().split(", ")])
papers_size = deque([int(x) for x in input().split(", ")])
filled_boxes = 0

while eggs_size and papers_size:
    egg = eggs_size.popleft()
    if egg <= 0:
        continue
    paper = papers_size.pop()

    if egg == 13:
        left_paper = papers_size.popleft()
        papers_size.appendleft(paper)
        papers_size.append(left_paper)
        continue

    if 0 < egg + paper <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size])}")
if papers_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_size])}")

