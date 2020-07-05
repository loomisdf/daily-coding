/* 
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add 
up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/
func canAddUp(array: [Int], to k: Int) -> Bool {
    // Single pass using a set
    let set = Set(array)
    for num in array {
        if set.contains(k - num) {
            return true
        }
    }
    // Brute force techqnique
//    for i in 0..<array.count {
//        for v in (i+1)..<array.count {
//            if array[v] + array[i] == k {
//                return true
//            }
//        }
//    }
    return false
}

let arr = [1, 2, 3, 4]

let value = canAddUp(array: arr, to: 3)
print(value)
