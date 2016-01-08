
// s 115
// u 117
// n 110
s = 115;
u = 117;
n = 110;
console.log(s&2);
console.log(u&2);
console.log(n&2);
console.log();
console.log((s&3)<2);
console.log((u&3)<2);
console.log((n&3)<2);
console.log();
console.log(s&2);
console.log(u&2);
console.log(n&2);
console.log();
console.log(s&u&2);
console.log(n&u&2);
console.log(n&s&2);
// TODO
console.log(s&u);
console.log(n&u);
console.log(n&s);
console.log(s&s);
console.log(n&n);
console.log(u&u);

console.log((s&u&5)<1);
console.log((n&u&5)<1);
console.log((n&s&5)<1);
console.log((s&s&5)<1);
console.log((n&n&5)<1);
console.log((u&u&5)<1);
