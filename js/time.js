// http://worldtimeapi.org/api/ip

const api_url = 'http://worldtimeapi.org/api/ip';
async function getTime() {
    const response = await fetch(api_url);
    const data = await response.json();
    console.log(data);
    console.log(data.datetime);
    console.log(data.timezone);
    
    document.getElementById('hr').textContent = data.datetime;
    document.getElementById('reg').textContent = data.timezone;
}


getTime();


// implementacion: 
{/* <p>Hora: <span id="hr"></span><br/>
                Region: <span id="reg"></span></p> */}

// "hr" y "reg" son Id de elemento