---
description: Notes on Rust programming language
---

# Rust

## Common Programming Concepts

### Keywords and Identifiers

In rust keywords can't be used as variable or function name. This is same for all identifiers in rust. But if you need to use an identifier that has the same name as the keywords then you can use the keyword as **raw identifier.**  Raw identifiers start with `r#`

```rust
let r#fn = "this variable is named 'fn' even though that's a keyword";

// call a function named 'match'
r#match();

let r#let = "chill bro!";
println!("{}",r#let); // will print r#let value
```

#### Variables and Mutability

In rust by default variables are immutable. This helps the programmer to check a certain portion of code for finding bugs. It also helps in concurrency too. This will cause error:

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);
    x = 6; // x will not be able to assign 6 in x
           // this will cause error
    println!("The value of x is: {}", x);
}
```

To make any variable mutable we have to use  `mut` :

```rust
let mut a = "hello world";
a = "this can be changed";
println!("{}",a);
```

but you have make sure the type of the variable must match with the type of the changed variable:

```rust
let mut a = "ha ha";
a = "you can do this";
a = 12; //sorry this will give error coz a takes String not integer
```

#### Difference between constant in rust and variable

The concept of immutable variable of rust is similar to the concept of `const` in other programming languages. But rust

