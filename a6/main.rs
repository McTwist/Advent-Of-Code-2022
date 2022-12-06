use std::fs;

fn distinct(data: &str) -> bool {
	for i in 0..data.len() {
		for n in (i+1 as usize)..data.len() {
			if data.chars().nth(i).unwrap() == data.chars().nth(n).unwrap() {
				return false
			}
		}
	}
	return true
}

fn marker(data: &String, distinct: usize) -> i32 {
	for i in (distinct-1)..data.len() {
		if distinct(&data[(i-(distinct-1))..(i+1)]) {
			return (i+1) as i32;
		}
	}
	unreachable!()
}

fn solve1(data: &String) -> i32 {
	marker(data, 4)
}

fn solve2(data: &String) -> i32 {
	marker(data, 14)
}

fn main() {
	let data: String = fs::read_to_string("input.txt")
		.expect("File does not exist");
	println!("{:?}", solve1(&data));
	println!("{:?}", solve2(&data));
}
