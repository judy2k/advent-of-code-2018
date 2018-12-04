use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io;
use std::io::prelude::*;

fn main() {
    println!("{}", solve("../input.txt").unwrap())
}

fn twos_and_threes(s: &str) -> (bool, bool) {
    let mut counts = HashMap::<char, i64>::new();

    for c in s.chars() {
        let count = counts.entry(c).or_insert(0);
        *count += 1;
    }

    let count_set = counts.values().collect::<HashSet<&i64>>();
    (count_set.contains(&2), count_set.contains(&3))
}

fn read_file(path: &str) -> Result<Vec<String>, io::Error> {
    let f = File::open(path)?;
    let result = io::BufReader::new(f);
    Ok(result.lines().map(Result::unwrap).collect::<Vec<String>>())
}

fn solve(path: &str) -> Result<i64, io::Error> {
    let mut two_count = 0;
    let mut three_count = 0;

    for line in read_file(path)?.iter() {
        let (two, three) = twos_and_threes(line);
        if two {
            two_count+= 1;
        }
        if three {
            three_count+= 1;
        }
    }
    Ok(two_count * three_count)
}

#[test]
fn test_twos_and_threes() {
    assert_eq!(twos_and_threes("abcdef"), (false, false));
    assert_eq!(twos_and_threes("abadef"), (true, false));
    assert_eq!(twos_and_threes("abcbeb"), (false, true));
    assert_eq!(twos_and_threes("ababeb"), (true, true));
}

#[test]
fn test_read_file() {
    assert_eq!(
        read_file("../sample_input.txt").unwrap(),
        vec!("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab",)
    )
}

#[test]
fn test_solve() {
    assert_eq!(solve("../sample_input.txt").unwrap(), 12);
}
