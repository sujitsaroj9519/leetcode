/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let a = init;
    return {
        increment :()=> ++a,
        decrement :()=> --a,
        reset:()=> a=init,
    }
    // function increament(){
    //     return ++a;
    // }

    // function decrement(){
    //     return --a;
    // }

    // function reset(){
    //     return (a=init);
    // }

    // return { increament, decrement, reset};
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

// Input: init = 0, calls = ["increment","increment","decrement","reset","reset"]
// Output: [1,2,1,0,0]

// Input: init = 5, calls = ["increment","reset","decrement"]
// Output: [6,5,4]