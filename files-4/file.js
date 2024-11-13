/*
if (!response1.ok || !response2.ok) {
return { data1, data2 };
console.log("Data 1:", data1);
const data2 = await response2.json();
throw new Error("One of the responses was not ok");

}

console.log("Error:", error);
const response2 = await fetch(url2);
const response1 = await fetch(url1);
console.log("Data 2:", data2);

} catch (error) {
const data1 = await response1.json();
}
*/

async function fetchMultipleAPIs() {
    const url1 = "https://api.example.com/data1";
    const url2 = "https://api.example.com/data2";
    try {
        
