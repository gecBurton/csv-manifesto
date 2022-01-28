# CSV Manifesto

## CSV the means of production!

Anyone who has worked in tech for a non tech company, e.g. finance, banking, pharma etc will know that CSVs are ubiquitous!

[JSON](https://datatracker.ietf.org/doc/html/rfc8259)


This is both a blessing and curse. On the positive side CSVs vs json are:
1. table-like which is the most common data structure. 
2. terse, half the size of json
3. can be parsed line by line. 
4. well supported

However there is no credible CSV specification, as such everyone has their own take on what CSV really means they everytime you recieve a CSV from a gi... not going to work
see https://donatstudios.com/Falsehoods-Programmers-Believe-About-CSVs for a list


[rfc4180](https://datatracker.ietf.org/doc/html/rfc4180)  exists , but still too vague

https://www.w3.org/TR/tabular-data-primer/ exists but is far too complex

[webcsv](https://eaglebush.github.io/webcsv/) good but complex... requires a seperate schema

[ndjson](https://github.com/ndjson/ndjson-spec) line by line but not actually tabular, 

## specification

concerned with encoding only

there will be a 1:1 mapping to JSON

no ambiguity will be supported, e.g. there will only be one of encoding null, or a boolean.

strict subset of rfc4180


1. subset of rfc4180
2. utf8
3. \n delimeted
4. all rows will be formatted as a json array of primitives with the enclosing brakets removed
5. all rows will have the same number of elements
6. there will alsways be at least one row
7. the first row will always be considered as the header
8. the first row (header) will have unique elements

## implications


## example

```csv
"Name", "Sex", "Age", "Height (in)", "Consent Given"
"Alex",   "M",    41,          null,            true
"Bert",   "F",    42,          68.5,            null
"Carl",  null,    32,          70.0,           false
```
