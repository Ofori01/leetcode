function minOperations(logs: string[]): number {
    let currentLevel = 0
    for(let i = 0; i < logs.length; i++){
        if(logs[i]==="../"){
           currentLevel !==0 ? --currentLevel : currentLevel
        }
        else if(logs[i] === './'){}
        else {
            currentLevel++
        }
    }
    return currentLevel
};