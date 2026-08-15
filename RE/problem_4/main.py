import re

text = "Great session today! Thanks @john_doe and @alice_smith for the insights.#Python #Regex #CodingLife Let's meet again @bob_92 #Learning"


hashTagsExp = r"#[A-Za-z0-9]+"
mentionExp = r"@[A-Za-z_0-9]+"

hashTags = re.findall(hashTagsExp, text)
mentions = re.findall(mentionExp, text)

print("Hastages: ", hashTags)
print("Mentions: ", mentions)

