import re

regex = re.compile(
    r'(?P<host>(?:\d+\.){1,3}\d+)\s+-\s+'
    r'(?P<user_name>[\w+\-]+)?\s+'
    r'\[(?P<time>[-\w\s:/]+)\]\s+'
    r'"(?P<request>\w+.+?)"'
)

def names():
    simple_string = """Amy is 5 years Old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = r"[A-Z][a-z]+"
    name = re.findall(pattern, simple_string)

    return name
print(names())

def grades():
	with open("docs/grate.txt", "r") as file:
		grade = file.read()

	pattern = '([A-Z][a-z]+ [A-Z][a-z]+): B'
	grades = re.findall(pattern, grade)

	return grades

def logs():
    data = []

    with open("docs/logdata.txt", "r") as f:
        logdata = f.read()

        for item in regex.finditer(logdata):
            x = item.groupdict()

            if x["user_name"] is None:
                x["user_name"] = "-"

            data.append(x)
            
    return data

