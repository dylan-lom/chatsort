.SILENT:

TERM=dumb

java:
	cp sorter.source sorter.java
	bash -c 'set -o pipefail; java sorter.java 2>&1 | sed "s/sorter.java/sorter.source/g"'

rust:
	rustc sorter.source
	./sorter

go:
	cp sorter.source sorter.go
	bash -c 'set -o pipefail; go run sorter.go 2>&1 | sed "s/sorter.go/sorter.source/g"'

lisp:
	clisp -q sorter.source

ruby:
	ruby sorter.source

javascript:
	node sorter.source

bash:
	bash sorter.source

haskell:
	runghc sorter.source

python:
	python3 sorter.source

c++:
	c++ -o sorter.bin -x c++ sorter.source
	./sorter.bin

c:
	cc -o sorter.bin -x c sorter.source
	./sorter.bin

clean:
	rm -f sorter.bin

