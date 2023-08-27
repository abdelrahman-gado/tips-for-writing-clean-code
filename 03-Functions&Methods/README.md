# Functions & Methods

## What makes up a function?
1. Working with the function should be easy / readable (function body)
   - The length of the function body matters.
2. Calling the function should be readable. (function call)
   - The number and order of arguments matters. 

## The number of function / method parameters
- Minimize the number of parameters
  1. None parameters -> best possible option
  2.  `1` -> very good possible option
  3.  `2` -> use with caution
  4.  `3` -> avoid if possible
  5.  `> 3` -> always avoid

- Try to avoid output arguments - especially if they are unexpected


## Function Body
- Function should be small.
- Functions should do one thing
- Functions should do work that's one level of abstraction below their name.
- Keep Functions Short
- DRY - Don't Repeat Yourself - For reusability
- Use Common Sense (Question your code)
- Try Keeping Functions Pure 
  - (The same input always yields the same output)
  - No side effects
    - A side effect is an operation which does not just acts on function inputs and change the function output but **which instead changes the overall system / program state**
    - Side effects are not automatically bad - we do need them in our programs. But unexpected side effects should be avoided.
  
- Avoid unexpected Side Effects.
  - The name of a function should signal or imply that a side effects is likely to occur.

- Unit Testing helps (can you easily test a function?)


### The problem with multiple levels of abstraction
- High Level `isEmail(email)`
- Low Level `email.includes('@)`


