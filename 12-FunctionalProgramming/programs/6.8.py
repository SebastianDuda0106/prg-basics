results=[37,51,44,23,78,92,39,84,83,51]

passed=lambda y:list(filter(lambda x:x>y,results))

print(passed(70))
print(passed(40))
print(passed(30))