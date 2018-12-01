use std::collections::HashSet;
use std::fs::File;
use std::io;
use std::io::prelude::*;

fn main() {
    let mut seen_vals = HashSet::new();
    for frequency in Frequencies::new(changes("../input.txt").expect("error")) {
        if seen_vals.contains(&frequency) {
            println!("{}", frequency);
            break;
        }
        seen_vals.insert(frequency);
    }
}

struct Frequencies {
    current: i32,
    changes: Vec<i32>,
    next_change: usize,
}

impl Frequencies {
    fn new(changes: Vec<i32>) -> Frequencies {
        Frequencies {
            current: 0,
            changes,
            next_change: 0,
        }
    }
}

impl Iterator for Frequencies {
    type Item = i32;
    fn next(&mut self) -> Option<i32> {
        let result = self.current;
        self.current += self.changes[self.next_change];
        self.next_change = (self.next_change + 1) % self.changes.len();
        Some(result)
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
