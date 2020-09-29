const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        // executablePath: '/usr/bin/chromium'
        executablePath: '/usr/bin/google-chrome'
    });
    try {
        // login
        const page = await browser.newPage();
        await page.goto('https://app-dev.rosterbuster.aero/');
        await page.type('input[name="email"]', '<EMAIL>');
        await page.type('input[name="signInPassword"]', '<PASS>');
        await page.click('button[type="submit"]');

        // goto settings
        await page.waitForSelector('.user-avatar');
        await page.click('#user-drop-down');
        await page.$x('//a[contains(text(), "Settings")]').then(async (selectors) => {
            if (selectors.length > 0) {
                selectors[0].click();
            }
        });

        // change phone number
        await page.waitForSelector('.upload-avatar');
        await page.click('input[name="profile.phonenumber"', {clickCount: 3});
        await page.type('input[name="profile.phonenumber"', Math.floor((Math.random() * 99999) + 10000).toString());
        await page.click('.submit-btn');
        await page.waitForFunction("document.querySelector('.submit-btn').disabled == false", {timeout: 5000});

        // save screenshot and source
        await page.screenshot({ path: '/app/donkey.jpg', type: 'jpeg' });
        await page.content().then(async (source) => {
            require('fs').writeFile('/app/donkey.txt', source, 'utf8', (err) => { if(err) console.log(err); });
        });
    } finally {
        await browser.close();
    }
})();
