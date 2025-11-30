/**
 * @param {number[]} deadline
 * @param {number[]} profit
 * @returns {number[]}
 */

class Solution {
    jobSequencing(deadline, profit) {
        // code here
        const n= deadline.length;
        const jobs=[];
        for(let i =0;i<n;i++)
        {
            jobs.push([deadline[i],profit[i]]);
        }
        jobs.sort((a,b)=>b[1]-a[1]);
        let maxD=0;
        for(let i =0;i<n;i++)
        {
            if(deadline[i]>maxD)maxD=deadline[i];
        }
        const parent=new Array(maxD+1);
        for(let i =0;i<=maxD;i++) parent[i]=i;
        const find=(x)=>{
            if (parent[x]!==x)parent[x]=find(parent[x]);
            return parent[x];
        };
        const merge=(a,b)=>{
            parent[a]=b;
        };
        let count=0;
        let totalProfit=0;
        for(let[d,p]of jobs)
        {
            let slot=find(d);
            if (slot>0)
            {
                merge(slot,slot-1);
                count++;
                totalProfit+=p;
            }
        }
        return [count,totalProfit];
    }
}