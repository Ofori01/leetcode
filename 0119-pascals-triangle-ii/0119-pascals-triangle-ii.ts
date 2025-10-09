function getRow(rowIndex: number): number[] {
        // using recursion

        let row = new Array(rowIndex+1).fill(1)

        // base case
        if (row.length === 1) return row;

        let prev_row = getRow(rowIndex-1) 

        // build row
        for (let i = 1; i < rowIndex  ; i++ ){
            row[i] = prev_row[i-1] + prev_row[i]
        }
        
        return row 


};