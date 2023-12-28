require './compliment'
RSpec.describe Compliment, "#hello" do
  it "should return Hello" do
    hello = Compliment.new.hello
    expect(hello).to eq("hello")
  end
end