import re

content = 'Hello 123 4567 World_This is a Regex Demo'
#
# result = re.match('^Hello\s(\d+)\s(\d+)\sWorld',content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.span())


content = 'Hello 123 4567 World_This is a Regex Demo'

result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))

content = '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)

print(result.group())