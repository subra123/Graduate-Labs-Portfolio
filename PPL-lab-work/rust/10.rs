use std::fs;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut file = fs::create("output.txt")?;
    file.write_all(b"Hello, Rust!")?;
    Ok(())
}

