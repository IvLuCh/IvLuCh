all:
	pandoc NOTES.md --mathjax -o notes.html

test: all
	brave-browser notes.html
