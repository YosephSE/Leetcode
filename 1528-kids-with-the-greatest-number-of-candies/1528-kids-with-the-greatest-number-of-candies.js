/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */var kidsWithCandies = function(candies, extraCandies) {
    let candies2 = candies
    let res = []
    let max = Math.max(...candies)
    for(i = 0; i < candies.length; i++){
        candies2[i] += extraCandies
        res.push(candies2[i] >= max)
    }
        return res
        
};