use std::fs;

fn contains((a, b): &(i32, i32), (c, d): &(i32, i32)) -> bool {
	a <= c && b >= d
}
fn overlap((a, b): &(i32, i32), (c, d): &(i32, i32)) -> bool {
	contains(&(*a, *b), &(*c, *d)) || (a <= d && b >= d)
}

fn solve1(assignments: &[((i32, i32), (i32, i32))]) -> i32 {
	assignments.iter().filter(|(a, b)| contains(a, b) || contains(b, a)).count() as i32
}

fn solve2(assignments: &[((i32, i32), (i32, i32))]) -> i32 {
	assignments.iter().filter(|(a, b)| overlap(a, b) || overlap(b, a)).count() as i32
}

fn main() {
	let assignments: Vec<((i32, i32), (i32, i32))> = fs::read_to_string("input.txt")
		.expect("File does not exist")
		.split("\n")
		.map(|a| {
			let mut q = a.splitn(2, ",")
				.map(|b| {
					let mut q = b.splitn(2, "-")
						.map(|s| s.parse::<i32>().unwrap());
					(q.next().unwrap(), q.next().unwrap())
				});
			(q.next().unwrap(), q.next().unwrap())
		}).collect();
	println!("{:?}", solve1(&assignments));
	println!("{:?}", solve2(&assignments));
}
