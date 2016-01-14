<?php

$n = (int) trim(fgets(STDIN));
print(divs($n) . "\n");

function divs($n) {
    $i = 0;
    while ($n != 1) {
        if ($n % 2 == 0) {
            $n /= 2;
        } else {
            $n -= 1;
        }
        $i += 1;
    }
    return $i;
}
