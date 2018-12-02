extern crate day01;

use std::collections::HashSet;
use std::fs::File;
use std::io;
use std::io::prelude::*;

use day01::AggregateTrait;

fn main() {
    println!("{}", calculate_result("../input.txt").unwrap())
}

fn int_file(path: &str) -> Result<Vec<i32>, io::Error> {
    let f = File::open(path)?;
    Ok(io::BufReader::new(f)
        .lines()
        .map(Result::unwrap)
        .map(|s| s.parse::<i32>().unwrap())
        .collect::<Vec<i32>>())
}


fn calculate_result(path: &str) -> Result<i32, io::Error> {
    let mut seen_vals = HashSet::new();
    for frequency in vec!(0 as i32).into_iter().chain(int_file(path)?.into_iter().cycle()).aggregate() {
        if seen_vals.contains(&frequency) {
            return Ok(frequency);
        }
        seen_vals.insert(frequency);
    }
    panic!("Should never reach this point")
}


#[test]
fn test_calculate_result() {
    assert_eq!(calculate_result("../sample_input.txt").unwrap(), 2);
    assert_eq!(calculate_result("../input.txt").unwrap(), 55250);
}
