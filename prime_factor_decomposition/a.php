<?php

$asn_list = array();
for ($i = 1000; $i < 10000; $i++) {
    if (sum_degits($i) == count_pfd($i) - 1) {
        $asn_list[] = $i;
    }
}
echo implode(PHP_EOL, $asn_list);

/* get_pfds 関数のテスト
for ($i = 2; $i < 100; $i++) {
    $ps = get_pfds($i);
    echo $i . ': ' . implode('x', $ps) . '=' . array_product($ps) . PHP_EOL;
}
 */

/**
 * count prime factor decomposition
 * 素因数の数を返す
 *
 * @param $num int 対象の数値
 * @return int 素因数の数
 */
function count_pfd($num) {
    return count(get_pfds($num));
}

/**
 * count prime factor decomposition
 * 素因数の数を返す
 *
 * @param $num int 対象の数値
 * @return int[] 素因数の配列
 */
function get_pfds($num) {
    $num_tmp = $num;
    $min_limit = 2;
    $cs = array();
    while ($p = first_prime($num, $min_limit)) {
        while ($num_tmp % $p == 0) {
            $cs[] = $p;
            $num_tmp /= $p;
        }
        $min_limit = $p + 1;
    }
    if ($num_tmp != 1) {
        $cs[] = $num_tmp;
    }
    return $cs;
}

/**
 * 最初の素因数を返す
 * ない場合はNULL
 * @param $num int 対象の数値
 * @param $min_limit int 下限値
 * @return int|bool 素因数|NULL
 */
function first_prime($num, $min_limit) {
    if ($min_limit == 2 && $num % 2 == 0) {
        return 2;
    }
    $start = floor($min_limit / 2) * 2 + 1;
    $end = sqrt($num);
    for ($i = $start; $i <= $end; $i+= 2) {
        if ($num % $i == 0) {
            return $i;
        }
    }
    return FALSE;
}

/**
 * 各桁の和を返す
 *
 * @param $num int 対象の数値
 * @return int 素因数の数
 */
function sum_degits($num) {
    return array_sum(str_split($num));
}
