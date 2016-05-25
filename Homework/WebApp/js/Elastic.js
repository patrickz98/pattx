Elastic = {};

Elastic.baseUrl = "http://patrick-macbook.local/homework/data.php?";

Elastic.getData = function(url, endPoint)
{
    var script = WebLibSimple.createAnyAppend("script", document.body);
    script.src = url + "&endPoint=" + endPoint;
}

Elastic.log = function(response)
{
    console.log("--> Elastic.log - response: " + JSON.stringify(response));
}

//
// Data by Uuid
// atcion --> f
//

Elastic.getByUuid = function(type, uuid, callback)
{
    var action = "f";

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&uuid=" + uuid;
    Elastic.getData(url, callback);
}

//
// Data by id
// atcion --> g
//

Elastic.getById = function(type, id, callback)
{
    var action = "g";

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&id=" + id;
    Elastic.getData(url, callback);
}

//
// post data --> uuid
// atcion --> p
//

Elastic.postByUuid = function(type, uuid, json, callback)
{
    var action = "p";
    var json = JSON.stringify(json);

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&uuid=" + uuid + "&json=" + json;
    // Elastic.getData(url, "Elastic.log");
    Elastic.getData(url, callback);
}

//
// put/update data --> id
// atcion --> u
//

Elastic.updateById = function(type, id, json)
{
    console.log("updateById: " + id);

    var action = "u";

    var json = encodeURI(JSON.stringify(json));

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&id=" + id + "&json=" + json;
    Elastic.getData(url, "Elastic.log");
}

Elastic.delteById = function(type, id)
{
    console.log("delteById: " + id);

    var action = "d";

    var url = Elastic.baseUrl + "action=" + action + "&type=" + type + "&id=" + id;
    Elastic.getData(url, "Elastic.log");
}

// var json = {
//     "Name": "Mr. Zoluu",
//     "ShortName": "Zo",
//     "Subjects": "Space",
//     "Notes": "Cool",
//     "School": "GSH",
//     "uuid": "PATpLAJgPkDt6iI38jVw",
//     "id": "AVTK_TiEBE-ZAybXntx0"
// };

// Elastic.updateById("teacher", "AVTK_TiEBE-ZAybXntx0", json);

// Elastic.postByUuid("teacher", "PATpLAJgPkDt6iI38jVw", json);
// Elastic.getById("teacher", "AVTIlMRbYnkdd7Ja7TUV");
