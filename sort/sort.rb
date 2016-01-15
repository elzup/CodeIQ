
class Student
  include Comparable
  attr_accessor :x, :y, :z, :name
  def initialize(name, x, y, z)
    @name = name;
    @x = x;
    @y = y;
    @z = z;
  end

  def <=>(o)
    if @x != o.x
      return -(@x <=> o.x)
    elsif @y != o.y
      return -(@y <=> o.y)
    elsif @z != o.z
      return -(@z <=> o.z)
    end
    @name <=> o.name
  end

  def to_s
    [@name, @x, @y, @z].join(',')
  end
end

head = gets.chomp
students = []
while line = gets
  data = line.chomp.split(',')
  students << Student.new(data[0], data[1].to_i, data[2].to_i, data[3].to_i)
end
# p students

students.sort!

# output
puts head
students.each do |v|
  puts v.to_s
end

# name,english,japanese,math
# a,58,29,56
# b,64,86,18
# c,89,50,36
# d,89,50,84
# e,95,89,53
# f,64,99,43
# g,13,59,68
