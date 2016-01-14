<?php

list($m, $n) = explode(" ", trim(fgets(STDIN)));
$m = (int) $m;
$hn = ((int) $n) / 2;

if ($m * 3 < $hn || $n % 2 == 1) {
    echo "error\n";
    exit();
}
$max = $m - ((int) ceil($hn / 3));
$min = $m - $hn;
echo $max . ' ' . $min;
echo PHP_EOL;
