#!/usr/bin/env ruby
## accepts one arg and uses regular expression matching method

puts ARGV[0].scan(/hbt{2,5}n/).join
