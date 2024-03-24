#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
# Manage Flask package using pip
python::pip { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
