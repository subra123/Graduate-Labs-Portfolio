use std::fs;

fn main() {
    let content = fs::read_to_string("output.txt").expect("Failed to read file");
    println!("{}", content);
    let mut word=1;
    for i in content.chars() {
        if i == ' '{
            word+=1;
        }
    }
    println!("{}",word);
}

