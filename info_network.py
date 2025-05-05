import datetime

now = datetime.datetime.now()

print("Lovely Rusco")
print("231-0179")
print(now)

issue = input("networking issue: ")

file = open("./network_issue.txt", "a")

file.write(issue + "/n")

file.close

