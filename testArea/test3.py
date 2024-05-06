def count_lines(text):
    lines = text.splitlines()
    return len(lines)

# Example usage:
text = """This is a sample text
with multiple lines
to demonstrate counting lines"""

num_lines = count_lines(text)
print("Number of lines:", num_lines)
