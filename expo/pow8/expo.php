<?php

define("LIMIT", 100000000);
//$filename = "./sample.in.txt";
$filename = "./testdata.in.txt";

$lines = explode(PHP_EOL, file_get_contents($filename));
foreach ($lines as $line) {
    list($base, $exp) = explode(' ', $line);
    if ($base == 0 && $line == 0) {
        break;
    }
    echo pow8($base, $exp) . PHP_EOL;
}

function pow8($base, $exp) {
    $ps = split_pow2($exp);
    $base_k = $base % LIMIT;
    $res = array_shift($ps) ? $base_k : 1;
    foreach ($ps as $n) {
        $base_k = ($base_k * $base_k) % LIMIT;
        if (!$n) {
            continue;
        }
        $res = ($base_k * $res) % LIMIT;
    }
    return $res;
}

/**
 * 2のべき乗数の和に分解
 */
function split_pow2($n) {
    $i = 1;
    while ($i * 2 <= $n) {
        $i *= 2;
    }
    $nums = array();
    while ($i >= 1) {
        if ($nums[] = $n >= $i) {
            $n -= $i;
        }
        $i /= 2;
    }
    $nums = array_reverse($nums);
    return $nums;
}
