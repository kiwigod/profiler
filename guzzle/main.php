<?php

error_reporting(E_ALL ^ E_WARNING);

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client();
$res = $client->get('https://www.google.com/')
    ->getBody()
    ->getContents();

$dom = new DOMDocument();
$dom->loadHTML($res);
$dom->getElementsByTagName('title')->item(0)->textContent;
