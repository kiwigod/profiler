<?php

error_reporting(E_ALL ^ E_WARNING);

$ch = curl_init("https://www.google.com/");

curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HEADER         => false
]);

$content = curl_exec($ch);
curl_close($ch);

$dom = new DomDocument();
$dom->loadHTML($content);
// Website will only contain 1 title
$title = $dom->getElementsByTagName('title')[0]->nodeValue;

var_dump($title);
