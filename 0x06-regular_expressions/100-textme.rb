#!/usr/bin/env ruby
## using reg ex to retrive text information

puts ARGV[0].scan(/\[from:.(.?)\] \[to:(.?)\] \[flags:(.?)\]/).join(",")
