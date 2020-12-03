all:
	pandoc NOTES.md -s --webtex -o notes.html

test: all
	brave-browser notes.html
