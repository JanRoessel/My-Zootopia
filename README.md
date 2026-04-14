A simple Python project that fetches animal data from an API and generates a structured HTML website based on the results.

The project is split into two main components:

📦 Data Fetcher (API layer)
🌐 Website Generator (HTML builder)

This separation ensures a clean and scalable architecture.

🚀 Features
Fetch animal data from the API Ninjas Animals API
Clean separation between data and presentation logic
Safe dictionary access using .get()
Generates an HTML file from a template
Simple CLI input (search animals directly)
Modular and extendable architecture


Project structure:

workspace/
│
├── data_fetcher.py          # Fetches data from API
├── animals_web_generator.py # Generates HTML website
├── animals_template.html    # HTML template
├── animals.html             # Output file (generated)
├── .env                     # API key storage


Install dependencies:

pip install requests python-dotenv

How to run:

python animals_web_generator.py

