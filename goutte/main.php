<?php

require __DIR__ . '/vendor/autoload.php';

use Goutte\Client;

$client = new Client();
$crawler = $client->request('GET', 'https://www.google.com/');

$crawler->filter('title')->first()->text();
