# JavaScript `var`, `let`, and `const`

## Overview
In JavaScript, we use `var`, `let`, and `const` to declare variables. Each has different scoping rules, hoisting behavior, and mutability.

## 1. `var` (Function-Scoped)
- **Scope:** Function-scoped (not block-scoped)
- **Hoisting:** Variables are hoisted and initialized as `undefined`
- **Redeclaration:** Allowed
- **Reassignment:** Allowed

### Example:
```javascript
function testVar() {
    if (true) {
        var x = 10;
    }
    console.log(x); // ✅ Works (Function-scoped)
}
testVar();
```
**Output:**
```
10
```

#### Hoisting with `var`
```javascript
console.log(a); // ✅ Output: undefined (Hoisted)
var a = 5;
console.log(a); // Output: 5
```

---

## 2. `let` (Block-Scoped)
- **Scope:** Block-scoped (`{}`)
- **Hoisting:** Variables are hoisted but cannot be accessed before declaration (Temporal Dead Zone)
- **Redeclaration:** Not allowed in the same scope
- **Reassignment:** Allowed

### Example:
```javascript
function testLet() {
    if (true) {
        let y = 20;
    }
    console.log(y); // ❌ Error: y is not defined (Block-scoped)
}
testLet();
```

#### Hoisting with `let`
```javascript
console.log(b); // ❌ ReferenceError: Cannot access 'b' before initialization
let b = 10;
console.log(b);
```

---

## 3. `const` (Block-Scoped & Immutable)
- **Scope:** Block-scoped (`{}`)
- **Hoisting:** Variables are hoisted but cannot be accessed before declaration
- **Redeclaration:** Not allowed
- **Reassignment:** Not allowed

### Example:
```javascript
const z = 30;
z = 40; // ❌ Error: Assignment to constant variable
console.log(z);
```

#### `const` with Objects:
```javascript
const person = {
    name: "John",
    age: 25
};
person.age = 26; // ✅ Allowed (Object properties can be modified)
console.log(person.age); // Output: 26
```

---

## Key Differences
| Feature  | `var` | `let` | `const` |
|----------|-------|-------|---------|
| **Scope** | Function-scoped | Block-scoped | Block-scoped |
| **Hoisting** | Yes (initialized as `undefined`) | Yes (not accessible before declaration) | Yes (not accessible before declaration) |
| **Redeclaration** | ✅ Yes | ❌ No | ❌ No |
| **Reassignment** | ✅ Yes | ✅ Yes | ❌ No |

---

## Best Practices
- **Use `const`** by default unless you need to reassign a value.
- **Use `let`** if you know the variable will change.
- **Avoid `var`** in modern JavaScript development.

---

## Author
Created by Utkarsh  😊

