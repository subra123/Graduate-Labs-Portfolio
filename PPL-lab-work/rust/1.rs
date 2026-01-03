use std::io;

fn main(){
    let mut ip = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut ip).unwrap();
    let num : i32 = ip.trim().parse().unwrap();

    if num % 2 == 0 {
        println!("This is Even");
    } else{
        println!("This is odd");
    }
}
