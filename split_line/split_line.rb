n, m = gets.chomp.split(',').map &:to_i
k = [n]
t = 0
while k.length > 0
  kn = Array.new
  k.sort!
  [k.length, m].min.times do |i|
    v = k.pop
    if v == 2
      next
    elsif v == 3
      kn << 2
      next
    end
    kn << v / 2
    if v % 2 == 0
      kn << v / 2
    else
      kn << v / 2 + 1
    end
  end
  k.concat(kn)
  t += 1
  p k
end
puts t
