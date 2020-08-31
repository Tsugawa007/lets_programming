K,S = gets.split(" ").map(&:to_i)
c = 0
for i in 0..K do
  for j in 0..K do
    if S-(i+j)<= K && 0 <=S-(i+j) then
      c += 1
    end
  end
end
puts c
