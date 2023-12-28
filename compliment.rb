class Compliment
  def initialize
  end

  def hello
    "hello"
  end

  def nine_compliment(input)
    length = input.digits.length
    nines = ("9" * length).to_i
    nines - input
  end
end