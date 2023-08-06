## Selenium-recaptcha-solver

This package is used to solve recaptcha challenges when 
using a Selenium web driver for web automation tasks.

It supports single-step and multi-step audio solving for ReCAPTCHA audio challenges.

**Note:** ReCAPTCHA may detect automated queries if you're solving multiple ReCAPTCHA challenges in a row or not using a hard-to-detect web driver. If you need a hard-to-detect web driver, I recommend you use the one I link below. Make sure that if you're using a headless web driver, you set a non-headless user agent (I've also placed the one I usually use below)!

User-agent: Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36

Hard-to-detect web driver: https://github.com/ultrafunkamsterdam/undetected-chromedriver

## Requirements 

Python 3.7+

Main dependencies:
  <ul>
    <li>SpeechRecognition python package to transcribe speech</li>
    <li>Pydub for file conversions</li>
</ul>

This solver uses audio transcription to automatically solve ReCAPTCHA challenges, so you need to have FFmpeg installed on your machine and in your PATH (If using windows) or installed on your machine (For Linux or MacOS).

Guide for installing FFmpeg on Windows: https://phoenixnap.com/kb/ffmpeg-windows
Guide for installing FFmpeg on Linux: https://www.tecmint.com/install-ffmpeg-in-linux/
Guide for installing FFmpeg on MacOS: https://phoenixnap.com/kb/ffmpeg-mac

## Installation

```bash
python -m pip install selenium-recaptcha-solver
```

## Usage

```python
from selenium_recaptcha_solver import RecaptchaSolver
import undetected_chromedriver as webdriver


test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument(f'--user-agent={test_ua}')

# Example driver, the API works for any browser
driver = webdriver.Chrome(options=options)

# Create API object and bind it to your webdriver
api_client = RecaptchaSolver(driver=driver)

# Fetch random web page
driver.get('https://foo.bar.com')

# Get example iframe web element
iframe = driver.find_element(
    by='foo', 
    value='bar',
)

# Solve ReCAPTCHA using API (Usually used for ReCAPTCHA challenges or invisible ReCAPTCHA V2 - The ones that pop up from clicking a button or from another action done by the user)
api_client.solve_recaptcha_v2(iframe=iframe)

# Or solve a ReCAPTCHA V2 visible (The one where you have to click a checkbox - If a challenge pops up after the click it's automatically resolved)
api_client.click_recaptcha_v2(iframe=iframe)

# Write the rest of your operations to do after solving the Captcha
```

You can check a detailed use case in the tests folder of this project (Its execution is shown below in the demonstration chapter).

## Demonstration
[![Image from Gyazo](https://i.gyazo.com/858ceb5df9f43f6aafadf69e233cd2d1.gif)](https://gyazo.com/858ceb5df9f43f6aafadf69e233cd2d1)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
