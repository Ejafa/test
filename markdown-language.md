---
description: learning markdown laguage
---

# Markdown language

this section will discuss on markdown laguage.markdown language is really a wartered down version of markup laguages. I think that's why it's called markdown maybe.

by the way, markdown may be warter downed version of other markup languages like html,xhtml etc. But most amazing fact of markdown language is that it is a superset of markup languages and it supports most of the tags of html language.

## Syntax \(Basics\)

### 1.paragraph

`blank line`

### 2.header

headers in markdown are similar to HTML

`hash[#] space[ ] text to make header 1`

similarly double hash \#\# for header 2 and so on till header 6

put 1-6 hashes to make header form 1 to 6

### 3. blockquote

 `>[space] blockquote`

> quotes of Albert Einstein
>
> Few are those who see with their own eyes and feel with their own hearts.
>
> Imagination is more important than knowledge. Knowledge is limited.Imagination encircles the world.
>
> Unthinking respect for authority is the greatest enemy of truth.
>
> Try not to become a man of success, but rather try to become a man of value.
>
> I am by heritage a Jew, by citizenship a Swiss, and by makeup a human being, and only a human being, without any special attachment to any state or national entity whatsoever.
>
> Great spirits have always encountered violent opposition from mediocre minds.
>
> Not everything that can be counted counts, and not everything that counts can be counted.
>
> Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.

you can also put other markdown elements in blockquote to make quote look cool.

`>[space]#[space]header 1 text`

paragraph in blockquote

`>[space] [blankline]`

> this is line in blockquote
>
> this is another line after making paragraph but in same blockquote

### 4. PHRASE EMPHASIS

Markdown uses asterisks and underscores to indicate spans of emphasis.

**normal emphasis**

 ``_`[nospace] this is inside emphasis`_ ``_`[nospace]`_

or,

 ``_`[nospace] this is inside emphasis`_ ``_`[nospace]`_

**output:** _this is inside emphasis_

**strong emphasis**

use  _or \_ two times. like \*_ or \_\_

### 5. Lists

like HTML,two kings of lists in markdown language:

1. unordered
2. ordered

**unordered** :

\[ \* , + , - \] can create bulleted lists, but they can't be mixed up

`[*][space]elements of lists`

* bullet 1
* bullet 2
* bullet 3

**ordered**

Ordered \(numbered\) lists use regular numbers, followed by periods

 `[number][.][space]elements`

1. item 1
2. item 2
3. item 3

paragraphed lists can be made.to do that we need to indent the lists properly

```text
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

```text
This is an [example link](http://example.com/).
```

this is [google](http://google.com)

```text
This is an [example link](http://example.com/ "With a Title").
```

this is [google](http://google.com)

**write emails and links**

```text
<http://google.com>
<username@mail.com>
```

[http://google.com](http://google.com)

[user@mail.com](mailto:user@mail.com)

**auto url linking**

```text
http://google.com
```

[http://google.com](http://google.com)

if you don't want auto linking then

```text
`http://google.com`
```

`http://google.com`

**Reference-style**

```text
I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].
```

I get 10 times more traffic from [Google](http://google.com/) than from [Yahoo](http://search.yahoo.com/) or [MSN](http://search.msn.com/).

### 7. Images

```text
![alt text](/path/to/img.jpg "Title")
```

![trying man!](.gitbook/assets/download.gif)

**Linking Images**

To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.

```text
[![An old rock in the desert](/images/hill.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
```

[![Shiprock, New Mexico by Beau Rogers](.gitbook/assets/hill.jpg)](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

### 8. Code

```text
`coding in here`
```

### 9. Horizontal Rules

```text
---
***
___
```

### 10. Escaping Characters

```text
\* Without the backslash, this would be a bullet in an unordered list.
```

\* Without the backslash, this would be a bullet in an unordered list.

very useful when\*write something\*like this.

### 11. Tables

```text
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

| Syntax | Description |
| :--- | :--- |
| Header | Title |
| Paragraph | Text |

to align text in table

```text
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

| Syntax | Description | Test Text |
| :--- | :--- | :--- |
| Header | Title | Here's this |
| Paragraph | Text | And more |

as it's hard to write \| and -- in making table,people often use [table generator](http://www.tablesgenerator.com/markdown_tables).

### 12. Fenced Code Blocks

three tick marks \(\`\`\`\) or three tildes \(~~~\) on the lines before and after the code block

```text
```
multiple lines of coding goes here
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
```

**Syntax Highlighting**

```text
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
```

```javascript
{
  "firstName": "Ejafa",
  "lastName": "Bassam",
  "University": "IU"
}
```

```text
```
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char** argv)
{
    printf("writing codes in c with this highlighting is cool");
    return(0);
}
```
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char** argv)
{
    printf("writing codes in c with this highlighting is cool");
    return(0);
}
```

### 13. Strikethrough

```text
~~The world is flat.~~ We now know that the world is round.
```

~~The world is flat.~~ We now know that the world is round.

### 14. Task Lists

```text
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

* [x] Write the press release
* [ ] Update the website
* [ ] Contact the media

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).

