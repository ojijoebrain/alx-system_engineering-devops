#!/usr/bin/env ruby
## using reg ex to validate a 10 digit phone number

puts ARGV[0].scan(/^[0-9]{10}/).join
