// Validate subsequence
// https://www.algoexpert.io/questions/Validate%20Subsequence

// arr = [1,1,6,1]
arr = [5,1,22,6,-1,8,10]
// sequence = [1,1,1,6]
sequence = [-1,8,10]


function isValidSubsequence(array, sequence) {
    for(let num=0;num<sequence.length;num++){
        // Check if the number exist in arr
        if(array.includes(sequence[num])){
            console.log(sequence[num], " is ", array[array.indexOf(sequence[num])])
            array.splice(0,array.indexOf(sequence[num])+1);
            console.log("New array", array)
            // T > shrink the visited part of the array
        }else{
            // F > Return false
            return false
        }
    }
    return true   // If it goes trough all of the sequence > return true
}
console.log(isValidSubsequence(arr,sequence))