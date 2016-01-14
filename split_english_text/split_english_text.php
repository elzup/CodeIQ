<?php

$pattern = "#.*?([0-9]+|Mr|Ms|Mrs|Mt|)[.!?](\s|$)#";
$subject = trim(fgets(STDIN));

$lines = [];
if (preg_match_all($pattern, $subject, $m, PREG_SET_ORDER)) {
    # print_r($m);
    $newline = true;
    foreach ($m as $mun) {
        list($line, $check, $end) = $mun;
        if ($newline) {
            $lines[] = $line;
        } else {
            # echo $lines[count($lines) - 1];
            $lines[count($lines) - 1] .= $line;
        }
        $newline = $check == '';
    }
}
echo implode("\n", $lines) . PHP_EOL;
