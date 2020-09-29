const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        // executablePath: '/usr/local/bin/firefox'
        executablePath: '/usr/bin/chromium'
    });
    const page = await browser.newPage();
    await page.goto('https://www.google.com/');
    const title = await page.title();

    // console.log(title);

    await browser.close();
})();
