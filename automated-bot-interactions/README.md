# Automated Bot Interactions

This repository contains a collection of mini projects implemented using Python and Selenium. Each project automates a specific task using web scraping and browser automation.

## Project 1: LinkedIn Job Application Automation

This project automates the job application process on `LinkedIn` for Python Developer roles (or any other role of your choice) using Selenium and Python.

### How to Use

Install the required libraries:

```bash
pip install selenium python-dotenv
```

Create a .env file in the project directory and add your `LinkedIn` credentials:

```env
USER_EMAIL=your_email@example.com
USER_PASSWORD=your_password
```

Run the main script:

```bash
python main.py
```

The script will login to `LinkedIn`, search for Python Developer jobs (or the role you specified), apply filters, and automate the job application process.

### Important

Make sure you have a phone number and a CV in your LinkedIn account

## Project 2: Wikipedia Articles Count

This script scrapes the total number of articles on `Wikipedia`.

### How to Use

Install the required libraries:

```bash
pip install selenium
```

Run the script:

```bash
python wikipedia_articles.py
```

The script will open `Wikipedia`, find the article count, print it, and close the browser.

## Project 3: Python.org Events Dictionary

This script scrapes the upcoming events from the `python.org` website and stores them in a dictionary.

### How to Use

Install the required libraries:

```bash
pip install selenium
```

Run the script:

```bash
python events_dictionary.py
```

The script will open `python.org`, find upcoming events, store them in a dictionary, print the dictionary, and close the browser.

## Project 4: Create Accounts

This script automates the account creation process on a sample website.

### How to Use

Install the required libraries:

```bash
pip install selenium
```

Run the script:

```bash
python create_accounts.py
```

The script will open the sample website, fill in the account creation form with test data, submit the form, and close the browser.

## Project 5: Cookie Clicker Game

This script automates clicking the cookie in the `Cookie Clicker` game for a specified amount of time.

### How to Use

Install the required libraries:

```bash
pip install selenium
```

Run the script:

```bash
python cookies_game.py
```

The script will open the `Cookie Clicker` game, click the cookie for 5 seconds, and then close the browser.

## License

This repository is licensed under the MIT License.
