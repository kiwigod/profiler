var casper = require('casper').create();
casper.start('https://www.google.com/');

casper.then(function() {
    this.getTitle();
});

casper.run();
