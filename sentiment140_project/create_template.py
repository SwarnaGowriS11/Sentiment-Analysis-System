import os

# create templates folder if it does not exist
if not os.path.exists("templates"):
    os.makedirs("templates")

# path for index.html
html_path = os.path.join("templates", "index.html")

# write a simple html template
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>Sentiment Analysis</h1>
    <form method="post" action="/predict">
        <textarea name="text" rows="5" cols="40" placeholder="Enter your text here..."></textarea><br><br>
        <button type="submit">Analyze</button>
    </form>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ templates/index.html created successfully!")
