# text = """
# Python is great. Python is easy to learn.
# I love Python programming. Python makes coding fun.
# """

# import re
# from collections import Counter

# def word_analyzer(text):
#     pattern = r"\w+"

#     words = re.findall(pattern, text)

#     words_dict = Counter(words)
    
#     print("Output")
#     print(f"Total words: {len(words)}\n")
#     print("Word frequency")
#     for w, f in words_dict.items():
#         print(f"{w} -> {f}")
#     print("\n")
    
#     print("Top 5 words")
#     top_5 = words_dict.most_common(5)
#     for t in top_5:
#         word, freq = t
#         print(f"{word} -> {freq}")
       

# word_analyzer(text)


html = """
<html>
<body>
<h1>Welcome to Python</h1>
<p>This is a <b>bold</b> text.</p>
<img src="image.jpg" />
<a href="link.html">Click here</a>
</body>
</html>
"""

import re

def html_tag_remover(text):
    pattern = r"<[^>]+>"
    new_text = re.sub(pattern, "", text)
    return new_text.strip()

print(html_tag_remover(html))