// Define the struct
struct EvenNumbers {
    current: u32,
    limit: u32,
}

// Implement methods for EvenNumbers
impl EvenNumbers {
    fn new(limit: u32) -> Self {
        EvenNumbers { current: 0, limit }
    }
}

// Implement the Iterator trait
impl Iterator for EvenNumbers {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        self.current += 2; // Generate even numbers (2, 4, 6, ...)
        if self.current <= self.limit {
            Some(self.current)
        } else {
            None
        }
    }
}

// Demonstrate in main
fn main() {
    let even_numbers = EvenNumbers::new(20); // Limit set to 20

    for val in even_numbers.take(10) { // Print only the first 10 even numbers
        println!("{}", val);
    }
}
