#try making a grade card 
name = input("Enter your full name:")
print("enter your marks for each of the following subjects:")
python = int(input("Python marks:"))
HTML = int(input("HTML marks:"))
Java = int(input("Java marks:"))
CSS = int(input("CSS marks:"))
R_Programming = int(input("R programming marks:"))
total = python + HTML + CSS +Java + R_Programming

def get_grade(total):
    if total >= 400:
        return "A"
    elif total >= 300:
        return "B"
    elif total >= 200:
        return "C"
    elif total >= 100:
        return "D"
    else:
        return "FAIL"
    
grade = get_grade(total)

print(f"{'='*7} {'Swami Vivekananad college , kolhapur':^22} {'='*7}")
print(f"{'='*5} {name:^22} {'='*5}")
print(f"|{'subject':^13}|{'Marks':^8}|")
print(f"|{'Python':^13}|{python:^8}|")
print(f"|{'HTML':^13}|{HTML:^8}|")
print(f"|{'CSS':^13}|{CSS:^8}|")
print(f"|{'Java':^13}|{Java:^8}|")
print(f"|{'R Programming':^13}|{R_Programming:^8}|")
print(f"{'='*7}{'TOTAL:'}{total} {'='*7}")
print(f"{'='*7} {'GRADE:'}{grade} {'='*7}")
