use std::fs;

fn solve1(calories: &[Vec<i32>]) -> i32 {
	calories.iter().fold(std::i32::MIN, |a, b| {
		a.max(b.iter().sum())
	})
}

fn solve2(calories: &[Vec<i32>]) -> i32 {
	let mut c1: Vec<i32> = calories.iter().map(|a| {
		a.iter().sum()
	}).collect();
	c1.sort_by(|a, b| b.partial_cmp(a).unwrap());
	c1[0..3].iter().sum()
}

fn main() {
	let calories: Vec<Vec<i32>> = fs::read_to_string("input.txt")
		.expect("File does not exist")
		.split("\n\n")
		.map(|item| {
			item.split("\n").map(|s| s.parse::<i32>().unwrap()).collect()
		}).collect();
	println!("{:?}", solve1(&calories));
	println!("{:?}", solve2(&calories));
}
