<?php

namespace App\Console;

use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
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
            $this->browser
                 ->visit('https://www.google.com/')
                 ->value('.gNO89b');
        } finally {
            $this->browser->quit();
            $this->process->stop();
        }
    }
}
