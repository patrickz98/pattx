Elastic = {};

Elastic.baseUrl = "http://patrick-macbook.local/homework/data.php?";

Elastic.getData = function(url, endPoint)
{
    var xmlhttp = null;

    if (window.XMLHttpRequest)
    {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else
    {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function()
    {
        console.log("xmlhttp.readyState: " + xmlhttp.readyState);

        if ((xmlhttp.readyState == 4) && (xmlhttp.status == 200))
        {
            var response = xmlhttp.responseText;
            var funct = endPoint;

            funct(response);
            // return xmlhttp.responseText;
        }
    }

    // json = encodeURI(json);

    xmlhttp.open("GET", url, false);
    xmlhttp.send();
}

Elastic.setEntrys = function(response)
{
    console.log("--> Elastic.loaded - response: " + response);
    Data.entrys = JSON.parse(response);
}

Elastic.getByUuid = function(type, uuid)
{
    var action = "f";

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&uuid=" + uuid;
    Elastic.getData(url, Elastic.setEntrys);
}

Elastic.log = function(response)
{
    console.log("--> Elastic.log - response: " + response);
}

Elastic.getById = function(type, id)
{
    var action = "g";

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&id=" + id;
    Elastic.getData(url, Elastic.log);
}

Elastic.postByUuid = function(type, uuid, json)
{
    var action = "p";
    var json = JSON.stringify(json);

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&uuid=" + uuid + "&json=" + json;
    Elastic.getData(url, Elastic.log);
}

Elastic.updateById = function(type, id, json)
{
    var action = "u";

    delete json.id;

    var json = JSON.stringify(json);

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&id=" + id + "&json=" + json;
    Elastic.getData(url, Elastic.log);
}

Elastic.getByUuid("teacher", "PATpLAJgPkDt6iI38jVw");

var json = {
    "Name": "Mr. Shoot",
    "ShortName": "Sh",
    "Subjects": "Pistols",
    "Notes": "",
    "School": "Avh",
    "uuid": "PATpLAJgPkDt6iI38jVw",
    "id": "AVTNvhCakm7_y62aR-SV"
};

// Elastic.updateById("teacher", "AVTNvhCakm7_y62aR-SV", json);

// Elastic.postByUuid("teacher", "PATpLAJgPkDt6iI38jVw", json);
// Elastic.getById("teacher", "AVTIlMRbYnkdd7Ja7TUV");
