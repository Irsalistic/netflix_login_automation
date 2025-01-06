# Netflix Login Automation tool

A Python-based security testing tool that demonstrates automated login testing using Selenium WebDriver. This tool is designed for educational purposes and legitimate security testing of your own applications.

## ⚠️ Important Disclaimer

This tool is for **educational and authorized testing purposes only**. Always:
- Obtain explicit permission before testing any system
- Only test systems you own or have authorization to test
- Follow responsible disclosure practices
- Comply with all applicable laws and terms of service

## Features

- Automated login attempt simulation
- Configurable timing delays to prevent rate limiting
- Headless browser operation
- Detailed logging of test results
- Support for both email and phone number formats
- Random delays to simulate human interaction

## Requirements

- Python 3.7+
- Chrome browser
- Required Python packages:
  - selenium
  - webdriver_manager
  - fake_useragent

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install selenium webdriver-manager fake-useragent
```

## Configuration

Create a credentials file with test accounts in the following format:
```
email@example.com:password
```

## Usage

1. Update the `credentials_file_path` in the script to point to your test credentials file
2. Run the script:
```bash
python netflix_automate.py
```

## Output

Results are saved to `login_results.txt` in the format:
```
(email, password, result)
```

## Best Practices for Security Testing

1. Always obtain proper authorization before testing
2. Document all testing activities
3. Use dedicated test accounts
4. Respect rate limits
5. Monitor resource usage
6. Keep logs secured

## Code Structure

- `read_credentials()`: Parses credential file
- `random_delay()`: Implements timing controls
- `check_login()`: Performs login attempts
- `main()`: Orchestrates the testing process

<span style="color: red">**Note:**
- Always edit read_credential function according to the structure of your credentials file
## Contributing

Feel free to submit issues and enhancement requests. Please follow responsible security testing practices.

## License

This project is intended for educational purposes only. Use responsibly.