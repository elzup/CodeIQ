# a, b = input(), input()

# lib = {}
# (12..15).each do |n|
#   lib[21.to_s(n)] = 33.to_s(n)
# end

a = gets.chomp
lib = {"19"=>"29", "18"=>"27", "17"=>"25", "16"=>"23"}
puts lib[a]
