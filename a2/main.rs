use std::fs;

fn solve1(strategy: &[(i32, i32)]) -> i32 {
	strategy.iter().fold(0, |a, (you, me)| {
		a + me + 1 + match you - me {
			1 | -2 => 0,
			0 => 3,
			-1 | 2 => 6,
			_ => unreachable!(),
		}
	})
}

fn solve2(strategy: &[(i32, i32)]) -> i32 {
	strategy.iter().fold(0, |a, (you, me)| {
		a + (((you + 3) + (me - 1)) % 3) + 1 + (me * 3)
	})
}

fn main() {
	let strategy: Vec<(i32, i32)> = fs::read_to_string("input.txt")
		.expect("File does not exist")
		.split("\n")
		.map(|item| {
			let mut q = item.splitn(2, " ").map(|s| if "ABC".contains(s) {
				s.chars().nth(0).unwrap() as i32 - 'A' as i32
			} else {
				s.chars().nth(0).unwrap() as i32 - 'X' as i32
			});
			(q.next().unwrap(), q.next().unwrap())
		}).collect();
	println!("{:?}", solve1(&strategy));
	println!("{:?}", solve2(&strategy));
}
