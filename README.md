# Heroku Playwright Tests 🎭

Automated UI test suite for [The Internet](https://the-internet.herokuapp.com) 
using **Playwright** and **Python**.

## 📋 Test Coverage
- ✅ Login (valid, invalid, empty fields)
- ✅ Dropdown (select by value, by label)
- ✅ Checkboxes (check, uncheck, verify state)
- ✅ iFrames (TinyMCE editor interactions)

## 🛠️ Tech Stack
- Python 3.x
- Playwright
- Pytest

## ⚙️ Setup & Installation

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/heroku-playwright-tests.git
cd heroku-playwright-tests

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install browsers
playwright install

## ▶️ Run Tests

# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py -v

# Run with visible browser
pytest --headed

# Run in slow motion
pytest --headed --slowmo 1000
