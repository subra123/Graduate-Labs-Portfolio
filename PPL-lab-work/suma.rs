fn main() {
    let n = 10;
    let mut fib_sequence = vec![0, 1];

    for i in 2..n {
        let next_fib = fib_sequence[i - 1] + fib_sequence[i - 2];
        fib_sequence.push(next_fib);
    }

    println!("Fibonacci sequence: {}", fib_sequence);
}
