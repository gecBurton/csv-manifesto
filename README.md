# CSV Manifesto

CSVs are everywhere. If you have ever exported data from a website, or transfered
data between two systems, or consumed bespoke information from a business, 
doctor or school then there is a good chance that that data was formatted as CSV. 

This can be a problem, because the CSV format is notoriously hard to work with. 

In this article I explain what CSV is, why business users love it and why 
technologists loathe it. A sensible, low cost compromise 
exists, we should use it.

## what is CSV?

CSV stands for comma-separated-variables. It is a loose specification for how tabular 
data can be represented as text.

In CSV each line of the represents a row in the table, and each item in the row is 
separated by a comma as its name suggests.

Here is an example CSV:

```csv
first name, middle name(s), family name, children, age 
Priya     ,               , Das        ,         ,  32 
Keith     , Joe,   Edwarad, James      ,        1,   
```

## why CSV is good

1. CSV is simple to produce, most tools support it, e.g. Excel. 
2. CSV formatted data looks like the table it represents. The use of new-lines and commas to 
   delimit rows and variables means that it can easily be read and edited by hand.
3. CSV formatted data is typically half the size of other common data formats such as `xml` or `json`.
4. CSV can be processed line-by-line without having to read the whole file at once. 
   This is why it is the default format for loading large data files into databases. 

All of this means that CSV is great for ad-hoc data exchange: you give me some data
produced using your favourite software, and I can inspect it by eye and work out how 
to load it into my system without much effort.
   
## why CSV is bad

CSV becomes a problem when it is used in automated processes. Because there is 
no widely accepted working definition of what a CSV is this means that there is a
lot of room for (miss)interpretation of what the data in a CSV means. 

A long list of many of the pitfalls of CSVs can be found [here](https://donatstudios.com/Falsehoods-Programmers-Believe-About-CSVs).

Some common examples are:

1. CSV is often not comma delimited! Yes, even though CSV specifies only one thing, the comma,
   this is still open to interpretation. A good example of this is the UK National Health Service's [public data downloads](https://assets.nhs.uk/prod/documents/NHS-Website-about-our-data-downloads.pdf)
   which, staggeringly, uses the [Windows-1252 encoding of ¬](https://bytetool.web.app/en/ascii/code/0xac/) to separate its variables. 

2. Usually this first situation arises because the author of the CSV wants to use the comma within a 
   variable, e.g. in the example above Keith has 2 middle names... or maybe he has one, and a child
   called James who is one year old... who knows?

3. Zero vs null, in the example given above Keith has no age and Priya has no children, a human
   understands that Keith's age is unknown but that Priya has zero children... or maybe she does have some but this data is missing?

All of this means that whilst it is easy to produce a CSV it is very hard to consume it. A great
deal of interpretation is required, this can be hard to do with a computer and is very prone to 
error.

## CSV the means of production!

It is a shame that we are in this mess because there is a lot to like about CSV, moreover its 
shortcomings should be easy to overcome. What we need is a formal definition of what a CSV is, 
lets call it Strict-CSV, or `.scsv`, that is:

* recognizably still CSV, such that it works with existing tools
* unambiguous to read and write

We will base this on [JSON](https://datatracker.ietf.org/doc/html/rfc8259) which is a very
successful human-readable data format widely used to exchange and store data.

Our definition is:

1. The file is [utf8](https://en.wikipedia.org/wiki/UTF-8) encoded. 
2. Rows are new-line, `\n`, delimited. 
3. Variables are comma, `,`, delimited. 
4. All variables are encoded as JSON primitives, e.g:
   1. integers: `1`, `2`, `-3`
   2. floats: `1.2`, `-0.3`, `1e5`
   3. strings: `"my name is \"George\", I have 2 brothers"`
   4. booleans: `true`, `false`
   5. none: `null` 
5. All rows will have the same number of variables. 
6. The first row will be considered as the header. 
7. The first row will have unique elements. 

In this way our example CSV would be:

```csv
"first name", "middle name(s)", "family name", "children", "age" 
     "Priya",             null,         "Das",          0,   32 
     "Keith", "Joe,   Edwarad",       "James",          1, null 
```

and we can finally confirm that Priya has no children but that Keith's age is unknown!

## Alternatives

Unsurprisingly there exist many alternative definitions of what a CSV should be. Here are
some of them and why I don't think they are effective.

* [rfc4180](https://datatracker.ietf.org/doc/html/rfc4180) is the most common definition. 
  It is recommended by the [UK government](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard) 
  amongst others. Its principle problem is that it is still too ambiguous to be useful. 

* [CSV on the Web](https://www.w3.org/TR/tabular-data-primer/) is far far too complicated!

* [webcsv](https://eaglebush.github.io/webcsv/) allows for more or less any CSV standard but
  requires that the standard is defined in a separate schema. Whilst this works it seems 
  excessively burdensome for what should be a simple data-encoding.

* [ndjson](https://github.com/ndjson/ndjson-spec) is very similar to what is being 
  proposed in this article but it is neither recognizably a CSV nor is it necessarily tabular.



