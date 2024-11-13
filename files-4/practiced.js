const processResponse = (response) => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

fetch('https://api.example.com/first')
    .then(processResponse)
    .then(data => {
        console.log('First API data:', data);
        return fetch('https://api.example.com/second');
    })
    .then(processResponse)
    .then(data2 => console.log('Second API data:', data2))
    .catch(error => console.error('Error:', error));

// -------------------------------------------------------------------------------------------------
const apiUrl1 = 'https://api.example.com/first';
const apiUrl2 = 'https://api.example.com/second';
const apiUrl3 = 'https://api.example.com/third';

const handleError = (response) => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
};

async function fetchData() {
    try {
        const response1 = await fetch(apiUrl1);
        handleError(response1);
        const data1 = await response1.json();
        console.log('First API data:', data1);

        const response2 = await fetch(apiUrl2);
        handleError(response2);
        const data2 = await response2.json();
        console.log('Second API data:', data2);

        if (data2.someCondition) {
            const response3 = await fetch(apiUrl3);
            handleError(response3);   
            const data3 = await response3.json();
            console.log('Third API data:', data3);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

fetchData();

// -------------------------------------------------------------------------------------------------

async function getData() {
    const url = "https://api.example.com/data";

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        console.log("Data:", data);
        return data;
    } catch (error) {
        console.log("Error:", error);
    }
}