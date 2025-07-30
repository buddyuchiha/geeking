a = [(1, '{"id": 1, "name": "USD"', 2), ('b', '{"id": 1, "name": "USD"', 2)]
result = []
for i in a:
    res = dict(i)
    result.append(res)

print(result)