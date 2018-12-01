use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() {
    let f = File::open("../input.txt").unwrap();
    println!(
        "{}",
        BufReader::new(f)
            .lines()
            .map(Result::unwrap)
            .map(|s| s.parse::<i32>().unwrap())
            .sum::<i32>()
    );
}
