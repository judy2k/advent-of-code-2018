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


fn frequencies(v: Vec<i32>) -> impl Iterator<Item = i32> {
    vec!(0 as i32).into_iter().chain(v.into_iter().cycle()).aggregate()
}


fn calculate_result(path: &str) -> Result<i32, io::Error> {
    let mut seen_vals = HashSet::new();
    for frequency in frequencies(int_file(path)?) {
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

#[test]
fn test_frequencies() {
    assert_eq!(frequencies(vec!(4, -5, 6)).take(6).collect::<Vec<i32>>(), vec!(0, 4, -1, 5, 9, 4));
}
