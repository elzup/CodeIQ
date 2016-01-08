// var q = [['s', 'u', 'n'],
//      ['s', 'u', 'n'],
//      ['s', 'u', 'n']];

var q = 'sun\nsun\nsun';

var h = 0;
var w = 0;
var r = '';
for (var j = 0; j < 3; j ++) {
    console.log(q[j * 4 + 0]);
    console.log(q[j * 4 + 1]);
    console.log(q[j * 4 + 2]);
    if (q[j * 4 + 1] == 'u' && ('sns'.indexOf(q[j * 4 + 0] + q[j * 4 + 2]) != -1)) h++;
    if (q[1 * 4 + j] == 'u' && ('sns'.indexOf(q[0 * 4 + j] + q[2 * 4 + j]) != -1)) w++;
}
r = (h + w)*3 - h * w;
r = h + "" + w;


r = h + "" + w;
console.log(r);
r = (h + w)*3 - h * w;
console.log(r);

