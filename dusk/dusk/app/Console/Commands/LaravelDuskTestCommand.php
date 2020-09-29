<?php

namespace App\Console;

use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Illuminate\Console\Command;
use Laravel\Dusk\Browser;
use Laravel\Dusk\Chrome\SupportsChrome;
use Laravel\Dusk\Concerns\ProvidesBrowser;

class LaravelDuskTestCommand extends Command
{
    use ProvidesBrowser, SupportsChrome;

    protected $name = 'dusk:test';

    public function __construct()
    {
        parent::__construct();
        // static::startChromeDriver();
    }

    public function handle()
    {
        $this->browse(function (Browser $browser) {
            $res = $browser->visit('https://www.google.com/')
                ->value('.gNO89b');
            // dump($res);

            $browser->quit();
        });

        // static::stopChromeDriver();
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
            '--verbose',
            '--log-path=' . storage_path('logs/chromedriver.log'),
        ]);

        return RemoteWebDriver::create(
            'http://selenium-server:4444/wd/hub', DesiredCapabilities::chrome()->setCapability(
                ChromeOptions::CAPABILITY, $options
            )
        );
    }
}
