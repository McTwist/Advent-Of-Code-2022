use std::fs;

fn calc_priority(a: char) -> i32 {
	if 'a' <= a && a <= 'z' {
		return a as i32 - 'a' as i32 + 1 as i32;
	}
	if 'A' <= a && a <= 'Z' {
		return a as i32 - 'A' as i32 + 27 as i32;
	}
	unreachable!();
}

fn intersect(a: &String, b: &String) -> String {
	a.chars().filter(|&c| b.contains(c)).collect()
}

fn calc_similar(a: &String, b: &String) -> i32 {
	return calc_priority(intersect(a, b).chars().next().unwrap())
}

fn solve1(rucksacks: &[String]) -> i32 {
	rucksacks.iter().fold(0, |a, l| {
		let (first, second) = l.split_at(l.chars().count() / 2);
		a + calc_similar(&first.to_string(), &second.to_string())
	})
}

fn solve2(rucksacks: &[String]) -> i32 {
	(0..(rucksacks.len() / 3)).fold(0, |t, i| {
		let (first, second, third) = if let [first, second, third] = &rucksacks[(i*3)..(i*3+3)] {
			(first, second, third)
		} else {
			unreachable!()
		};
		t + calc_similar(&intersect(first, second), third)
	})
}

fn main() {
	let rucksacks: Vec<String> = fs::read_to_string("input.txt")
		.expect("File does not exist")
		.split("\n")
		.map(|a| a.to_string())
		.collect();
	println!("{:?}", solve1(&rucksacks));
	println!("{:?}", solve2(&rucksacks));
}
