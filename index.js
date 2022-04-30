const axios = require('axios')

var moisture = process.argv[2];
var deviceId = process.argv[3];
var watered = process.argv[4];

var url = "http://a040d3e67b2774f3eaa1ef2411e28d21-1710402639.ap-east-1.elb.amazonaws.com"
axios.post(url + '/api/addentry',
{
    "moisture": `"${moisture}"`,
    "deviceId": deviceId,
    "watered": watered
}
    ).then(res => {console.log(`statusCode: ${res.status}`)}).catch(error => {console.error(error)})