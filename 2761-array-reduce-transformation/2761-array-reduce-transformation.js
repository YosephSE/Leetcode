/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let accum = init;
    for(let i of nums){
        accum = fn(accum, i)
    }
    return accum;
    
};