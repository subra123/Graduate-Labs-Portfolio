
use std::io;

fn main(){
    let mut ip = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut ip).unwrap();
    let num : i32 = ip.trim().parse().unwrap();
    let mut i=1;
    while i<num {
        if i % 2 ==0 {
            println!("{}",i);
        }
        i+=1;
    }
}
