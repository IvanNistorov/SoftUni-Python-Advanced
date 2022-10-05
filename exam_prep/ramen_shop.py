from collections import deque

bowls_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bowls_ramen and customers:
    ramen_value = bowls_ramen.pop()
    customer_value = customers.popleft()

    if customer_value > ramen_value:
        customer_value -= ramen_value
        customers.appendleft(customer_value)

    elif ramen_value > customer_value:
        ramen_value -= customer_value
        bowls_ramen.append(ramen_value)

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {(', '.join([str(x) for x in customers]))}")
else:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_ramen])}")