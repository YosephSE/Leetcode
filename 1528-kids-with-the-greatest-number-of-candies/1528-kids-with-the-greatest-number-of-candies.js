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
        if(candies2[i] >= max){
            res.push(true)
        }else{
            res.push(false)
        }
    }
        return res
        
};