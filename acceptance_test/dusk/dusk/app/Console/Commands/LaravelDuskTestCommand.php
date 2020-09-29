<?php

namespace App\Console;

use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;
use Illuminate\Console\Command;
use Laravel\Dusk\Browser;
use Laravel\Dusk\Concerns\ProvidesBrowser;

class LaravelDuskTestCommand extends Command
{
    use ProvidesBrowser;

    protected $name = 'dusk:test';

    public function handle()
    {
        $this->browse(function (Browser $browser) {
            try { $this->something($browser); }
            finally { $browser->quit(); }
        });
    }

    private function something(Browser $browser)
    {
        // login, navigate settings, change phonenumber
        $browser->visit('https://app-dev.rosterbuster.aero/')
                ->type('email', env('RB_USER'))
                ->type('signInPassword', env('RB_PW'))
                ->clickLink('Sign in', 'button')
                ->waitFor('.user-avatar')
                ->click('#user-drop-down')
                ->clickLink('Settings')
                ->value('input[name="profile.phonenumber"]', '')  // clear input field
                ->type('profile.phonenumber', random_int(10000, 99999));

        // submit form
        $saveBtn = $browser->driver->findElement(WebDriverBy::cssSelector('div.form-group > button'));
        $saveBtn->click();
        // busy wait; dusk doesn't support wait for enable/disable element
        while (!$saveBtn->isEnabled()) {}

        $browser->storeSource('/app/donkeysource')
                ->screenshot('/app/donkey');
    }

    /**
     * Create the RemoteWebDriver instance.
     *
     * @return \Facebook\WebDriver\Remote\RemoteWebDriver
     */
    protected function driver()
    {
        $options = (new ChromeOptions)->addArguments([
            '--headless',
            '--window-size=1920,1080',
            '--disable-dev-shm-usage'
        ]);

        return RemoteWebDriver::create(
            'http://selenium-server:4444/wd/hub', DesiredCapabilities::chrome()->setCapability(
                ChromeOptions::CAPABILITY, $options
            )
        );
    }
}
