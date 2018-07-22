---
description: learning markdown laguage
---

# Markdown language

this section will discuss on markdown laguage.markdown language is really a wartered down version of markup laguages. I think that's why it's called markdown maybe.

by the way, markdown may be warter downed version of other markup languages like html,xhtml etc. But most amazing fact of markdown language is that it is a superset of markup languages and it supports most of the tags of html language.

## Syntax (Basics)

### 1.paragraph

```blank line```

### 2.header

headers in markdown are similar to HTML

<code>hash[#] space[ ] text to make header 1</code>

similarly double hash ## for header 2 and so on till header 6

put 1-6 hashes to make header form 1 to 6

### 3. blockquote

<code> >[space] blockquote </code>

> quotes of Albert Einstein 

> Few are those who see with their own eyes and feel with their own hearts.

> Imagination is more important than knowledge. Knowledge is limited.Imagination encircles the world.

>Unthinking respect for authority is the greatest enemy of truth.

>Try not to become a man of success, but rather try to become a man of value.


>I am by heritage a Jew, by citizenship a Swiss, and by makeup a human being, and only a human being, without any special attachment to any state or national entity whatsoever.

>Great spirits have always encountered violent opposition from mediocre minds.

>Not everything that can be counted counts, and not everything that counts can be counted.

>Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.

you can also put other markdown elements in blockquote to make quote look cool.

<code>>[space]#[space]header 1 text</code>

paragraph in blockquote

<code>>[space] [blankline]</code>

>this is line in blockquote
>
>this is another line after making paragraph but in same blockquote

### 4. PHRASE EMPHASIS

Markdown uses asterisks and underscores to indicate spans of emphasis.

__normal emphasis__

<code> * [nospace] this is inside emphasis [nospace] *</code>

or,

<code> _ [nospace] this is inside emphasis [nospace] _</code>

__output:__
*this is inside emphasis*

__strong emphasis__

use * or _ two times. like ** or __

### 5. Lists

like HTML,two kings of lists in markdown language:

1. unordered
2. ordered

__unordered__ :

[ * , + , - ] can create bulleted lists, but they can't be mixed up

<code>[*][space]elements of lists</code>

* bullet 1
* bullet 2
* bullet 3

__ordered__

Ordered (numbered) lists use regular numbers, followed by periods

<code> [number][.][space]elements </code>

1. item 1
2. item 2
3. item 3

paragraphed lists can be made.to do that we need to indent the lists properly

```[number][.][tab/space]elements

[blank line]

[indentation]elements

```

1. item 1

    with item 1.1
    
    with item 1.2
2. item 2

    with item 2.2

etc...

### 6. Links

```
This is an [example link](http://example.com/).
```
this is [google](http://google.com)

```
This is an [example link](http://example.com/ "With a Title").
```
 this is [google](http://google.com "title of google")


**write emails and links**
```
<http://google.com>
<username@mail.com>
```
<http://google.com>

<user@mail.com>

**auto url linking**
```
http://google.com
```
http://google.com

if you don't want auto linking then

```
`http://google.com`
```
`http://google.com`

**Reference-style**

```
I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"
```
I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"


### 7. Images

```
![alt text](/path/to/img.jpg "Title")
```
![this is alternative text for just do it](/images/just_do_it.gif "just do it man!")

**Linking Images**

To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.

```
[![An old rock in the desert](/images/hill.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
```
[![An old rock in the desert](/images/hill.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


### 8. Code
```
`coding in here`
```

### 9. Horizontal Rules

```
---
***
___
```

### 10. Escaping Characters
```
\* Without the backslash, this would be a bullet in an unordered list.
```
\* Without the backslash, this would be a bullet in an unordered list.

very useful when\*write something\*like this.

### 11. Tables

```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

works same as 

| Syntax | Description |
| --- | ----------- |
| Header | Title |
| Paragraph | Text |

```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

to align text in table
```
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

as it's hard to write | and -- in making table,people often use [table generator](http://www.tablesgenerator.com/markdown_tables "table generator online").

### 12. Fenced Code Blocks

three tick marks (```) or three tildes (~~~) on the lines before and after the code block

~~~
```
multiple lines of coding goes here
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
~~~

**Syntax Highlighting**

~~~
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
~~~
```json
{
  "firstName": "Ejafa",
  "lastName": "Bassam",
  "University": "IU"
}
```
~~~
```
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char** argv)
{
    printf("writing codes in c with this highlighting is cool");
    return(0);
}
```
~~~
~~~c
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char** argv)
{
    printf("writing codes in c with this highlighting is cool");
    return(0);
}
~~~

### 13. Strikethrough

```
~~The world is flat.~~ We now know that the world is round.
```
~~The world is flat.~~ We now know that the world is round.

### 14. Task Lists

```
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media


<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
