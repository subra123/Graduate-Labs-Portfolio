// Define a custom iterator for even numbers
struct EvenNumbers {
    current: u32,
    limit: u32,
}

// Implement the Iterator trait for EvenNumbers
impl Iterator for EvenNumbers {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current > self.limit {
            return None; // Stop when the limit is reached
        }

        let next_even = self.current;
        self.current += 2; // Move to the next even number

        Some(next_even)
    }
}

// Function to create a new EvenNumbers iterator
fn even_numbers(limit: u32) -> EvenNumbers {
    EvenNumbers { current: 2, limit }
}

fn main() {
    println!("First 10 even numbers:");

    // Create an EvenNumbers iterator up to 20
    let even_iter = even_numbers(20);

    // Print the first 10 even numbers
    for num in even_iter.take(10) {
        println!("{}", num);
    }
}
