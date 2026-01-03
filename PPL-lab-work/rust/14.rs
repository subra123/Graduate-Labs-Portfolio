fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8];
    let evens: Vec<i32> = numbers.into_iter().filter(|x| x % 2 == 0).collect();
    println!("{:?}", evens);
}

