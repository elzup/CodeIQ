while line = gets
  line.match(/\d{1,3}\.([a-z]{2,9})/) do |m|
    puts "1. #{m[1]}"
  end
end
