// http://worldtimeapi.org/api/ip

const api_url = 'http://worldtimeapi.org/api/ip';
async function getTime() {
    const response = await fetch(api_url);
    const data = await response.json();
    console.log(data);
    console.log(data.datetime);
    console.log(data.timezone);
    
    const hora = data.datetime.substring(11, 16)
    const dia = data.datetime.substring(0, 10)

    document.getElementById('hr').textContent = hora;
    document.getElementById('reg').textContent = data.timezone;
    document.getElementById('dia').textContent = dia;
}


getTime();


// implementacion: 
{/* <p>Hora: <span id="hr"></span><br/>
                Region: <span id="reg"></span></p> */}

// "hr" y "reg" son Id de elemento