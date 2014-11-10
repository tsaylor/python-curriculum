#!/bin/bash
rm -rf build
mkdir build
touch toc.html
for i in $( ls | grep lesson ); do
    mkdir build/$i
    pandoc -s -f markdown -t html --template=templates/template.html.tmpl --variable=before:$i --variable=after:$i -o build/$i/index.html $i/instruction $i/exercises
    echo "<a href=\"$i/index.html\">$i</a><br>" >> build/index.html
done
