var webPage = require('webpage');
var page = webPage.create();

page.open('http://www.google.com/', function(status) {
    page.title;
    phantom.exit();
});
