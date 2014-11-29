#!/bin/bash
rm -rf _build
mkdir _build
cp intro/index _build/index.md
max=20
for a in {1..20}
do
    this="$a";
    prev="";
    next="";
    if [ $a -gt 1 ]; then prev=`expr $a - 1`; fi
    if [ $a -lt $max ]; then next=`expr $a + 1`; fi    
    if [ ${#this} -eq 1 ]; then this="0$this"; fi
    if [ ${#prev} -eq 1 ]; then prev="0$prev"; fi
    if [ ${#next} -eq 1 ]; then next="0$next"; fi
    mkdir _build/lesson$this
    if [ -z prev ]; then pandoc -s -f markdown -t html --template=templates/template.html --variable=after:"lesson$next" -o _build/lesson$this/index.html lesson$this/instruction lesson$this/exercises;
    elif [ -z next ]; then pandoc -s -f markdown -t html --template=templates/template.html --variable=before:"lesson$prev" -o _build/lesson$this/index.html lesson$this/instruction lesson$this/exercises;
    else pandoc -s -f markdown -t html --template=templates/template.html --variable=before:"lesson$prev" --variable=after:"lesson$next" -o _build/lesson$this/index.html lesson$this/instruction lesson$this/exercises; fi
    echo "1. [- Title](/lesson$this/index.html)" >> _build/index.md
done
pandoc -s -f markdown -t html --template=templates/index.html -o _build/index.html _build/index.md
