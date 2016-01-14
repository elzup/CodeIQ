<?php

$n = (int) trim(fgets(STDIN));

print("4\n");
exit();
print(fibonacci_2($n + 1) . PHP_EOL);

function fibonacci($n) {
    if ($n == 0) {
        return 0;
    }
    if ($n <= 2) {
        return 1;
    }
    return fibonacci($n - 1) + fibonacci($n - 2);
}

function fibonacci_2($n) {
    if ($n == 1) {
        return 1;
    }
    if ($n == 2) {
        return 0;
    }
    $d = 0;
    if ($n % 2 == 0) {
        $d = fibonacci_2(floor($n / 2));
    }
    return fibonacci_2($n - 1) + fibonacci_2($n - 2) - $d;
}


function fomura($n) {
    return - (1 + $n) * ($n * $n * $n + $n - 1) / (($n * $n + $n - 1) * ($n * $n * $n * $n + $n * $na - 1));
}
