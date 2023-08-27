# Control Structures & Errors

## Keep Your Control Structures Clean
- Avoid Deep Nesting
- Using Factories functions & polymorphism
- prefer positive checks (more easy to understand)
- utilize errors

## How you can make code structure clean?
1. use guards and fail fast.
    ```js
        if (!email.includes('@')) {
            return;
        } 
    ```

2. Embrace Errors and Error Handling
   1. Throwing + handling errors can replace if statements and lead to more focused functions.
   2. if something is an error, make it error.
   3. Error handling is one thing when we talk about functions that do one thing.