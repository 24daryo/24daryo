module hello_world

go 1.16

replace 1.hello_world/add => ./add

require 1.hello_world/add v0.0.0-00010101000000-000000000000 // indirect
