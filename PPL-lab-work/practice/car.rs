fn main() {
// Immutable reference
let mut name = "Alice";

println!(" name: {}", name);
let first_name = &mut name; // Immutable reference denoted by '&'
// Print the value using the immutable reference
println!("First name: {}", first_name);

println!(" name: {}", name);
*first_name = "Al00ice";
// Print the value using the immutable reference

println!("First name: {}", first_name);

println!(" name: {}", name);
//println!("firstname {}",first_name);
}

