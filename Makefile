.SILENT:

TERM=dumb

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

