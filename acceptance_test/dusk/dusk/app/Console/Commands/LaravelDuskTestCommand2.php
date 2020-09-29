<?php

namespace App\Console;

use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;
use Illuminate\Console\Command;
use Laravel\Dusk\Browser;
use Laravel\Dusk\Chrome\ChromeProcess;

class LaravelDuskTestCommand2 extends Command
{
    protected $name = 'dusk:test2';
    private $process;
    private $options;
    /** @var callable $driver */
    private $driver;
    private $browser;

    public function __construct() {
        parent::__construct();

        $this->process = (new ChromeProcess)->toProcess();
        $this->process->start();
        $this->options = (new ChromeOptions)->addArguments(['--disable-gpu', '--headless', '--disable-dev-shm-usage', '--no-sandbox']);
        $capabilities = DesiredCapabilities::chrome()->setCapability(ChromeOptions::CAPABILITY, $this->options);
        $this->driver = retry(5, function () use ($capabilities) {
            return RemoteWebDriver::create('http://localhost:9515', $capabilities);
        }, 50);
        $this->browser = new Browser($this->driver);
    }

    public function handle() {
        try {
            // login, navigate settings, change phonenumber
            $this->browser->visit('https://app-dev.rosterbuster.aero/')
                ->type('email', env('RB_USER'))
                ->type('signInPassword', env('RB_PW'))
                ->clickLink('Sign in', 'button')
                ->waitFor('.user-avatar')
                ->click('#user-drop-down')
                ->clickLink('Settings')
                ->value('input[name="profile.phonenumber"]', '')  // clear input field
                ->type('profile.phonenumber', random_int(10000, 99999));

            // submit form
            $saveBtn = $this->browser->driver->findElement(WebDriverBy::cssSelector('div.form-group > button'));
            $saveBtn->click();
            // busy wait; dusk doesn't support wait for enable/disable element
            while (!$saveBtn->isEnabled()) {}

            $this->browser->storeSource('/app/donkeysource')
                    ->screenshot('/app/donkey');
        } finally {
            $this->browser->quit();
            $this->process->stop();
        }
    }
}
