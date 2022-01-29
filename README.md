# CSV Manifesto

CSVs are everywhere. If you have ever exported data from a website, or transfered
data between two systems, or consumed bespoke information from a business or a 
doctor or a school then there is a good chance that that data was formatted as CSV. 

And this can be a problem, because the CSV file format is notoriously hard to work with. 
Countless hours and untold costs have been lost trying to work out how to interpret the
contents of a CSV.

In this article I am going to explain what CSV is, why business users love it and why 
technologists loathe it. I am going to argue that a sensible, low cost compromise 
exists and that we should use it.

## what is CSV?

CSV stands for comma-separated-variables. It is a loose specification for how tabular 
data can be represented as text.

In CSV each line of the represents a row in the table, and each item in the row is 
separated by a comma as its name suggests.

Here is an example CSV:

```csv
first name, middle name(s), family name, children, age 
     Priya,               ,         Das,         ,   5 
     Keith, Joe,   Edwarad,       James,        1,   
```

## why CSVs are good

1. CSVs are easy to produce, all data tools can work with it, e.g. Excel. 
2. CSVs look like the tables they represent. The use new-lines and commas to 
   delimit rows and variables means that they can be easily read and edited by hand.
3. CSVs are typically half the size of other common data formats such as `xml` or `json`.
4. CSVs can be processed line-by-line without having to read the whole file at once. 
   This is why they are the default format for loading large data files into databases. 

All of this means that CSVs are great for ad-hoc data exchange: you give me some data
produced using your favourite software, and I can inspect it by eye and work out how 
to load it into my system without much effort.
   
## why CSVs are bad

CSVs become a problem when they are used in automated processes. Because there is 
no widely accepted working definition of what a CSV is this means that there is a
lot of room for (miss)interpretation of what the data in a CSV means. 

A long list of many of the pitfalls of CSVs can be found [here](https://donatstudios.com/Falsehoods-Programmers-Believe-About-CSVs).
In 10 years of working with data in banks, healthcare, and aerospace I have personally come
across at least half of these in the wild!

Some common examples are:

1. CSVs are often not comma delimited! Yes, even though CSV specifies only one thing, the comma,
   this is still open to interpretation. A good example of this is the UK's National-Health-
   Service's [public data downloads](https://assets.nhs.uk/prod/documents/NHS-Website-about-our-data-downloads.pdf)
   which, staggeringly, uses the Windows-1252 encoding of ¬ to separate its variables. 

2. Usually this first situation arises because the CSVs author wants to use the comma within a 
   variable, e.g. in the example above Keith has 2 middle names... or maybe he has one, and a child
   called James who is one year old... who knows?

3. Zero vs null, in the example given above Keith has no age and Priya has no children, a human
   understands that Keith's age is unknown but that Priya has zero children... or maybe she
   does, but we don't know?

All of this means that whilst it is easy to produce a CSV it is very hard to consume it. A great
deal of interpretation is required, this can be hard to do with a computer and is very prone to 
error.

## CSV the means of production!

It is a shame that we are in this mess because there is a lot to like about CSVs, moreover their 
shortcomings should be easy to overcome. What we need is a formal definition of what a CSV is, 
lets call it Strict-CSV, or `.scsv`, that is:

* recognizably still a CSV, such that it works with existing tools
* unambiguous to interpret

We wil base this on [JSON](https://datatracker.ietf.org/doc/html/rfc8259) which is a very
successful human-readable data format widely used to exchange and store data.

Our definition is:

1. `.scsv` is [utf8](https://en.wikipedia.org/wiki/UTF-8) encoded
2. rows are new-line, `\n`, delimited
3. variables are comma, `,`, delimited
4. all variables are encoded as JSON primitives, e.g:
   1. integers: `1`, `2`, `-3`
   2. floats: `1.2`, `-0.3`, `1e5`
   3. strings: `"my name is \"George\", I have 2 brothers"`
   4. booleans: `true`, `false`
   5. none: `null` 
5. all rows will have the same number of variables
6. the first row will be considered as the header
7. the first row will have unique elements

In this way our example CSV would be:

```csv
"first name", "middle name(s)", "family name", "children", "age" 
     "Priya",             null,         "Das",          0,    5 
     "Keith", "Joe,   Edwarad",       "James",          1,  null 
```

and we can finally confirm that Priya has no children but that Keith's age is unknown!

## Alternatives

Unsurprisingly there exist many alternative definitions of what a CSV should be. Here are
some of them and why I don't think they are effective.

* [rfc4180](https://datatracker.ietf.org/doc/html/rfc4180) This is the most common definition
  it is recommended by the [UK government](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard) 
  amongst others. Its principle problem is that it is still far too ambiguous to be useful. 

* [CSV on the Web](https://www.w3.org/TR/tabular-data-primer/) far far far too complicated!

* [webcsv](https://eaglebush.github.io/webcsv/) this allows for more or less any CSV standard but
  requires that the standard is defined in a separate schema. Whilst this works it seems 
  excessively burdensome for what should be a simple data-encoding.

* [ndjson](https://github.com/ndjson/ndjson-spec) this is very similar to what is being 
  proposed in this article but it is neither recognizably a CSV nor is it necessarily tabular.



