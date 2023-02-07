// The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

// Given two integers x and y, return the Hamming distance between them.

 

// Example 1:

// Input: x = 1, y = 4
// Output: 2
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        ↑   ↑
// The above arrows point to positions where the corresponding bits are different.
// Example 2:

// Input: x = 3, y = 1
// Output: 1
 

// Constraints:

// 0 <= x, y <= 231 - 1

const hammingDistance = function (x, y) {
	let newX = x.toString(2);
	let newY = y.toString(2);
    let count = 0

	if (newX.length > newY.length) {
		for (let i = newY.length; i < newX.length; i++) {
			newY = 0 + newY;
		}
	} else if (newY.length > newX.length) {
		for (let i = newX.length; i < newY.length; i++) {
			newX = 0 + newX;
		}
	}

    for (let j = 0; j < newX.length; j++) {
        if (newX[j] !== newY[j]) {
            count++
        }
    }
	return count
};

console.log(hammingDistance(1, 4));
