/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var arrr = [];
    for (var i=0; i <arr.length; i++){
        if (fn(arr[i],i)){
            arrr.push(arr[i]);
        }
    }
    
    return arrr
};

// Input: arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }
// Output: [-2,0,1,2]

// Input: arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
// Output: [1]

// Input: arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
// Output: [20,30]