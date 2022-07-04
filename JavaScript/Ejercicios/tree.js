var floor = 5;
var floor_math = 2 * floor + 1;

for (let i = 0; i < floor_math; i++){
    if (i % 2 === 1){
        console.log(" ".repeat(Math.trunc((floor - i) / 2)) + "+".repeat(i) + " ".repeat(Math.trunc((floor - i) / 2)))
    }
}

