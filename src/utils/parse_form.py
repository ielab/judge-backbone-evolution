from bs4 import BeautifulSoup

html_content = open("/Users/uqgzucc1/.gemini/antigravity/brain/4b8052c0-9ed9-4ce0-a713-c80d9904903c/.system_generated/steps/4/content.md").read()
soup = BeautifulSoup(html_content, 'html.parser')
for i, el in enumerate(soup.find_all('div', role='heading')):
    print(f"Heading {i}: {el.text}")
print("-----")
for i, el in enumerate(soup.find_all('div', class_='M7eMe')):
    print(f"div M7eMe {i}: {el.text}")
