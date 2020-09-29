const { remote } = require('webdriverio');

(async () => {
    const browser = await remote({
        logLevel: 'debug',
        hostname: 'selenium-server',
        capabilities: {
            browserName: 'chrome'
        }
    });

    await browser.url('https://www.google.com');
    
    console.log(await browser.getTitle());

    await browser.deleteSession();
})().catch((e) => console.error(e));
