<?php

$secretKey = 'enter your secret key';
$publicKey = 'enter your public key';
$timestamp = time();
$payload = $timestamp . '.' . $publicKey;
$hash = hash_hmac('sha256', $payload, $secretKey, true);
$hexHash = array_shift(unpack('H*', $hash));
$signature = $payload . '.' . $hexHash;

$tickerUrl = "https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD"; // request URL
$aHTTP = array(
  'http' =>
    array(
    'method'  => 'GET',
  	)
);
$aHTTP['http']['header']  = "X-Signature: " . $signature;
$context = stream_context_create($aHTTP);
$content = file_get_contents($tickerUrl, false, $context);

echo $content;

?>