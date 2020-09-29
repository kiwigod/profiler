const webdriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const chrome = require('selenium-webdriver/chrome');

const options = new firefox.Options();
options.headless();
options.addArguments("--no-sandbox");
options.addArguments("--disable-dev-shm-usage");


(async () => {
    let driver = await new webdriver.Builder()
        .forBrowser('firefox')
        .setFirefoxOptions(options)
        // .setChromeOptions(options)
        .build();
    try {
        await driver.get('https://www.google.com/');
        await driver.getTitle().then((title) => {
            console.log(title);
        });
    } finally {
        await driver.quit();
    }
})();
