reveal:
	pandoc SLIDES.md -s --mathjax -i -t revealjs -o slides.html

dz:
	pandoc SLIDES.md -s --mathml -i -t dzslides -o slides.html

all: reveal

test: all
	i3b-browser slides.html
