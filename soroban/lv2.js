function f(i) {
    var r;
    r = i<10 ? i%10<5?"0"+i%5:"1"+i%5 :
        (i%100<50 ? i%10<5?"0"+ i/10%5-i/10%1+"0"+i%5:"1"+i/10%5-i/10%1+""+ i%5 : 0);
    return r;
}

print(f(1));
print(f(2));
print(f(6));
print(f(16));
print(f(14));
print(f(66));

