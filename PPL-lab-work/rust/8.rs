use std::io;

fn main() {
    let mut numbers = Vec::new();
    let mut input = String::new();

    println!("Enter numbers (0 to stop):");
    while let Ok(_) = io::stdin().read_line(&mut input) {
        let number: i32 = input.trim().parse().expect("Please enter a number");
        if number == 0 {
            break;
        }
        numbers.push(number);
        input.clear();
    }

    println!("Even numbers: {:?}", numbers.iter().filter(|&&x| x % 2 == 0).collect::<Vec<_>>());
}
