use std::fs;
use std::collections::HashMap;

fn solve1(dirs: &Vec<&i32>) -> i32 {
	dirs.iter().filter(|a| **a < &100000).fold(0, |a, b| a + **b)
}

fn solve2(dirs: &Vec<&i32>) -> i32 {
	let total_disk: i32 = 70000000;
	let required_disk: i32 = 30000000;
	let current_used: i32 = **dirs.iter().max().unwrap();
	let to_be_removed: i32 = required_disk - (total_disk - current_used);
	dirs.iter().fold(total_disk, |a, b| if **b > to_be_removed && **b < a { **b } else { a })
}

fn main() {
	let mut dirs: HashMap<Vec<String>, i32> = HashMap::new();
	dirs.insert(vec![], 0);
	let mut stack: Vec<String> = Vec::new();
	for line in fs::read_to_string("input.txt")
			.expect("File does not exist")
			.split("\n") {
		match line.split(" ").collect::<Vec<&str>>()[..] {
			["$", "cd", d] => match d {
				"/" => { stack.clear(); },
				".." => { stack.pop(); },
				f => { stack.push(f.to_string()); },
			},
			["$", "ls"] => {},
			["dir", d] => {},
			[s, _] => {
				let s = s.parse::<i32>().unwrap();
				for i in 0..(stack.len()+1) {
					dirs.entry(stack[0..i].to_vec()).and_modify(|a| *a += s as i32).or_insert(s as i32);
				}
			},
			_ => unreachable!(),
		}
	}

	let sizes: Vec<&i32> = dirs.iter().map(|(_, b)| b).collect();

	println!("{:?}", solve1(&sizes));
	println!("{:?}", solve2(&sizes));
}
