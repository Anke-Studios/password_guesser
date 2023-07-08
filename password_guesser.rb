#encoding: utf-8

def generate_bigsmall(number)
  charset = Array('A'..'Z') + Array('a'..'z')
  Array.new(number) { charset.sample }.join
end
@bigsmall = Array("A".."Z") + Array("a".."z")
@bigsmall = @bigsmall.join
def generate_number(number)
  charset = Array(0..9)
  Array.new(number) { charset.sample }.join
end
@numbers = Array(0..9).join
def generate_strongcode(number)
  charset = Array('A'..'Z') + Array('a'..'z') + Array(0..9) + Array["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~", "@", " "]
  Array.new(number) { charset.sample }.join
end
@strongcode = Array('A'..'Z') + Array('a'..'z') + Array(0..9) + Array["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~", "@", " "]
@strongcode = @strongcode.join
def type_of_code
  @codetype = gets.strip
  if @codetype.to_s == "cancel"
    cancel
  end
  if @codetype.to_i == 0 || @codetype.to_i > 3
    puts "Write 1, 2 or 3"
    type_of_code
  else
    @codetype = @codetype.to_i
  end
end
def get_digits
  @digits = gets.strip
  if @digits.to_s == "cancel"
    cancel
  end
  if @digits.to_i == 0 || @digits.to_i > 30
    puts "Write a number from one to thirty."
    get_digits
  end
    @digits = @digits.to_i
end
def write_password
  @password = gets.strip
  unless @password.ascii_only?
    puts "Write password in ascii characters."
    write_password
  end
  unless @password.size == @digits
    puts "Write the password with correct number of characters (#{@digits})"
    write_password
  end
  @password = @password.to_s
  test_password
end
def test_password
  case @codetype
  when 1
    @password.to_s.each_byte {
    |pass_byte1|
    unless @bigsmall.include?(pass_byte1.chr)
      puts "Write the password in the correct type (only big and small letters)"
      write_password
    end
    }
    @gencode = generate_bigsmall(@digits)
  when 2
    @password.to_s.each_byte {
    |pass_byte2|
    unless @numbers.include?(pass_byte2.chr)
      puts "Write the password in the correct type (only numbers)"
      write_password
    end
    }
    @gencode = generate_number(@digits)
  when 3
    @password.to_s.each_byte {
    |pass_byte3|
    unless @strongcode.include?(pass_byte3.chr)
      puts "Write the password in the correct type (only big and small letters, numbers and ascii specials characters)"
      write_password
    end
    }
    @gencode = generate_strongcode(@digits)
  end
end
def cancel
  puts "\nDo you want to cancle? (yes/no)"
  answer = gets.strip.downcase
  if answer == "yes"
    exit
  else
    program
  end
end
def program
  puts "What type of code you want?\n1 -> big and small letters\n2 -> only numbers\n3 -> strong code (big and small letters, numbers and special characters)"
  type_of_code
  puts "How many digits you want?"
  get_digits
  puts "Write your password: (#{@digits}):"
  write_password
  i = 1
  while @gencode != @password
    test_password
    i += 1
    puts @gencode
  end
  puts "Your password is: #{@gencode}"
  puts "Number of attempts: #{i}"
  cancel
end
program