<?php

$n = trim(fgets(STDIN));
$users = array();
while ($line = trim(fgets(STDIN))) {
    list($a, $b) = explode(" ", trim($line));
    @$users[$a][] = $b;
    @$users[$b][] = $a;
}
# print_r($users);
$max = 0;
for ($i=1; $i < $n; $i++) {
    for ($j=$i + 1; $j <= $n; $j++) {
        $a = $users[$i];
        $b = $users[$j];
        $li = array_merge($a, $b);
        $max = max($max, count($li) - count(array_unique($li)));
    }
}
print($max);
