import requests
from bs4 import BeautifulSoup
import re

# Fetch the website content
# Replace this with the website URL you want to analyze
url = 'https://jayeshbhushan.me/'
response = requests.get(url)
html_content = response.text

# Extract and preprocess the text
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text(strip=True)
preprocessed_text = re.sub('<[^<]+?>', '', text)

# Vectorize the preprocessed text
vectorized_text = vectorizer.transform([preprocessed_text])

# Make predictions using the trained model
predictions = model.predict(vectorized_text)

# Interpret the results
if predictions[0] == 1:
    print("Potential XSS detected!")
else:
    print("No XSS detected.")
