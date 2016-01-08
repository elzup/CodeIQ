<?php

define('FORMAT_PRINT', '%Y%,%X%');
//define('FORMAT_PRINT', '%Y%,%X% = %C%');
$filename_csv = "./gutenberg.csv";
$search_text = "STAY HUNGRY, STAY FOOLISH";

// コマンドライン引数から実行
if (isset($argv[1])) {
    $filename_csv = $argv[1];
}
if (isset($argv[2])) {
    $search_text = $argv[2];
}

$gm = new GutenManager($filename_csv, $search_text);
try {
    $gm->run();
    echo $gm;
//    $gm->result_test();
} catch (Exception $e) {
    echo 'caught Exception: ' . $e->getMessage();
}

class GutenManager {
    private $search_text;
    private $filename_csv;
    private $char_list;
    private $queues;
    private $result_data_list;

    public function __construct($filename_csv, $search_text) {
        $this->filename_csv = $filename_csv;
        $this->search_text = $search_text;
    }

    public function run() {
        $this->_initialize_queue();
        $this->_searching();
    }

    private function _initialize_queue() {
        $this->char_list = get_csv($this->filename_csv);
        $this->queues = GutenManager::create_queues($this->char_list);
    }

    private function _searching() {
        $search_chars = str_split($this->search_text);
        $this->result_data_list = array();
        foreach ($search_chars as $c) {
            if (!$data = @array_shift($this->queues[$c])) {
                throw new Exception('文字が足りません');
            }
            $this->result_data_list[] = $data;
        }
    }

    /**
     * 二次配列からをDataキュー作成
     * @param $char_list string[][]
     */
    public static function create_queues($char_list) {
        $queues = array();
        foreach ($char_list as $y => $chars) {
            foreach ($chars as $x => $c) {
                if (!isset($queues[$c])) {
                    $queues[$c] = array();
                }
                $queues[$c][] = new Data($x, $y, $c);
            }
        }
        return $queues;
    }

    public function result_test() {
        $strs = array();
        foreach ($this->result_data_list as $data) {
            if (!isset($this->char_list[$data->y][$data->y])) {
                throw new Exception("テスト失敗 Index");
            }
            $strs[] = $this->char_list[$data->y][$data->x];
        }
        $res = implode('', $strs);
        echo '検索テキスト: ' . $this->search_text . PHP_EOL;
        echo 'テスト結果　: ' . $res . PHP_EOL;
        echo '[' . ($res == $this->search_text ? "一致" : "不一致") . ']';
    }

    public function __tostring() {
        return implode(PHP_EOL, $this->result_data_list);
    }
}

class Data {
    public $x;
    public $y;
    public $char;

    public function __construct($x, $y, $char) {
        $this->x = $x;
        $this->y = $y;
        $this->char = $char;
    }

    public function __tostring() {
        return strtr(FORMAT_PRINT, array('%X%' => $this->x, '%Y%' => $this->y, '%C%' => $this->char));
    }
}

/**
* csvファイルを読み込み二次配列を返す
* @param $filename string
* @return string[][]
*/
function get_csv($filename) {
    $h = fopen($filename, 'r');
    $datas = array();
    while ($data = fgetcsv($h)) {
        $datas[] = $data;
    }
    fclose($h);
    return $datas;
}

