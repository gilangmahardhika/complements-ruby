require './compliment'
RSpec.describe Compliment, "#hello" do
  it "should return Hello" do
    hello = Compliment.new.hello
    expect(hello).to eq("hello")
  end
end

RSpec.describe Compliment, "#nine_compliment" do
  it "should return 123 for 876 9's compliment" do
    nine_comp = Compliment.new.nine_compliment(876)
    expect(nine_comp).to eq(123)
  end
end