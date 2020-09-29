const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const firefox = require('selenium-webdriver/firefox');

const options = new chrome.Options();
options.headless();
options.addArguments("--no-sandbox");
options.addArguments("--window-size=1920,1080");
options.addArguments("--disable-dev-shm-usage");


(async () => {
    let driver = await new webdriver.Builder()
        .forBrowser('chrome')
        // .setFirefoxOptions(options)
        .setChromeOptions(options)
        .build();
    try {
        // browse and login
        await driver.get('https://app-dev.rosterbuster.aero/');
        await driver.findElement(webdriver.By.name('email')).sendKeys('<EMAIL>');
        await driver.findElement(webdriver.By.name('signInPassword')).sendKeys('<PASS>');
        await driver.findElement(webdriver.By.css('button[type="submit"]')).click();

        // go to settings
        await driver.wait(webdriver.until.elementLocated(webdriver.By.className('user-avatar')), 3000);
        await driver.findElement(webdriver.By.id('user-drop-down')).click();
        await driver.findElement(webdriver.By.linkText('Settings')).click();

        // change the phonenumber
        let inputPhoneNumber = await driver.findElement(webdriver.By.css('input[name="profile.phonenumber"]'));
        for (i=0;i<100;i++) {
            await inputPhoneNumber.sendKeys(webdriver.Key.BACK_SPACE);
        }
        await inputPhoneNumber.sendKeys(Math.floor((Math.random() * 99999) + 10000));

        // save the form
        let buttonSaveForm = await driver.findElement(webdriver.By.css('div.form-group > button'));
        buttonSaveForm.click();
        await driver.wait(webdriver.until.elementIsEnabled(buttonSaveForm, 3000));

        await driver.getPageSource().then((src) => {
            require('fs').writeFile('/app/donkey.txt', src, 'utf8', (err) => { if(err) console.log(err); });
        });

        await driver.takeScreenshot().then((img) => {
            require('fs').writeFile('/app/donkey.png', img, 'base64', (err) => { if(err) console.log(err); });
        });
    } finally {
        await driver.quit();
    }
})();
