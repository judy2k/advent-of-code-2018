use std::collections::HashSet;
use std::fs::File;
use std::io;
use std::io::prelude::*;

fn main() {
    let mut current_val = 0;
    let mut seen_vals = HashSet::new();
    for change in changes("../input.txt").expect("error").iter().cycle() {
        if seen_vals.contains(&current_val) {
            println!("{}", current_val);
            break;
        }
        seen_vals.insert(current_val);
        current_val += change;
    }
}

fn changes(path: &str) -> Result<Vec<i32>, io::Error> {
    let f = File::open(path)?;
    Ok(io::BufReader::new(f)
        .lines()
        .map(Result::unwrap)
        .map(|s| s.parse::<i32>().unwrap())
        .collect::<Vec<i32>>())
}
