// var let const

//arrow function
var sumatoria = (a, b) => {
    return a + b;
}
var sum = (a, b) => a + b;
var array = [1, 34, 34, 43, 34333, 3, 2];
array.forEach((element,index,array )=> {
    console.log(element, index);
    
});

function imprime(value, index, array) {
    console.log(value);

}
array.forEach(imprime);