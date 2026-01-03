use std::fs;

fn main() {
    let content = fs::read_to_string("output.txt").expect("Failed to read file");
    println!("{}", content);

    let mut word_c =1;
    for cha in content.chars() {
        if cha == ' '{
            word_c+=1;
        } 
    }
    println("{}",word_c);
}

