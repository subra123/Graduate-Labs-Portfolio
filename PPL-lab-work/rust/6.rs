fn extract_first_word(sentence: &str) -> &str {
    let bytes = sentence.as_bytes();
    
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &sentence[..i];
        }
    }
    sentence
}

fn main() {
    let sentence = "Rust is fast and safe.";
    let first_word = extract_first_word(sentence);
    
    println!("Extracted word: {}", first_word);
    
    let modified_sentence = &sentence[first_word.len()..].trim();
    println!("Modified string: {}", modified_sentence);
}
