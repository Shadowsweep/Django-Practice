// Objects
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 25,
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
};
console.log(person.fullName()); // Output: John Doe

// Arrays

let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // Output: Apple
fruits.push("Mango"); // Adds an item
console.log(fruits);
