# frozen_string_literal: true

require 'set'
require 'benchmark'

def part1(changes)
  changes.sum
end

def part2(changes)
  frequencies = Set.new
  value = 0
  loop do
    changes.each do |change|
      value += change
      if frequencies.include? value
        return value
      else
        frequencies.add value
      end
    end
  end
end

lines = File.readlines('inputs/01')
changes = lines.map(&:to_i)

p part1(changes)
p part2(changes)

total_seconds = 0
n = 5000
n.times do
  start = Time.now
  part2(changes)
  total_seconds += (Time.now - start)
end

puts "Mean over #{n} runs: #{(total_seconds / n) * 1000}ms"
